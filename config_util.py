"""Capture experiment configuration for reproducibility."""

from __future__ import annotations

import os
import random
import subprocess
from pathlib import Path
from typing import Any, Optional

from core import ExperimentConfig
from dataset import hash_dataset, hash_file

GRADER_VERSION = "evals-graders-v1.1"


def git_commit(repo: Path | None = None) -> Optional[str]:
    root = repo or Path(__file__).resolve().parent
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=root,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return out or None
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None


def freeze_seed(seed: int) -> None:
    """Freeze RNGs for components that support it."""
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import numpy as np  # type: ignore

        np.random.seed(seed)
    except ImportError:
        pass


def build_experiment_config(
    *,
    condition: str,
    model_version: str,
    dataset_version: str,
    dataset_path: str | Path,
    prompt_version: str,
    prompt_template: list,
    guardrail_config_path: str | Path | None = None,
    temperature: float | None = None,
    generation_settings: dict | None = None,
    seed: int | None = 42,
    trial: int = 1,
    notes: str = "",
    extra: dict | None = None,
) -> ExperimentConfig:
    if seed is not None:
        freeze_seed(seed)
    gpath = str(guardrail_config_path) if guardrail_config_path else None
    return ExperimentConfig(
        condition=condition,
        model_version=model_version,
        dataset_version=dataset_version,
        dataset_path=str(dataset_path),
        dataset_hash=hash_dataset(dataset_path),
        prompt_version=prompt_version,
        prompt_template=prompt_template,
        grader_version=GRADER_VERSION,
        guardrail_config_path=gpath,
        guardrail_config_hash=hash_file(gpath) if gpath else None,
        temperature=temperature,
        generation_settings=generation_settings or {},
        seed=seed,
        software_commit=git_commit(),
        trial=trial,
        notes=notes,
        extra=extra or {},
    )


def config_to_jsonable(cfg: ExperimentConfig) -> dict[str, Any]:
    return cfg.to_dict()
