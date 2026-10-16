"""
Freeze a gold train/val/test split for lyrics → composer evals.

Usage:
  cd evals && python3 build_lyrics_gold.py
"""

from __future__ import annotations

from lyrics_lib import GOLD_JSONL, META_JSON, build_gold_dataset


def main() -> None:
    meta = build_gold_dataset()
    print("Gold dataset frozen.")
    print(f"  path:   {GOLD_JSONL}")
    print(f"  meta:   {META_JSON}")
    print(f"  total:  {meta['n_total']}")
    print(f"  train:  {meta['n_train']}  val: {meta['n_val']}  test: {meta['n_test']}")
    print(f"  classes:{meta['composers']}")


if __name__ == "__main__":
    main()
