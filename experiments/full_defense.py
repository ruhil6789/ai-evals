#!/usr/bin/env python3
"""Condition: full_defense — input + retrieval + output rails."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from experiments.common import run_condition  # noqa: E402


def main() -> None:
    split = sys.argv[1] if len(sys.argv) > 1 else "development"
    result = run_condition("full_defense", split=split)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
