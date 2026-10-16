"""
Eval runner — create run, generate outputs, apply graders.

Supports:
  - classic model_fn + prompt_template (ticket demo)
  - replaceable SystemUnderTest (guardrail experiment conditions)

Persists:
  - reports/<run_id>.md / .json
  - reports/run_results.jsonl  (append per-sample records)
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Callable, Optional

from core import EvalRun, EvalSpec, ExperimentConfig, RunStatus, SampleResult
from dataset import load_jsonl
from prompt import render_messages


class Runner:
    def __init__(self, reports_dir: str | Path | None = None):
        self.reports_dir = Path(reports_dir or Path(__file__).parent / "reports")
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        self._runs: dict[str, EvalRun] = {}
        self.results_jsonl = self.reports_dir / "run_results.jsonl"

    def create_run(
        self,
        eval_spec: EvalSpec,
        *,
        name: str,
        model_name: str,
        model_fn: Callable,
        prompt_template: list[dict],
        data_path: str | Path,
        metadata: dict | None = None,
        config: ExperimentConfig | None = None,
        condition: str = "",
        dataset_version: str = "",
    ) -> EvalRun:
        """Classic path: render prompt → model_fn → grade."""

        def _call(item: dict) -> tuple[str, dict, float, Optional[str]]:
            t0 = time.perf_counter()
            try:
                messages = render_messages(prompt_template, item)
                output_text, usage = model_fn(messages)
                return output_text, usage or {}, (time.perf_counter() - t0) * 1000, None
            except Exception as e:  # noqa: BLE001
                return "", {}, (time.perf_counter() - t0) * 1000, str(e)

        return self._execute(
            eval_spec,
            name=name,
            model_name=model_name,
            data_path=data_path,
            call_fn=_call,
            prompt_template=prompt_template,
            metadata=metadata,
            config=config,
            condition=condition or (config.condition if config else ""),
            dataset_version=dataset_version
            or (config.dataset_version if config else ""),
        )

    def create_sut_run(
        self,
        eval_spec: EvalSpec,
        *,
        name: str,
        sut: Any,
        data_path: str | Path,
        config: ExperimentConfig,
        metadata: dict | None = None,
    ) -> EvalRun:
        """SUT path: sut.respond(item) → grade (replaceable defense stacks)."""

        def _call(item: dict) -> tuple[str, dict, float, Optional[str]]:
            resp = sut.respond(item)
            if resp.error:
                return "", resp.usage or {}, resp.latency_ms, resp.error
            return resp.output_text, resp.usage or {}, resp.latency_ms, None

        return self._execute(
            eval_spec,
            name=name,
            model_name=config.model_version,
            data_path=data_path,
            call_fn=_call,
            prompt_template=config.prompt_template,
            metadata={**(metadata or {}), "condition": config.condition, "sut": sut.name},
            config=config,
            condition=config.condition,
            dataset_version=config.dataset_version,
        )

    def _execute(
        self,
        eval_spec: EvalSpec,
        *,
        name: str,
        model_name: str,
        data_path: str | Path,
        call_fn: Callable,
        prompt_template: list,
        metadata: dict | None,
        config: ExperimentConfig | None,
        condition: str,
        dataset_version: str,
    ) -> EvalRun:
        run = EvalRun(
            eval_id=eval_spec.id,
            name=name,
            model=model_name,
            status=RunStatus.QUEUED,
            prompt_template=prompt_template,
            metadata=metadata or {},
            config=config,
        )
        self._runs[run.id] = run
        items = load_jsonl(data_path)
        run.status = RunStatus.RUNNING

        try:
            for item in items:
                errors = eval_spec.data_source_config.validate_item(item)
                if errors:
                    sample = SampleResult(
                        item=item,
                        output_text="",
                        error="; ".join(errors),
                        run_id=run.id,
                        condition=condition,
                        model_version=model_name,
                        dataset_version=dataset_version,
                    )
                    run.samples.append(sample)
                    self._append_sample_record(sample)
                    continue

                output_text, usage, latency_ms, err = call_fn(item)
                if err:
                    sample = SampleResult(
                        item=item,
                        output_text=output_text,
                        error=err,
                        usage=usage,
                        latency_ms=latency_ms,
                        run_id=run.id,
                        condition=condition,
                        model_version=model_name,
                        dataset_version=dataset_version,
                    )
                    run.samples.append(sample)
                    self._append_sample_record(sample)
                    continue

                grades = [g.grade(item, output_text) for g in eval_spec.testing_criteria]
                sample = SampleResult(
                    item=item,
                    output_text=output_text,
                    grades=grades,
                    usage=usage,
                    latency_ms=latency_ms,
                    run_id=run.id,
                    condition=condition,
                    model_version=model_name,
                    dataset_version=dataset_version,
                )
                run.samples.append(sample)
                self._append_sample_record(sample)

            run.status = RunStatus.COMPLETED
        except Exception as e:  # noqa: BLE001
            run.status = RunStatus.FAILED
            run.error = str(e)

        report_path = self.write_report(run, eval_spec)
        run.metadata["report_path"] = str(report_path)
        return run

    def _append_sample_record(self, sample: SampleResult) -> None:
        with self.results_jsonl.open("a", encoding="utf-8") as f:
            f.write(json.dumps(sample.to_record(), ensure_ascii=False) + "\n")

    def retrieve(self, run_id: str, eval_id: str | None = None) -> EvalRun:
        run = self._runs.get(run_id)
        if not run:
            raise KeyError(f"unknown run_id: {run_id}")
        if eval_id and run.eval_id != eval_id:
            raise KeyError("eval_id does not match run")
        return run

    def write_report(self, run: EvalRun, eval_spec: EvalSpec) -> Path:
        from analyze import write_markdown_report

        path = self.reports_dir / f"{run.id}.md"
        write_markdown_report(path, run, eval_spec)
        json_path = self.reports_dir / f"{run.id}.json"
        json_path.write_text(
            run.to_json(report_url=str(path.resolve())), encoding="utf-8"
        )
        return path
