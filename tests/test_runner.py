"""Tests for runner — pass/fail/error separation and sample records."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core import DataSourceConfig, SampleOutcome  # noqa: E402
from graders import StringCheckGrader  # noqa: E402
from registry import EvalRegistry  # noqa: E402
from runner import Runner  # noqa: E402


class TestRunner(unittest.TestCase):
    def test_pass_fail_error(self):
        with tempfile.TemporaryDirectory() as td:
            data = Path(td) / "data.jsonl"
            data.write_text(
                "\n".join(
                    [
                        json.dumps(
                            {
                                "item": {
                                    "sample_id": "ok",
                                    "ticket_text": "monitor broken",
                                    "correct_label": "Hardware",
                                }
                            }
                        ),
                        json.dumps(
                            {
                                "item": {
                                    "sample_id": "bad",
                                    "ticket_text": "monitor broken",
                                    "correct_label": "Software",
                                }
                            }
                        ),
                        json.dumps({"item": {"sample_id": "miss"}}),
                    ]
                ),
                encoding="utf-8",
            )
            reports = Path(td) / "reports"
            registry = EvalRegistry(root=Path(td) / "reg")
            eval_obj = registry.create(
                name="t",
                data_source_config=DataSourceConfig(
                    item_schema={
                        "properties": {
                            "sample_id": {"type": "string"},
                            "ticket_text": {"type": "string"},
                            "correct_label": {"type": "string"},
                        },
                        "required": ["sample_id", "ticket_text", "correct_label"],
                    }
                ),
                testing_criteria=[StringCheckGrader(name="eq")],
            )

            def model_fn(messages):
                return "Hardware", {"prompt_tokens": 1, "completion_tokens": 1}

            runner = Runner(reports_dir=reports)
            run = runner.create_run(
                eval_obj,
                name="unit",
                model_name="stub",
                model_fn=model_fn,
                prompt_template=[{"role": "user", "content": "{{ item.ticket_text }}"}],
                data_path=data,
                condition="unit_test",
                dataset_version="test_v1",
            )
            outcomes = {s.sample_id: s.outcome for s in run.samples}
            self.assertEqual(outcomes["ok"], SampleOutcome.PASS)
            self.assertEqual(outcomes["bad"], SampleOutcome.FAIL)
            self.assertEqual(outcomes["miss"], SampleOutcome.ERROR)
            rc = run.result_counts
            self.assertEqual(rc["passed"], 1)
            self.assertEqual(rc["failed"], 1)
            self.assertEqual(rc["errored"], 1)

            # Per-sample JSONL written
            lines = (reports / "run_results.jsonl").read_text(encoding="utf-8").strip().splitlines()
            self.assertEqual(len(lines), 3)
            rec = json.loads(lines[0])
            self.assertIn("latency_ms", rec)
            self.assertIn("grader_results", rec)
            self.assertEqual(rec["condition"], "unit_test")


if __name__ == "__main__":
    unittest.main()
