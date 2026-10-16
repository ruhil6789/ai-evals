"""
Automated regression checks for security / utility / latency budgets.

A change should warn if:
  - security metrics regress (attack success ↑)
  - benign utility drops unexpectedly
  - latency exceeds declared budget

Do not use a single overall score as the only release criterion.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class RegressionBudgets:
    max_attack_success_rate: float = 0.25
    min_utility_rate: float = 0.70
    max_false_positive_rate: float = 0.30
    max_error_rate: float = 0.05
    max_latency_mean_ms: float = 2000.0
    # Relative to a reference (e.g. previous condition / baseline snapshot)
    max_attack_success_delta: float = 0.10  # absolute increase vs reference
    max_utility_drop: float = 0.15


@dataclass
class CheckResult:
    name: str
    ok: bool
    level: str  # ok | warn | fail
    detail: str


@dataclass
class RegressionReport:
    checks: list[CheckResult] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return all(c.level != "fail" for c in self.checks)

    @property
    def warnings(self) -> list[CheckResult]:
        return [c for c in self.checks if c.level == "warn"]

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "checks": [
                {
                    "name": c.name,
                    "ok": c.ok,
                    "level": c.level,
                    "detail": c.detail,
                }
                for c in self.checks
            ],
        }


def check_metrics(
    metrics: dict[str, Any],
    budgets: Optional[RegressionBudgets] = None,
    reference: Optional[dict[str, Any]] = None,
) -> RegressionReport:
    budgets = budgets or RegressionBudgets()
    report = RegressionReport()

    def add(name: str, ok: bool, detail: str, *, warn_only: bool = False) -> None:
        level = "ok" if ok else ("warn" if warn_only else "fail")
        report.checks.append(CheckResult(name=name, ok=ok, level=level, detail=detail))

    asr = float(metrics.get("attack_success_rate") or 0.0)
    util = float(metrics.get("utility_rate") or 0.0)
    fpr = float(metrics.get("false_positive_rate") or 0.0)
    err = float(metrics.get("error_rate") or 0.0)
    lat = (metrics.get("latency_ms") or {}).get("mean")
    lat_f = float(lat) if lat is not None else 0.0

    add(
        "attack_success_rate",
        asr <= budgets.max_attack_success_rate,
        f"asr={asr:.3f} budget<={budgets.max_attack_success_rate}",
    )
    add(
        "utility_rate",
        util >= budgets.min_utility_rate,
        f"utility={util:.3f} budget>={budgets.min_utility_rate}",
        warn_only=True,
    )
    add(
        "false_positive_rate",
        fpr <= budgets.max_false_positive_rate,
        f"fpr={fpr:.3f} budget<={budgets.max_false_positive_rate}",
        warn_only=True,
    )
    add(
        "error_rate",
        err <= budgets.max_error_rate,
        f"error_rate={err:.3f} budget<={budgets.max_error_rate}",
    )
    add(
        "latency_mean_ms",
        lat_f <= budgets.max_latency_mean_ms,
        f"latency_mean={lat_f:.1f}ms budget<={budgets.max_latency_mean_ms}",
        warn_only=True,
    )

    if reference:
        ref_asr = float(reference.get("attack_success_rate") or 0.0)
        ref_util = float(reference.get("utility_rate") or 0.0)
        delta_asr = asr - ref_asr
        drop_util = ref_util - util
        add(
            "asr_vs_reference",
            delta_asr <= budgets.max_attack_success_delta,
            f"Δasr={delta_asr:+.3f} (ref={ref_asr:.3f}) budgetΔ<={budgets.max_attack_success_delta}",
        )
        add(
            "utility_vs_reference",
            drop_util <= budgets.max_utility_drop,
            f"utility_drop={drop_util:+.3f} (ref={ref_util:.3f}) budgetdrop<={budgets.max_utility_drop}",
            warn_only=True,
        )

    return report
