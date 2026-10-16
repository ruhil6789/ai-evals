"""
Continuous evaluation gate for lyrics → composer.

Fails (exit 1) if latest metrics drop below baselines/lyrics_composer_baseline.json.

Usage (CI):
  cd evals
  python3 run_lyrics_eval.py
  python3 ci_check_lyrics.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASELINE = ROOT / "baselines" / "lyrics_composer_baseline.json"
LATEST = ROOT / "reports" / "lyrics_composer_latest_metrics.json"


def main() -> int:
    if not BASELINE.exists():
        print(f"No baseline at {BASELINE}")
        print("Run: python3 run_lyrics_eval.py --write-baseline")
        return 1
    if not LATEST.exists():
        print(f"No latest metrics at {LATEST}")
        print("Run: python3 run_lyrics_eval.py")
        return 1

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    latest = json.loads(LATEST.read_text(encoding="utf-8"))

    exact = latest["exact_match_pass_rate"]
    top3 = latest["top3_pass_rate"]
    min_exact = baseline["min_exact_match_pass_rate"]
    min_top3 = baseline["min_top3_pass_rate"]

    print("CE check — lyrics → composer")
    print(f"  exact: {exact:.4f}  (floor {min_exact:.4f})")
    print(f"  top3:  {top3:.4f}  (floor {min_top3:.4f})")

    ok = True
    if exact < min_exact:
        print("REGRESSION: exact match below baseline floor")
        ok = False
    if top3 < min_top3:
        print("REGRESSION: top-3 below baseline floor")
        ok = False

    if ok:
        print("PASS: no regression vs baseline")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
