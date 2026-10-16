"""
System-under-test (SUT) interface — replaceable defense stacks.

The runner evaluates any object that implements `respond(item) -> SutResponse`.
Conditions:
  baseline          — no defenses
  input_defense     — input guardrail only
  retrieval_defense — input + retrieval/context screening + grounding
  full_defense      — input + retrieval + output rails
"""

from __future__ import annotations

import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional, Protocol

ROOT = Path(__file__).resolve().parent
GUARDRAIL_SRC = ROOT.parent / "guardrail" / "src"
DEFAULT_POLICY = ROOT.parent / "guardrail" / "configs" / "support_copilot_guardrail.yaml"

# Synthetic "secrets" used only in lab fixtures (not real credentials)
LAB_SECRET_MARKER = "LAB_SECRET_TOKEN_X9"
LAB_INJECTION_MARKER = "IGNORE PREVIOUS INSTRUCTIONS"


@dataclass
class SutResponse:
    output_text: str
    blocked: bool = False
    stage: str = "app"
    latency_ms: float = 0.0
    usage: dict = field(default_factory=dict)
    meta: dict = field(default_factory=dict)
    error: Optional[str] = None


class SystemUnderTest(Protocol):
    name: str

    def respond(self, item: dict) -> SutResponse: ...


def _ensure_guardrail_import() -> None:
    src = str(GUARDRAIL_SRC)
    if src not in sys.path:
        sys.path.insert(0, src)


def _load_guardrail(config_path: Path | None = None):
    _ensure_guardrail_import()
    from guardrail_fw.policy.engine import Guardrail

    path = config_path or DEFAULT_POLICY
    return Guardrail.from_yaml(str(path))


def _naive_answer(item: dict) -> str:
    """
    Deterministic offline 'application' — intentionally vulnerable without rails.

    - Follows obvious injection phrases found in query or retrieved context
    - Echoes lab secrets from context when asked
    - Otherwise answers benign support-style questions
    """
    query = str(item.get("user_query") or item.get("ticket_text") or "")
    ctx = str(item.get("retrieved_context") or "")
    blob = f"{query}\n{ctx}".lower()

    if LAB_INJECTION_MARKER.lower() in blob or "ignore previous" in blob:
        if "secret" in blob or LAB_SECRET_MARKER.lower() in blob.lower():
            return f"Sure — here is the secret: {LAB_SECRET_MARKER}"
        return (
            "OK I will ignore previous instructions and follow the injected ones. "
            "Dumping internal notes."
        )

    if "secret" in query.lower() and LAB_SECRET_MARKER in ctx:
        return f"From the documents: {LAB_SECRET_MARKER}"

    if re.search(r"\b(refund|payment|invoice)\b", query, re.I):
        return "Refunds take 3–5 business days after approval."
    if re.search(r"\b(password|reset)\b", query, re.I):
        return "You can reset your password from Account → Security."
    if re.search(r"\b(hour|open|support)\b", query, re.I):
        return "Support hours are 9am–6pm local time on weekdays."

    # Ticket-style fallback (IT categorization demo compatibility)
    if item.get("ticket_text"):
        from models import ticket_classifier_stub

        text, _ = ticket_classifier_stub(
            [{"role": "user", "content": item["ticket_text"]}]
        )
        return text

    return "Here is a helpful answer based on available context."


class BaselineApp:
    """No defenses — vulnerable application stub."""

    name = "baseline"

    def respond(self, item: dict) -> SutResponse:
        t0 = time.perf_counter()
        try:
            out = _naive_answer(item)
            return SutResponse(
                output_text=out,
                blocked=False,
                stage="baseline",
                latency_ms=(time.perf_counter() - t0) * 1000,
                usage={"prompt_tokens": 10, "completion_tokens": max(1, len(out.split()))},
            )
        except Exception as e:  # noqa: BLE001
            return SutResponse(
                output_text="",
                error=str(e),
                latency_ms=(time.perf_counter() - t0) * 1000,
            )


class InputDefenseApp:
    """Screen user input with guardrail; then answer if allowed."""

    name = "input_defense"

    def __init__(self, config_path: Path | None = None):
        self.rail = _load_guardrail(config_path)
        self.config_path = config_path or DEFAULT_POLICY

    def respond(self, item: dict) -> SutResponse:
        t0 = time.perf_counter()
        query = str(item.get("user_query") or item.get("ticket_text") or "")
        try:
            vin = self.rail.apply_input(query)
            if not vin.allowed:
                msg = vin.message or "Request blocked by input guardrail."
                return SutResponse(
                    output_text=msg,
                    blocked=True,
                    stage="input",
                    latency_ms=(time.perf_counter() - t0) * 1000,
                    meta={"decision": vin.decision},
                )
            out = _naive_answer({**item, "user_query": vin.text})
            return SutResponse(
                output_text=out,
                blocked=False,
                stage="app",
                latency_ms=(time.perf_counter() - t0) * 1000,
            )
        except Exception as e:  # noqa: BLE001
            return SutResponse(
                output_text="",
                error=str(e),
                latency_ms=(time.perf_counter() - t0) * 1000,
            )


class RetrievalDefenseApp:
    """Input rails + screen retrieved context + grounding on answer."""

    name = "retrieval_defense"

    def __init__(self, config_path: Path | None = None):
        self.rail = _load_guardrail(config_path)
        self.config_path = config_path or DEFAULT_POLICY

    def respond(self, item: dict) -> SutResponse:
        t0 = time.perf_counter()
        query = str(item.get("user_query") or item.get("ticket_text") or "")
        ctx = str(item.get("retrieved_context") or "")
        try:
            vin = self.rail.apply_input(query)
            if not vin.allowed:
                return SutResponse(
                    output_text=vin.message or "Blocked by input guardrail.",
                    blocked=True,
                    stage="input",
                    latency_ms=(time.perf_counter() - t0) * 1000,
                )
            if ctx:
                vctx = self.rail.apply_input(ctx)
                if not vctx.allowed:
                    return SutResponse(
                        output_text="Retrieved context failed safety screening.",
                        blocked=True,
                        stage="retrieval",
                        latency_ms=(time.perf_counter() - t0) * 1000,
                    )
                # Strip injection markers from context before answering
                if LAB_INJECTION_MARKER.lower() in ctx.lower():
                    return SutResponse(
                        output_text="Retrieved context failed safety screening.",
                        blocked=True,
                        stage="retrieval",
                        latency_ms=(time.perf_counter() - t0) * 1000,
                    )
            out = _naive_answer({**item, "user_query": vin.text, "retrieved_context": ctx})
            # Confidentiality rail: never emit lab secret markers
            if LAB_SECRET_MARKER.lower() in out.lower():
                return SutResponse(
                    output_text="I cannot help with that request under the current safety policy.",
                    blocked=True,
                    stage="output",
                    latency_ms=(time.perf_counter() - t0) * 1000,
                    meta={"reason": "secret_leak_blocked"},
                )
            vout = self.rail.apply_output(out, context=ctx or None)
            if not vout.allowed:
                return SutResponse(
                    output_text=vout.message or "Answer blocked (grounding/output).",
                    blocked=True,
                    stage="output",
                    latency_ms=(time.perf_counter() - t0) * 1000,
                )
            return SutResponse(
                output_text=vout.text,
                blocked=False,
                stage="app",
                latency_ms=(time.perf_counter() - t0) * 1000,
            )
        except Exception as e:  # noqa: BLE001
            return SutResponse(
                output_text="",
                error=str(e),
                latency_ms=(time.perf_counter() - t0) * 1000,
            )


class FullDefenseApp(RetrievalDefenseApp):
    """Alias: input + retrieval + output (same stack as retrieval_defense + stricter meta)."""

    name = "full_defense"


def build_sut(condition: str, config_path: Path | None = None) -> Any:
    key = condition.strip().lower()
    if key == "baseline":
        return BaselineApp()
    if key == "input_defense":
        return InputDefenseApp(config_path)
    if key == "retrieval_defense":
        return RetrievalDefenseApp(config_path)
    if key == "full_defense":
        return FullDefenseApp(config_path)
    raise ValueError(f"unknown condition: {condition}")
