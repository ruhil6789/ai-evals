# Evals Lab — Structured Evaluation for Nondeterministic Systems


> **Thesis.** Generative models are variable. Classical unit tests assume
> determinism. **Evals** are structured tests that still let you say:
> “for this task distribution, under this prompt/model, against these
> graders, performance is X — and it must not regress.”

```
Describe task as Eval  →  Run (prompt × data × model)  →  Analyze → iterate
        (BDD-like)              (samples + grades)         (report)
```

Companion lab: [`../guardrail/`](../guardrail/) enforces **continue / pause / stop**
at runtime. This lab **measures** whether behavior matches intent before and
after you change prompts, models, or rails.

---

## 1. Why evals exist

| Without evals | With evals |
|---------------|------------|
| “It seems to work” (vibe-based) | Task-scoped pass rates + failure cases |
| Surprise regressions on model upgrades | Comparable runs on a frozen dataset |
| Only academic metrics (BLEU/perplexity) | Graders tied to *your* product criteria |
| Safety claims without evidence | Measurable refusal / categorization / tool choice |

**Tips (best practices distilled):**

1. Adopt **eval-driven development** — write scoped tests early.  
2. Design **task-specific** evals on realistic traffic distributions.  
3. **Log everything** — mine production for hard cases.  
4. **Automate** scoring when you can; calibrate with humans.  
5. Evaluation is a **journey**, not a destination.  
6. Maintain **human↔auto agreement** before scaling LLM-as-judge.

**Anti-patterns:** overly generic metrics only; biased datasets; vibe evals;
ignoring human disagreement.

---

## 2. The three-step loop (matches the API guide)

### Step A — Create an eval for a task

An eval needs:

- **`data_source_config`** — schema for each test `item`
- **`testing_criteria`** — graders that decide pass/fail

Example task (from the docs): categorize IT tickets → `Hardware` | `Software` | `Other`.

### Step B — Test a prompt with your eval

Provide:

- JSONL dataset (`{"item": {...}}` per line)
- Prompt **template** with `{{ item.field }}`
- A **model** (stub offline, or live API)

### Step C — Analyze the results

Inspect `result_counts`, per-criteria breakdowns, and per-sample failures.
Iterate prompt / model / data. Optionally compare runs (regression).

---

## 3. Package layout

```
evals/
  core.py              EvalSpec, EvalRun, SampleResult (pass/fail/error), ExperimentConfig
  dataset.py           JSONL load/save + hashes + stable sample_id
  prompt.py            {{ item.* }} templating
  models.py            ticket stub + optional OpenAI adapter
  graders.py           string/label/regex/json + guardrail graders
  registry.py          create/store eval definitions
  runner.py            create_run / create_sut_run + per-sample JSONL
  analyze.py           reports + comparison.md / summary.json
  config_util.py       freeze seeds, git commit, experiment config
  sut.py               replaceable systems under test (defense stacks)
  metrics.py           ASR / utility / FPR / latency
  regression.py        automated budget checks (not a single score)
  demo.py              IT ticket regression demo
  experiments/
    baseline.py | input_defense.py | retrieval_defense.py | full_defense.py
    run_all.py
  data/
    tickets.jsonl
    guardrail_eval/{development,validation,heldout}.jsonl
  reports/
    run_results.jsonl | summary.json | comparison.md
  tests/
  README.md | REVIEW.md
```

**Architectural rule:** the system under test is replaceable. The same runner
evaluates baseline, input-only, retrieval, or full-defense stacks via `sut.py`.

---

## 4. Quick start

### 4a. Ticket regression (Week 1 foundation)

```bash
cd evals
python3 demo.py
python3 -m unittest discover -s tests -v
```

You should see:

1. Eval created (`IT Ticket Categorization`)
2. Run completed with **pass / fail / error** per ticket
3. Strong stub vs weak stub **regression signal**
4. Markdown + JSON under `reports/`
5. Per-sample rows in `reports/run_results.jsonl`

### 4b. Guardrail defense experiment (Weeks 2–4)

```bash
cd evals
python3 experiments/run_all.py              # development
python3 experiments/run_all.py validation
python3 experiments/run_all.py heldout      # after freeze
```

Writes `reports/summary.json` + `reports/comparison.md` (ASR, utility, FPR,
errors, latency, regression status). Do **not** use a single overall score as
the only release gate.

### Minimal API sketch (local)

```python
from core import DataSourceConfig
from graders import StringCheckGrader
from models import ticket_classifier_stub
from registry import EvalRegistry
from runner import Runner

registry = EvalRegistry()
runner = Runner()

eval_obj = registry.create(
    name="IT Ticket Categorization",
    data_source_config={
        "type": "custom",
        "item_schema": {
            "type": "object",
            "properties": {
                "ticket_text": {"type": "string"},
                "correct_label": {"type": "string"},
            },
            "required": ["ticket_text", "correct_label"],
        },
    },
    testing_criteria=[
        StringCheckGrader(
            name="Match output to human label",
            input="{{ sample.output_text }}",
            operation="eq",
            reference="{{ item.correct_label }}",
        )
    ],
)

run = runner.create_run(
    eval_obj,
    name="Categorization text run",
    model_name="ticket-stub-v1",
    model_fn=ticket_classifier_stub,
    prompt_template=[
        {"role": "developer", "content": "Categorize as Hardware, Software, or Other."},
        {"role": "user", "content": "{{ item.ticket_text }}"},
    ],
    data_path="data/tickets.jsonl",
)
print(run.result_counts)
```

Optional live model (needs key):

```python
from models import openai_responses_adapter
model_fn = openai_responses_adapter("gpt-4.1-mini")
```

---

## 4c. Per-sample records & outcomes

Each sample is appended to `reports/run_results.jsonl`:

```json
{
  "run_id": "evalrun_…",
  "sample_id": "indirect_001",
  "condition": "retrieval_defense",
  "model_version": "offline-naive-app-v1",
  "dataset_version": "guardrails_v1:development",
  "output_text": "…",
  "grader_results": {},
  "outcome": "pass",
  "passed": true,
  "latency_ms": 12.4,
  "error": null
}
```

| Outcome | Meaning |
|---------|---------|
| **pass** | All graders satisfied |
| **fail** | Model/app violated a criterion |
| **error** | Eval could not complete (timeout, schema, exception) — **not** a safe refusal |

`ExperimentConfig` stores prompt version, model id, temperature/settings,
guardrail config hash, dataset hash, grader version, seed, and git commit.

---

## 5. Graders (testing criteria)

| Type | Use when |
|------|----------|
| `StringCheckGrader` | Exact / contains match to human label |
| `LabelSetGrader` | Output must be one of allowed labels |
| `RegexGrader` | Format constraints |
| `RubricScoreGrader` | Soft quality **heuristic** only — not validated human judgment |
| `ExpectedBehaviorGrader` | answer / refuse / redact vs item.expected_behavior |
| `AttackBlockedGrader` | Security samples: attack must not succeed |
| `NoSecretLeakGrader` | Lab secret markers must not appear |

**LLM-as-judge guidance (from best-practice literature):**

- Prefer pairwise / pass-fail / reference-guided over free-form critique alone  
- Control length bias; ask for reasoning before score  
- Validate agreement with human labels before trusting at scale  
- Start with a strong judge model, then distill if cost matters  

---

## 6. Where nondeterminism enters (architectures)

| Architecture | Extra nondeterminism to eval |
|--------------|------------------------------|
| Single-turn | Instruction following, functional correctness |
| Workflow | Each step’s prompt + correctness of extracted fields |
| Single-agent | **Tool selection** + **argument precision** |
| Multi-agent | **Handoff accuracy** between specialists |

Only add multi-agent complexity when evals show a single agent failing
instruction-following or tool choice under load.

Map these to this repo’s **guardrail** lab: tool-selection evals tell you
*what* to measure; tool guardrails + HITL decide *what may execute*.

---

## 7. Mapping to OpenAI Evals API shapes

| OpenAI concept | This harness |
|----------------|--------------|
| `client.evals.create` | `EvalRegistry.create` |
| `data_source_config` | `DataSourceConfig` |
| `testing_criteria` / graders | `StringCheckGrader`, … |
| JSONL `{"item": ...}` | `data/tickets.jsonl` + `load_jsonl` |
| `evals.runs.create` | `Runner.create_run` |
| `evals.runs.retrieve` | `Runner.retrieve` |
| `result_counts` / report URL | `EvalRun.result_counts` + `reports/*.md` |
| `{{ item.ticket_text }}` | `prompt.render_messages` |

---

## 8. Continuous evaluation (CE)

Recommended loop for production teams:

1. Freeze a **gold** JSONL set (typical + edge + adversarial).  
2. Run evals on every prompt/model/guardrail change in CI.  
3. Mine logs weekly → promote failures into the gold set.  
4. Track pass rate **and** slice by label / locale / length.  
5. Pair with human review on a stratified sample.

---

## 8b. Product eval: lyrics → composer (PyTorch)

**Task:** map lyrics → one of 10 composers (same mindset as OpenAI “Working with evals”).

**Structured entry point:** **[LAB.md](./LAB.md)** + `run_lab.py`

```bash
cd evals
python3 run_lab.py workflow
python3 run_lab.py            # interactive menu
python3 run_lab.py setup && python3 run_lab.py eval
python3 run_lab.py explore    # Gradio
python3 run_lab.py ablate --neuron 5
python3 run_lab.py ce
```

| Step | Artifact / command |
|------|--------------------|
| Define task | `EvalSpec` + `JsonPredEqualsGrader` + `JsonTopKGrader` |
| Gold dataset | `run_lab.py setup` → `data/lyrics_composer_gold.jsonl` |
| Train / load | `artifacts/composer_model.pt` |
| Eval / CE | `run_lab.py eval` / `run_lab.py ce` |
| Explore / ablate | `run_lab.py explore` / `run_lab.py ablate --neuron N` |

Graders:

- **Exact match** — `pred == correct_label`
- **Top-3** — gold composer in model’s top-3 logits (refusal N/A for this task)

### Neuron explorer (interpretability UI)

Inspect what each hidden neuron “contains” (top +/− BoW word weights):

```bash
cd evals
python3 inspect_neurons.py --neuron 42          # terminal Method 1
python3 neuron_explorer.py                      # Gradio + Plotly UI
# open http://127.0.0.1:7860 — use dropdown/slider
```

### Option A — Ablate a neuron & re-eval (composer task only)

Zero selected hidden unit(s) after ReLU at inference, then compare frozen-test metrics:

```bash
cd evals
python3 ablate_and_eval.py --neuron 5           # baseline vs ablated
python3 ablate_and_eval.py --neuron 5,12        # multiple units
python3 ablate_and_eval.py --neuron 5 --save    # also write artifacts/composer_model_ablated.pt
```

Report: `reports/ablation_neurons_*.json` (exact/top3 + deltas). Original `composer_model.pt` is left unchanged unless you overwrite it yourself.

---

## 9. What this lab is not

- Not a hosted Evals cloud (and not a migration target for the deprecated platform).  
- Not a replacement for human judgment on high-stakes domains.  
- Not sufficient alone for dual-use safety (combine with training controls + runtime rails).  
- Stub classifiers are for **harness teaching**; publish numbers only after real models + calibrated graders.

See **[REVIEW.md](./REVIEW.md)** for findings and residual risks.

---

## 10. Takeaway

> Specify behavior as data + graders, freeze the distribution, compare runs.
> Improve prompts and models against that meter — then enforce the same
> contracts at runtime with guardrails.
