#!/usr/bin/env python3
"""
Structured lab runner — one entry point for:
  1) Product evals (gold + train/load + graders + CE)
  2) Gradio neuron explorer
  3) Neuron ablation + re-eval

Usage:
  cd evals
  python3 run_lab.py                  # interactive menu
  python3 run_lab.py status
  python3 run_lab.py setup
  python3 run_lab.py eval
  python3 run_lab.py eval --write-baseline
  python3 run_lab.py explore
  python3 run_lab.py ablate --neuron 5
  python3 run_lab.py ablate --neuron 5,12 --save
  python3 run_lab.py all --neuron 5   # setup → eval → ablate (no Gradio)
  python3 run_lab.py workflow         # print the recommended order
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY = sys.executable

GOLD = ROOT / "data" / "lyrics_composer_gold.jsonl"
META = ROOT / "data" / "lyrics_composer_meta.json"
CKPT = ROOT / "artifacts" / "composer_model.pt"
BASELINE = ROOT / "baselines" / "lyrics_composer_baseline.json"
LATEST = ROOT / "reports" / "lyrics_composer_latest_metrics.json"


def run(script: str, *args: str) -> int:
    cmd = [PY, str(ROOT / script), *args]
    print("\n→", " ".join(cmd), flush=True)
    return subprocess.call(cmd, cwd=str(ROOT))


def cmd_status(_: argparse.Namespace) -> int:
    print("=" * 60)
    print("Lab status (evals/)")
    print("=" * 60)
    checks = [
        ("Gold JSONL", GOLD),
        ("Gold meta", META),
        ("Model checkpoint", CKPT),
        ("CE baseline", BASELINE),
        ("Latest metrics", LATEST),
    ]
    for name, path in checks:
        mark = "OK " if path.exists() else "MISSING"
        print(f"  [{mark}] {name}: {path.relative_to(ROOT)}")
    if LATEST.exists():
        m = json.loads(LATEST.read_text(encoding="utf-8"))
        print(
            f"\n  Latest exact={m.get('exact_match_pass_rate', 0):.4f}  "
            f"top3={m.get('top3_pass_rate', 0):.4f}"
        )
    print()
    return 0


def cmd_workflow(_: argparse.Namespace) -> int:
    print(
        """
Recommended structured workflow
================================

  [1] SETUP     Freeze gold split + ensure model exists
                python3 run_lab.py setup

  [2] EVAL      Product eval (exact + top-3) on frozen TEST
                python3 run_lab.py eval
                python3 run_lab.py eval --write-baseline   # first time / CE floors
                python3 run_lab.py ce                      # regression gate

  [3] EXPLORE   Gradio UI — inspect +/− words per neuron
                python3 run_lab.py explore
                # open http://127.0.0.1:7860

  [4] ABLATE    Zero neuron(s) at inference → compare metrics
                python3 run_lab.py ablate --neuron 5
                python3 run_lab.py ablate --neuron 5,12 --save

  [5] LOOP      After ablation, re-check CE if you care about floors
                python3 run_lab.py ce

One-shot (no UI):
  python3 run_lab.py all --neuron 5
"""
    )
    return 0


def cmd_setup(_: argparse.Namespace) -> int:
    print("=== [1/2] Build / ensure gold ===")
    rc = run("build_lyrics_gold.py")
    if rc != 0:
        return rc
    if CKPT.exists():
        print(f"=== [2/2] Checkpoint already present: {CKPT} ===")
        return 0
    print("=== [2/2] Train checkpoint via eval runner ===")
    return run("run_lyrics_eval.py")


def cmd_eval(args: argparse.Namespace) -> int:
    extra = []
    if args.write_baseline:
        extra.append("--write-baseline")
    if args.retrain:
        extra.append("--retrain")
    if args.rebuild_gold:
        extra.append("--rebuild-gold")
    return run("run_lyrics_eval.py", *extra)


def cmd_ce(_: argparse.Namespace) -> int:
    return run("ci_check_lyrics.py")


def cmd_explore(args: argparse.Namespace) -> int:
    extra = []
    if args.port:
        extra.extend(["--port", str(args.port)])
    if args.share:
        extra.append("--share")
    print("Starting Gradio neuron explorer …")
    print("Open http://127.0.0.1:%s" % (args.port or 7860))
    return run("neuron_explorer.py", *extra)


def cmd_ablate(args: argparse.Namespace) -> int:
    if not args.neuron:
        print("ERROR: --neuron is required (e.g. --neuron 5 or --neuron 5,12)")
        return 2
    extra = ["--neuron", args.neuron]
    if args.save:
        extra.append("--save")
    if args.skip_baseline:
        extra.append("--skip-baseline")
    return run("ablate_and_eval.py", *extra)


def cmd_inspect(args: argparse.Namespace) -> int:
    n = args.neuron or "0"
    return run("inspect_neurons.py", "--neuron", n, "--top", str(args.top or 20))


def cmd_all(args: argparse.Namespace) -> int:
    """setup → eval → ablate (Gradio is interactive; skip unless --explore)."""
    steps = [
        ("setup", lambda: cmd_setup(args)),
        ("eval", lambda: cmd_eval(args)),
        ("ce", lambda: cmd_ce(args)),
    ]
    if args.neuron:
        steps.append(("ablate", lambda: cmd_ablate(args)))
    if args.explore:
        steps.append(("explore", lambda: cmd_explore(args)))

    for name, fn in steps:
        print(f"\n######## STAGE: {name} ########")
        rc = fn()
        if rc != 0:
            print(f"STAGE {name} failed with code {rc}")
            return rc
    print("\nAll requested stages finished OK.")
    return 0


def interactive_menu() -> int:
    cmd_status(argparse.Namespace())
    print(
        """
Menu
----
  1) workflow   — print recommended order
  2) setup      — gold + model
  3) eval       — product eval
  4) ce         — CI regression check
  5) explore    — Gradio neuron UI
  6) inspect    — terminal Method 1 words
  7) ablate     — ablate neuron(s) + re-eval
  8) all        — setup → eval → ce → ablate
  0) quit
"""
    )
    choice = input("Choose [0-8]: ").strip()
    ns = argparse.Namespace(
        write_baseline=False,
        retrain=False,
        rebuild_gold=False,
        neuron=None,
        save=False,
        skip_baseline=False,
        port=7860,
        share=False,
        top=20,
        explore=False,
    )
    if choice == "1":
        return cmd_workflow(ns)
    if choice == "2":
        return cmd_setup(ns)
    if choice == "3":
        wb = input("Write CE baseline? [y/N]: ").strip().lower() == "y"
        ns.write_baseline = wb
        return cmd_eval(ns)
    if choice == "4":
        return cmd_ce(ns)
    if choice == "5":
        return cmd_explore(ns)
    if choice == "6":
        ns.neuron = input("Neuron index [0]: ").strip() or "0"
        return cmd_inspect(ns)
    if choice == "7":
        ns.neuron = input("Neuron(s) e.g. 5 or 5,12: ").strip()
        ns.save = input("Save ablated checkpoint? [y/N]: ").strip().lower() == "y"
        return cmd_ablate(ns)
    if choice == "8":
        ns.neuron = input("Neuron(s) for ablation (blank to skip ablate): ").strip() or None
        ns.write_baseline = False
        return cmd_all(ns)
    if choice == "0":
        return 0
    print("Unknown choice")
    return 2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Structured runner for lyrics evals / Gradio / ablation"
    )
    sub = p.add_subparsers(dest="command")

    sub.add_parser("status", help="Show which artifacts exist")
    sub.add_parser("workflow", help="Print recommended order")
    sub.add_parser("setup", help="Build gold + ensure checkpoint")

    pe = sub.add_parser("eval", help="Run product eval")
    pe.add_argument("--write-baseline", action="store_true")
    pe.add_argument("--retrain", action="store_true")
    pe.add_argument("--rebuild-gold", action="store_true")

    sub.add_parser("ce", help="Run CI regression check")

    px = sub.add_parser("explore", help="Launch Gradio neuron explorer")
    px.add_argument("--port", type=int, default=7860)
    px.add_argument("--share", action="store_true")

    pi = sub.add_parser("inspect", help="Terminal top +/− words for a neuron")
    pi.add_argument("--neuron", type=str, default="0")
    pi.add_argument("--top", type=int, default=20)

    pa = sub.add_parser("ablate", help="Ablate neuron(s) and compare eval")
    pa.add_argument("--neuron", type=str, required=True)
    pa.add_argument("--save", action="store_true")
    pa.add_argument("--skip-baseline", action="store_true")

    pall = sub.add_parser("all", help="setup → eval → ce → optional ablate")
    pall.add_argument("--neuron", type=str, default=None)
    pall.add_argument("--write-baseline", action="store_true")
    pall.add_argument("--retrain", action="store_true")
    pall.add_argument("--rebuild-gold", action="store_true")
    pall.add_argument("--save", action="store_true")
    pall.add_argument("--skip-baseline", action="store_true")
    pall.add_argument("--explore", action="store_true", help="Also launch Gradio at end")
    pall.add_argument("--port", type=int, default=7860)
    pall.add_argument("--share", action="store_true")

    return p


def main(argv: list | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        return interactive_menu()

    dispatch = {
        "status": cmd_status,
        "workflow": cmd_workflow,
        "setup": cmd_setup,
        "eval": cmd_eval,
        "ce": cmd_ce,
        "explore": cmd_explore,
        "inspect": cmd_inspect,
        "ablate": cmd_ablate,
        "all": cmd_all,
    }
    return dispatch[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
