"""
Analyze eval runs — result counts, per-criteria breakdown, markdown report,
multi-condition comparison.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from core import EvalRun, EvalSpec, SampleOutcome
from metrics import compare_conditions, compute_metrics


def summarize(run: EvalRun) -> str:
    rc = run.result_counts
    lines = [
        f"Run: {run.name} ({run.id})",
        f"Status: {run.status.value}",
        f"Model: {run.model}",
        f"Results: passed={rc['passed']} failed={rc['failed']} "
        f"errored={rc['errored']} total={rc['total']}",
        "",
        "Per testing criteria:",
    ]
    for row in run.per_testing_criteria_results():
        lines.append(
            f"  - {row['testing_criteria']}: "
            f"passed={row['passed']} failed={row['failed']}"
        )
    lines.append("")
    lines.append("Samples:")
    for i, s in enumerate(run.samples, 1):
        label = s.outcome.value.upper()
        pred = s.output_text if not s.error else f"<error: {s.error}>"
        ref = s.item.get("correct_label") or s.item.get("expected_behavior", "")
        ticket = s.item.get("ticket_text") or s.item.get("user_query") or s.item.get("sample_id")
        lines.append(
            f"  [{label}] #{i} id={s.sample_id} pred={pred!r} ref={ref!r}  q={ticket!r}"
        )
        for g in s.grades:
            lines.append(f"       grader={g.grader_name} score={g.score:.2f} {g.detail}")
    return "\n".join(lines)


def write_markdown_report(path: str | Path, run: EvalRun, eval_spec: EvalSpec) -> None:
    path = Path(path)
    rc = run.result_counts
    pass_rate = (rc["passed"] / rc["total"]) if rc["total"] else 0.0
    metrics = compute_metrics(run)

    md = [
        f"# Eval report: {run.name}",
        "",
        f"- **eval**: `{eval_spec.name}` (`{run.eval_id}`)",
        f"- **run**: `{run.id}`",
        f"- **status**: `{run.status.value}`",
        f"- **model**: `{run.model}`",
        f"- **condition**: `{metrics.get('condition')}`",
        f"- **pass rate**: **{pass_rate:.0%}** "
        f"({rc['passed']}/{rc['total']}; failed={rc['failed']}, errored={rc['errored']})",
        "",
        "## Security / utility metrics",
        "",
        f"- attack_success_rate: `{metrics['attack_success_rate']:.3f}` (n_attack={metrics['n_attack']})",
        f"- utility_rate: `{metrics['utility_rate']:.3f}` (n_benign={metrics['n_benign']})",
        f"- false_positive_rate: `{metrics['false_positive_rate']:.3f}`",
        f"- error_rate: `{metrics['error_rate']:.3f}`",
        f"- latency_ms: `{metrics['latency_ms']}`",
        "",
        "## Per-criteria results",
        "",
        "| Criteria | Passed | Failed |",
        "|----------|--------|--------|",
    ]
    for row in run.per_testing_criteria_results():
        md.append(
            f"| `{row['testing_criteria']}` | {row['passed']} | {row['failed']} |"
        )

    if run.config:
        md += ["", "## Experiment config", "", "```json", json.dumps(run.config.to_dict(), indent=2), "```"]

    md += ["", "## Samples", ""]
    for i, s in enumerate(run.samples, 1):
        label = s.outcome.value.upper()
        md.append(f"### #{i} — {label} (`{s.sample_id}`)")
        md.append("")
        md.append(f"- category: `{s.item.get('category')}`")
        md.append(f"- item keys: `{sorted(s.item.keys())}`")
        md.append(f"- output: `{s.output_text[:500]}`")
        md.append(f"- latency_ms: `{s.latency_ms}`")
        if s.error:
            md.append(f"- error: `{s.error}`")
        for g in s.grades:
            md.append(
                f"- grader `{g.grader_name}`: passed={g.passed} "
                f"score={g.score:.2f} — {g.detail}"
            )
        md.append("")

    md += [
        "## Usage",
        "",
        "```json",
        json.dumps(run.per_model_usage(), indent=2),
        "```",
        "",
        "## Research notes",
        "",
        "- Treat this report as a **signal**, not a certificate of safety.",
        "- Pass / fail / error are distinct — do not treat errors as safe refusals.",
        "- `RubricScoreGrader` heuristic scores are **not** validated human judgments.",
        "- Grow the dataset with production edge cases (logs → eval items).",
        "",
    ]
    path.write_text("\n".join(md), encoding="utf-8")


def write_summary_json(path: str | Path, metrics_by_condition: dict[str, dict]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "metrics": metrics_by_condition,
        "comparison": compare_conditions(metrics_by_condition),
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_comparison_md(
    path: str | Path,
    metrics_by_condition: dict[str, dict],
    regression_by_condition: Optional[dict[str, Any]] = None,
) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    cmp_ = compare_conditions(metrics_by_condition)
    lines = [
        "# Guardrail experiment comparison",
        "",
        "| Condition | ASR↓ | Utility↑ | FPR↓ | Error↓ | Pass | Latency mean (ms) |",
        "|-----------|------|----------|------|--------|------|-------------------|",
    ]
    for row in cmp_["conditions"]:
        lat = row["latency_mean_ms"]
        lat_s = f"{lat:.1f}" if lat is not None else "—"
        lines.append(
            f"| `{row['condition']}` | {row['attack_success_rate']:.3f} | "
            f"{row['utility_rate']:.3f} | {row['false_positive_rate']:.3f} | "
            f"{row['error_rate']:.3f} | {row['pass_rate']:.3f} | {lat_s} |"
        )
    lines += [
        "",
        "ASR = attack success rate (lower is better). "
        "Utility = benign helpfulness. FPR = benign false refusals.",
        "",
    ]
    if regression_by_condition:
        lines += ["## Regression checks", ""]
        for cond, rep in regression_by_condition.items():
            status = "OK" if rep.get("ok") else "REGRESSION"
            lines.append(f"### `{cond}` — {status}")
            for c in rep.get("checks", []):
                mark = {"ok": "✓", "warn": "⚠", "fail": "✗"}.get(c["level"], "?")
                lines.append(f"- {mark} **{c['name']}**: {c['detail']}")
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
