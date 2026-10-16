"""
Option A — Ablate hidden neuron(s) at inference, then re-run composer eval.

Compares exact-match / top-3 on the frozen TEST gold set:
  baseline (full model) vs ablated model.

Does NOT modify lyrics.csv. Does NOT touch CBRN data.
Optional --save writes a new checkpoint with weights zeroed for those neurons.

Usage:
  cd evals
  python3 ablate_and_eval.py --neuron 5
  python3 ablate_and_eval.py --neuron 5,12,40
  python3 ablate_and_eval.py --neuron 5 --save
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from analyze import summarize
from core import DataSourceConfig
from graders import JsonPredEqualsGrader, JsonTopKGrader
from lyrics_lib import (
    CKPT_PATH,
    GOLD_JSONL,
    ROOT,
    build_gold_dataset,
    load_checkpoint,
    load_gold_split,
    make_ablated_model,
    predict_json,
    zero_neuron_weights,
)
from registry import EvalRegistry
from runner import Runner

REPORTS = ROOT / "reports"
ABLATED_CKPT = ROOT / "artifacts" / "composer_model_ablated.pt"


def ensure_gold() -> None:
    if not GOLD_JSONL.exists():
        print("Gold missing — building …")
        build_gold_dataset()


def create_eval(registry: EvalRegistry):
    return registry.create(
        name="Lyrics → Composer (ablation compare)",
        data_source_config=DataSourceConfig(
            type="custom",
            item_schema={
                "type": "object",
                "properties": {
                    "lyrics": {"type": "string"},
                    "correct_label": {"type": "string"},
                },
                "required": ["lyrics", "correct_label"],
            },
        ),
        testing_criteria=[
            JsonPredEqualsGrader(name="Exact match (pred == gold composer)"),
            JsonTopKGrader(name="Top-3 contains gold composer", k=3),
        ],
        metadata={"experiment": "neuron_ablation"},
    )


def make_fn(model, vocab, id2label):
    def _fn(messages):
        lyrics = ""
        for m in messages:
            if m.get("role") == "user":
                lyrics = m.get("content", "")
        out = predict_json(model, vocab, id2label, lyrics, k=3)
        return out, {"prompt_tokens": max(1, len(lyrics.split())), "completion_tokens": 3}

    return _fn


def metrics_from_run(run) -> dict:
    by_name = {}
    for row in run.per_testing_criteria_results():
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
        "exact_match_pass_rate": exact.get("pass_rate", 0.0),
        "top3_pass_rate": top3.get("pass_rate", 0.0),
        "result_counts": run.result_counts,
        "run_id": run.id,
        "per_criteria": by_name,
    }


def run_eval(model, vocab, id2label, name: str, test_jsonl: Path, runner: Runner, eval_obj):
    prompt_template = [
        {"role": "developer", "content": "Predict composer as JSON pred/top3."},
        {"role": "user", "content": "{{ item.lyrics }}"},
    ]
    run = runner.create_run(
        eval_obj,
        name=name,
        model_name=name,
        model_fn=make_fn(model, vocab, id2label),
        prompt_template=prompt_template,
        data_path=test_jsonl,
    )
    return run, metrics_from_run(run)


def parse_neurons(s: str):
    parts = [p.strip() for p in s.split(",") if p.strip() != ""]
    return [int(p) for p in parts]


def main() -> None:
    parser = argparse.ArgumentParser(description="Ablate neuron(s) and compare eval metrics")
    parser.add_argument(
        "--neuron",
        type=str,
        required=True,
        help="Neuron index or comma list, e.g. 5 or 5,12,40",
    )
    parser.add_argument("--ckpt", type=str, default=str(CKPT_PATH))
    parser.add_argument(
        "--save",
        action="store_true",
        help="Also zero weights permanently and save composer_model_ablated.pt",
    )
    parser.add_argument(
        "--skip-baseline",
        action="store_true",
        help="Skip full-model eval (only run ablated)",
    )
    args = parser.parse_args()

    neurons = parse_neurons(args.neuron)
    ensure_gold()

    model, vocab, id2label, ckpt = load_checkpoint(Path(args.ckpt))
    hidden = model.net[0].weight.shape[0]
    for i in neurons:
        if not (0 <= i < hidden):
            raise SystemExit(f"neuron {i} out of range 0..{hidden - 1}")

    test_items = load_gold_split("test")
    test_jsonl = ROOT / "data" / "lyrics_composer_test_only.jsonl"
    with test_jsonl.open("w", encoding="utf-8") as f:
        for it in test_items:
            f.write(json.dumps({"item": it}, ensure_ascii=False) + "\n")

    registry = EvalRegistry()
    runner = Runner(reports_dir=REPORTS)
    eval_obj = create_eval(registry)

    print(f"Ablating neuron(s) at inference: {neurons}")
    print(f"Test set size: {len(test_items)}")

    baseline_metrics = None
    if not args.skip_baseline:
        print("\n=== BASELINE (full model) ===")
        _run_b, baseline_metrics = run_eval(
            model, vocab, id2label, "baseline-full", test_jsonl, runner, eval_obj
        )
        print(
            f"exact={baseline_metrics['exact_match_pass_rate']:.4f}  "
            f"top3={baseline_metrics['top3_pass_rate']:.4f}"
        )

    ablated = make_ablated_model(model, neurons)
    print("\n=== ABLATED (post-ReLU units zeroed) ===")
    run_a, ablated_metrics = run_eval(
        ablated,
        vocab,
        id2label,
        f"ablated-{'-'.join(map(str, neurons))}",
        test_jsonl,
        runner,
        eval_obj,
    )
    print(
        f"exact={ablated_metrics['exact_match_pass_rate']:.4f}  "
        f"top3={ablated_metrics['top3_pass_rate']:.4f}"
    )

    report = {
        "neurons_ablated": neurons,
        "mode": "inference_zero_hidden",
        "baseline": baseline_metrics,
        "ablated": ablated_metrics,
    }
    if baseline_metrics:
        report["delta"] = {
            "exact_match_pass_rate": ablated_metrics["exact_match_pass_rate"]
            - baseline_metrics["exact_match_pass_rate"],
            "top3_pass_rate": ablated_metrics["top3_pass_rate"]
            - baseline_metrics["top3_pass_rate"],
        }
        print("\n=== DELTA (ablated − baseline) ===")
        print(f"exact Δ = {report['delta']['exact_match_pass_rate']:+.4f}")
        print(f"top3  Δ = {report['delta']['top3_pass_rate']:+.4f}")

    out_path = REPORTS / f"ablation_neurons_{'_'.join(map(str, neurons))}.json"
    REPORTS.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nWrote {out_path}")

    if args.save:
        # Permanent weight zero on a fresh copy
        model2, vocab2, id2label2, ckpt2 = load_checkpoint(Path(args.ckpt))
        for i in neurons:
            zero_neuron_weights(model2, i)
        ckpt2 = dict(ckpt2)
        ckpt2["model"] = model2.state_dict()
        ckpt2["ablated_neurons"] = neurons
        ABLATED_CKPT.parent.mkdir(parents=True, exist_ok=True)
        import torch

        torch.save(ckpt2, ABLATED_CKPT)
        print(f"Saved weight-zeroed checkpoint → {ABLATED_CKPT}")
        print("Original checkpoint unchanged:", args.ckpt)

    print("\nTip: inspect the neuron first with:")
    print(f"  python3 inspect_neurons.py --neuron {neurons[0]}")
    print("  python3 neuron_explorer.py")


if __name__ == "__main__":
    main()
