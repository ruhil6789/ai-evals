"""Tests for dataset loading, hashing, and sample IDs."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dataset import hash_dataset, load_jsonl, save_jsonl, validate_items  # noqa: E402


class TestDataset(unittest.TestCase):
    def test_load_tickets_has_items(self):
        rows = load_jsonl(ROOT / "data" / "tickets.jsonl")
        self.assertGreaterEqual(len(rows), 3)
        self.assertIn("ticket_text", rows[0])
        self.assertTrue(rows[0]["sample_id"].startswith("row_"))

    def test_guardrail_dev_stable_ids(self):
        rows = load_jsonl(ROOT / "data" / "guardrail_eval" / "development.jsonl")
        ids = [r["sample_id"] for r in rows]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("indirect_001", ids)

    def test_hash_stable(self):
        path = ROOT / "data" / "tickets.jsonl"
        self.assertEqual(hash_dataset(path), hash_dataset(path))

    def test_save_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "t.jsonl"
            save_jsonl(p, [{"sample_id": "a", "x": "1"}])
            rows = load_jsonl(p)
            self.assertEqual(rows[0]["sample_id"], "a")

    def test_validate_items(self):
        schema = {
            "properties": {"sample_id": {"type": "string"}, "user_query": {"type": "string"}},
            "required": ["sample_id", "user_query"],
        }
        bad = validate_items([{"sample_id": "x"}], schema)
        self.assertEqual(len(bad), 1)


if __name__ == "__main__":
    unittest.main()
