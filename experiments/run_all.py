#!/usr/bin/env python3
"""
Run all defense conditions and write aggregate reports.

Usage:
  cd evals && python3 experiments/run_all.py
  cd evals && python3 experiments/run_all.py validation
  cd evals && python3 experiments/run_all.py heldout
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from experiments.common import persist_aggregate, run_condition  # noqa: E402

CONDITIONS = ("baseline", "input_defense", "retrieval_defense", "full_defense")


def main() -> None:
    split = sys.argv[1] if len(sys.argv) > 1 else "development"
    results = []
    for cond in CONDITIONS:
        print(f"\n=== Running {cond} on {split} ===")
        r = run_condition(cond, split=split)
        results.append(r)
        m = r["metrics"]
        print(
            f"  ASR={m['attack_success_rate']:.3f} "
            f"utility={m['utility_rate']:.3f} "
            f"FPR={m['false_positive_rate']:.3f} "
            f"errors={m['error_rate']:.3f} "
            f"regression_ok={r['regression']['ok']}"
        )
    summary, comparison = persist_aggregate(results)
    print("\nWrote:", summary)
    print("Wrote:", comparison)
    print(json.dumps({"runs": [{"condition": r["condition"], "run_id": r["run_id"]} for r in results]}, indent=2))


if __name__ == "__main__":
    main()
