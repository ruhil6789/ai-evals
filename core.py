"""
Core types for a framework-agnostic Evals harness.

Mental model:
  Evals are structured tests for nondeterministic generators.
  Pass / Fail / Error are distinct outcomes (errors are not failures).

Pipeline:
  1. Describe the task as an Eval (schema + graders)
  2. Run with a prompt template + dataset + replaceable SUT
  3. Persist per-sample records → analyze → regress → iterate
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Tuple
import json
import time
import uuid


class RunStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"


class SampleOutcome(str, Enum):
    """Pass / fail / error are reported separately."""

    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"


@dataclass
class DataSourceConfig:
    """Schema for eval items (analog of OpenAI data_source_config)."""

    type: str = "custom"
    item_schema: dict = field(default_factory=dict)
    include_sample_schema: bool = True

    def validate_item(self, item: dict) -> list:
        """Return list of validation errors (empty = ok)."""
        errors = []
        props = self.item_schema.get("properties", {})
        required = self.item_schema.get("required", list(props.keys()))
        for key in required:
            if key not in item:
                errors.append(f"missing required field: {key}")
        for key, spec in props.items():
            if key in item and spec.get("type") == "string" and not isinstance(item[key], str):
                errors.append(f"{key} must be string")
            if key in item and spec.get("type") == "object" and not isinstance(item[key], dict):
                errors.append(f"{key} must be object")
        return errors


@dataclass
class EvalSpec:
    """An eval definition: task name + data schema + testing criteria (graders)."""

    name: str
    data_source_config: DataSourceConfig
    testing_criteria: list  # list[Grader]
    id: str = field(default_factory=lambda: f"eval_{uuid.uuid4().hex[:24]}")
    created_at: float = field(default_factory=time.time)
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "object": "eval",
            "id": self.id,
            "name": self.name,
            "created_at": int(self.created_at),
            "data_source_config": {
                "type": self.data_source_config.type,
                "item_schema": self.data_source_config.item_schema,
                "include_sample_schema": self.data_source_config.include_sample_schema,
            },
            "testing_criteria": [g.to_dict() for g in self.testing_criteria],
            "metadata": self.metadata,
        }


@dataclass
class GradeResult:
    grader_name: str
    grader_id: str
    passed: bool
    score: float  # 0.0–1.0
    detail: str = ""
    raw: Any = None

    def to_dict(self) -> dict:
        return {
            "grader_name": self.grader_name,
            "grader_id": self.grader_id,
            "passed": self.passed,
            "score": self.score,
            "detail": self.detail,
            "raw": self.raw,
        }


@dataclass
class SampleResult:
    """One dataset row after model/SUT generation + grading."""

    item: dict
    output_text: str
    grades: list = field(default_factory=list)
    error: Optional[str] = None
    usage: dict = field(default_factory=dict)
    sample_id: str = ""
    latency_ms: Optional[float] = None
    condition: str = ""
    model_version: str = ""
    dataset_version: str = ""
    run_id: str = ""

    def __post_init__(self) -> None:
        if not self.sample_id:
            self.sample_id = str(
                self.item.get("sample_id")
                or self.item.get("id")
                or f"anon_{uuid.uuid4().hex[:8]}"
            )

    @property
    def outcome(self) -> SampleOutcome:
        if self.error:
            return SampleOutcome.ERROR
        if not self.grades:
            return SampleOutcome.ERROR
        if all(g.passed for g in self.grades):
            return SampleOutcome.PASS
        return SampleOutcome.FAIL

    @property
    def passed(self) -> bool:
        return self.outcome == SampleOutcome.PASS

    def to_record(self) -> dict:
        """Per-sample log row (no secrets / PII by convention — callers sanitize)."""
        return {
            "run_id": self.run_id,
            "sample_id": self.sample_id,
            "condition": self.condition,
            "model_version": self.model_version,
            "dataset_version": self.dataset_version,
            "category": self.item.get("category"),
            "expected_behavior": self.item.get("expected_behavior"),
            "output_text": self.output_text,
            "grader_results": {g.grader_name: g.to_dict() for g in self.grades},
            "outcome": self.outcome.value,
            "passed": self.passed,
            "latency_ms": self.latency_ms,
            "error": self.error,
            "usage": self.usage,
        }


@dataclass
class ExperimentConfig:
    """
    Full experiment configuration for reproducibility.

    Hosted models may still be nondeterministic; record trials + settings anyway.
    """

    condition: str
    model_version: str
    dataset_version: str
    dataset_path: str
    dataset_hash: str
    prompt_version: str
    prompt_template: list
    grader_version: str
    guardrail_config_path: Optional[str] = None
    guardrail_config_hash: Optional[str] = None
    temperature: Optional[float] = None
    generation_settings: dict = field(default_factory=dict)
    seed: Optional[int] = None
    software_commit: Optional[str] = None
    trial: int = 1
    notes: str = ""
    extra: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class EvalRun:
    """Analog of OpenAI eval.run — local, synchronous by default."""

    eval_id: str
    name: str
    model: str
    id: str = field(default_factory=lambda: f"evalrun_{uuid.uuid4().hex[:24]}")
    status: RunStatus = RunStatus.QUEUED
    created_at: float = field(default_factory=time.time)
    samples: list = field(default_factory=list)
    error: Optional[str] = None
    metadata: dict = field(default_factory=dict)
    prompt_template: list = field(default_factory=list)
    config: Optional[ExperimentConfig] = None

    @property
    def result_counts(self) -> dict:
        total = len(self.samples)
        errored = sum(1 for s in self.samples if s.outcome == SampleOutcome.ERROR)
        passed = sum(1 for s in self.samples if s.outcome == SampleOutcome.PASS)
        failed = sum(1 for s in self.samples if s.outcome == SampleOutcome.FAIL)
        return {
            "total": total,
            "errored": errored,
            "failed": failed,
            "passed": passed,
        }

    def per_testing_criteria_results(self) -> list:
        buckets: Dict[str, dict] = {}
        for s in self.samples:
            for g in s.grades:
                key = f"{g.grader_name}-{g.grader_id}"
                if key not in buckets:
                    buckets[key] = {
                        "testing_criteria": key,
                        "passed": 0,
                        "failed": 0,
                    }
                if g.passed:
                    buckets[key]["passed"] += 1
                else:
                    buckets[key]["failed"] += 1
        return list(buckets.values())

    def per_model_usage(self) -> list:
        prompt_tokens = completion_tokens = invocation = 0
        for s in self.samples:
            invocation += 1
            prompt_tokens += int(s.usage.get("prompt_tokens", 0))
            completion_tokens += int(s.usage.get("completion_tokens", 0))
        return [
            {
                "model_name": self.model,
                "invocation_count": invocation,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens,
                "cached_tokens": 0,
            }
        ]

    def to_dict(self, report_url: str = "") -> dict:
        return {
            "object": "eval.run",
            "id": self.id,
            "eval_id": self.eval_id,
            "report_url": report_url,
            "status": self.status.value,
            "model": self.model,
            "name": self.name,
            "created_at": int(self.created_at),
            "result_counts": self.result_counts,
            "per_model_usage": self.per_model_usage(),
            "per_testing_criteria_results": self.per_testing_criteria_results(),
            "error": self.error,
            "metadata": self.metadata,
            "config": self.config.to_dict() if self.config else None,
        }

    def to_json(self, report_url: str = "") -> str:
        return json.dumps(self.to_dict(report_url=report_url), indent=2)


# Model callable: rendered messages → output text (+ optional usage)
ModelFn = Callable[[List[dict]], Tuple[str, dict]]
