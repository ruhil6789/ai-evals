"""
Dataset loading — JSONL in the OpenAI evals shape:

  { "item": { "sample_id": "...", ... } }

Also: stable IDs, schema validation, content hashing for reproducibility.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterator, Optional


def load_jsonl(path: str | Path, *, ensure_sample_id: bool = True) -> list[dict]:
    path = Path(path)
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            item = obj["item"] if "item" in obj else obj
            if ensure_sample_id and "sample_id" not in item:
                item = {**item, "sample_id": f"row_{i:04d}"}
            rows.append(item)
    return rows


def iter_jsonl(path: str | Path) -> Iterator[dict]:
    for item in load_jsonl(path):
        yield item


def save_jsonl(path: str | Path, items: list[dict]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps({"item": item}, ensure_ascii=False) + "\n")


def hash_dataset(path: str | Path) -> str:
    """SHA256 of file bytes — version pin for experiment config."""
    data = Path(path).read_bytes()
    return hashlib.sha256(data).hexdigest()[:16]


def hash_file(path: str | Path) -> Optional[str]:
    p = Path(path)
    if not p.is_file():
        return None
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def validate_items(items: list[dict], schema: dict) -> list[tuple[str, list[str]]]:
    """Return [(sample_id, errors), ...] for invalid rows."""
    from core import DataSourceConfig

    cfg = DataSourceConfig(item_schema=schema)
    bad = []
    for item in items:
        errs = cfg.validate_item(item)
        if errs:
            bad.append((str(item.get("sample_id", "?")), errs))
    return bad
