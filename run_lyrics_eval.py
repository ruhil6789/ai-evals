"""
Product eval for: map lyrics → one of 10 composers.

Pipeline:
  1. Define task (EvalSpec + graders: exact match, top-3)
  2. Gold dataset (frozen JSONL split) — build if missing
  3. Ensure checkpoint (train if missing)
  4. Run eval on frozen TEST split
  5. Analyze pass rates + write failure report
  6. Emit metrics JSON for CE / CI

Usage:
  cd evals
  python3 run_lyrics_eval.py
  python3 run_lyrics_eval.py --retrain
  python3 run_lyrics_eval.py --write-baseline
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from analyze import summarize
from core import DataSourceConfig
from graders import JsonPredEqualsGrader, JsonTopKGrader
from lyrics_lib import (
    BASELINE_JSON,
    CKPT_PATH,
    GOLD_JSONL,
    META_JSON,
    ROOT,
    build_gold_dataset,
    load_checkpoint,
    load_gold_split,
    predict_json,
    train_and_save,
)
from registry import EvalRegistry
from runner import Runner

REPORTS = ROOT / "reports"


def ensure_gold() -> dict:
    if GOLD_JSONL.exists() and META_JSON.exists():
        return json.loads(META_JSON.read_text(encoding="utf-8"))
    print("Gold missing — freezing split from lyrics.csv …")
    return build_gold_dataset()


def ensure_checkpoint(retrain: bool = False) -> None:
    if CKPT_PATH.exists() and not retrain:
        print(f"Using existing checkpoint: {CKPT_PATH}")
        return
    print("Training model on frozen train split …")
    train_and_save()


def create_composer_eval(registry: EvalRegistry):
    return registry.create(
        name="Lyrics → Composer (top-10)",
        data_source_config=DataSourceConfig(
            type="custom",
            item_schema={
                "type": "object",
                "properties": {
                    "lyrics": {"type": "string"},
                    "correct_label": {"type": "string"},
                    "label": {"type": "integer"},
                    "split": {"type": "string"},
                },
                "required": ["lyrics", "correct_label"],
            },
            include_sample_schema=True,
        ),
        testing_criteria=[
            JsonPredEqualsGrader(name="Exact match (pred == gold composer)"),
            JsonTopKGrader(name="Top-3 contains gold composer", k=3),
        ],
        metadata={
            "task": "map lyrics → one of 10 composers",
            "domain": "lyrics",
            "refusal": "not_applicable",
        },
    )


def make_model_fn(model, vocab, id2label):
    def _fn(messages):
        # Runner templates user content as lyrics text
        lyrics = ""
        for m in messages:
            if m.get("role") == "user":
                lyrics = m.get("content", "")
        out = predict_json(model, vocab, id2label, lyrics, k=3)
        usage = {
            "prompt_tokens": max(1, len(lyrics.split())),
            "completion_tokens": 3,
        }
        return out, usage

    return _fn


def write_failures(run, path: Path, limit: int = 40) -> None:
    lines = ["# Lyrics composer eval — failures", ""]
    n = 0
    for i, s in enumerate(run.samples, 1):
        if s.passed:
            continue
        n += 1
        if n > limit:
            break
        lines.append(f"## Fail #{n} (sample {i})")
        lines.append(f"- gold: `{s.item.get('correct_label')}`")
        lines.append(f"- output: `{s.output_text}`")
        lines.append(f"- title: `{s.item.get('title', '')[:80]}`")
        for g in s.grades:
            mark = "PASS" if g.passed else "FAIL"
            lines.append(f"- [{mark}] {g.grader_name}: {g.detail}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def metrics_from_run(run) -> dict:
    rc = run.result_counts
    by_name = {}
    for row in run.per_testing_criteria_results():
        # testing_criteria is "Name-id"
        name = row["testing_criteria"].rsplit("-", 1)[0]
        total = row["passed"] + row["failed"]
        by_name[name] = {
            "passed": row["passed"],
            "failed": row["failed"],
            "pass_rate": (row["passed"] / total) if total else 0.0,
        }
    exact = by_name.get("Exact match (pred == gold composer)", {})
    top3 = by_name.get("Top-3 contains gold composer", {})
    return {
        "task": "map lyrics → one of 10 composers",
        "n_test": rc["total"],
        "exact_match_pass_rate": exact.get("pass_rate", 0.0),
        "top3_pass_rate": top3.get("pass_rate", 0.0),
        "result_counts": rc,
        "per_criteria": by_name,
        "run_id": run.id,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run lyrics→composer product eval")
    parser.add_argument("--retrain", action="store_true", help="Force retrain checkpoint")
    parser.add_argument(
        "--write-baseline",
        action="store_true",
        help="Write current metrics as CE baseline",
    )
    parser.add_argument("--rebuild-gold", action="store_true", help="Rebuild frozen gold")
    args = parser.parse_args()

    if args.rebuild_gold or not GOLD_JSONL.exists():
        ensure_gold() if not args.rebuild_gold else build_gold_dataset()
    else:
        ensure_gold()

    ensure_checkpoint(retrain=args.retrain)
    model, vocab, id2label, _ckpt = load_checkpoint()

    # Materialize test-only JSONL for Runner (schema-compatible)
    test_items = load_gold_split("test")
    test_jsonl = ROOT / "data" / "lyrics_composer_test_only.jsonl"
    with test_jsonl.open("w", encoding="utf-8") as f:
        for it in test_items:
            f.write(json.dumps({"item": it}, ensure_ascii=False) + "\n")

    registry = EvalRegistry()
    runner = Runner(reports_dir=REPORTS)
    eval_obj = create_composer_eval(registry)

    prompt_template = [
        {
            "role": "developer",
            "content": "Predict the Bollywood song composer. Reply with JSON pred/top3.",
        },
        {"role": "user", "content": "{{ item.lyrics }}"},
    ]

    print("\n=== Running eval on frozen TEST split ===")
    run = runner.create_run(
        eval_obj,
        name="lyrics-composer-test",
        model_name="ComposerClassifier-bow",
        model_fn=make_model_fn(model, vocab, id2label),
        prompt_template=prompt_template,
        data_path=test_jsonl,
        metadata={"checkpoint": str(CKPT_PATH), "gold": str(GOLD_JSONL)},
    )

    print(summarize(run))
    metrics = metrics_from_run(run)
    metrics_path = REPORTS / f"{run.id}_metrics.json"
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    fail_path = REPORTS / f"{run.id}_failures.md"
    write_failures(run, fail_path)

    # Also keep a stable latest pointer for CI
    latest = REPORTS / "lyrics_composer_latest_metrics.json"
    latest.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("\n=== Analyze ===")
    print(f"exact_match_pass_rate: {metrics['exact_match_pass_rate']:.4f}")
    print(f"top3_pass_rate:        {metrics['top3_pass_rate']:.4f}")
    print(f"metrics:  {metrics_path}")
    print(f"failures: {fail_path}")
    print(f"report:   {run.metadata.get('report_path')}")

    if args.write_baseline:
        BASELINE_JSON.parent.mkdir(parents=True, exist_ok=True)
        baseline = {
            "min_exact_match_pass_rate": round(metrics["exact_match_pass_rate"] * 0.90, 4),
            "min_top3_pass_rate": round(metrics["top3_pass_rate"] * 0.90, 4),
            "recorded_exact": metrics["exact_match_pass_rate"],
            "recorded_top3": metrics["top3_pass_rate"],
            "note": "CE floors at 90% of recorded rates to allow small noise",
        }
        BASELINE_JSON.write_text(json.dumps(baseline, indent=2), encoding="utf-8")
        print(f"baseline written → {BASELINE_JSON}")


if __name__ == "__main__":
    main()
