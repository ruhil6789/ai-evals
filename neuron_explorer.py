"""
Interactive neuron explorer (Gradio + Plotly).

- Overview chart: each hidden neuron's strongest + / − weight
- Click a bar (or use the slider) → see top +/− words and composer push

Usage:
  cd evals
  python3 neuron_explorer.py
  # open http://127.0.0.1:7860
"""

from __future__ import annotations

import argparse
from pathlib import Path

import plotly.graph_objects as go
import torch

from lyrics_lib import CKPT_PATH, load_checkpoint

_MODEL = None
_VOCAB = None
_ID2LABEL = None
_ID2WORD = None
_W0 = None
_B0 = None
_W2 = None


def _load(ckpt: Path) -> None:
    global _MODEL, _VOCAB, _ID2LABEL, _ID2WORD, _W0, _B0, _W2
    _MODEL, _VOCAB, _ID2LABEL, _ = load_checkpoint(ckpt)
    _ID2WORD = {idx: w for w, idx in _VOCAB.items()}
    _W0 = _MODEL.net[0].weight.detach()
    _B0 = _MODEL.net[0].bias.detach()
    _W2 = _MODEL.net[2].weight.detach()


def overview_figure(selected: int | None = None) -> go.Figure:
    H = _W0.shape[0]
    max_pos = _W0.max(dim=1).values.cpu().numpy()
    max_neg = _W0.min(dim=1).values.cpu().numpy()
    xs = list(range(H))

    fig = go.Figure()
    fig.add_trace(
        go.Bar(name="max + weight", x=xs, y=max_pos, marker_color="#2ca02c", opacity=0.85)
    )
    fig.add_trace(
        go.Bar(name="max − weight", x=xs, y=max_neg, marker_color="#d62728", opacity=0.85)
    )
    if selected is not None and 0 <= selected < H:
        fig.add_vline(
            x=selected,
            line_width=2,
            line_dash="dash",
            line_color="#1f77b4",
            annotation_text=f"neuron {selected}",
            annotation_position="top",
        )
    fig.update_layout(
        title="Hidden neurons — strongest + and − word weights (click a bar)",
        xaxis_title="Neuron index",
        yaxis_title="Weight",
        barmode="relative",
        clickmode="event+select",
        height=420,
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        margin=dict(l=40, r=20, t=60, b=40),
    )
    fig.update_xaxes(dtick=8)
    return fig


def neuron_from_event(evt, fallback: int) -> int:
    n = int(fallback)
    if evt is None:
        return n
    try:
        # Gradio SelectData
        if hasattr(evt, "index") and evt.index is not None:
            idx = evt.index
            return int(idx[0] if isinstance(idx, (list, tuple)) else idx)
        if isinstance(evt, dict):
            pts = evt.get("points") or []
            if pts:
                return int(pts[0].get("x", n))
    except Exception:
        return n
    return n


def neuron_detail(neuron_i: int, top_k: int = 20):
    H, V = _W0.shape
    neuron_i = max(0, min(H - 1, int(neuron_i)))
    top_k = max(5, min(50, int(top_k)))

    row = _W0[neuron_i]
    bias = float(_B0[neuron_i])

    pos_vals, pos_idx = torch.topk(row, min(top_k, V))
    neg_vals, neg_idx = torch.topk(-row, min(top_k, V))

    pos_rows = [
        [i + 1, _ID2WORD.get(int(j), str(j)), f"{v:+.4f}"]
        for i, (v, j) in enumerate(zip(pos_vals.tolist(), pos_idx.tolist()))
    ]
    neg_rows = [
        [i + 1, _ID2WORD.get(int(j), str(j)), f"{v:+.4f}"]
        for i, (v, j) in enumerate(zip((-neg_vals).tolist(), neg_idx.tolist()))
    ]

    col = _W2[:, neuron_i]
    comp_rows = [
        [_ID2LABEL[c], f"{score:+.4f}"]
        for c, score in sorted(enumerate(col.tolist()), key=lambda t: -t[1])
    ]

    md = f"""
### Neuron **{neuron_i}** / {H - 1}

- **Bias** \(b_i\): `{bias:+.4f}`
- **What makes a word + or −?** the learned weight `W[neuron, word]` in the first `Linear` layer
  - **+ weight** → word raises this neuron when it appears in the lyric (BoW count)
  - **− weight** → word suppresses this neuron
- \(z_i = \\sum_j W_{{ij}} x_j + b_i\\), then \(h_i = \\mathrm{{ReLU}}(z_i)\)
"""
    return overview_figure(selected=neuron_i), md, pos_rows, neg_rows, comp_rows, neuron_i


def build_app():
    import gradio as gr

    H = _W0.shape[0]
    neuron_choices = list(range(H))

    with gr.Blocks(title="Composer MLP Neuron Explorer") as demo:
        gr.Markdown(
            """
# Neuron explorer — lyrics → composer MLP

Pick a neuron with the **dropdown** or **slider** (Gradio `Plot` has no click-select
in this version). The chart highlights the selected neuron with a dashed line.
Tables show strongest **positive** and **negative** word weights (Method 1),
plus how that neuron pushes each composer in the output layer.
"""
        )
        with gr.Row():
            neuron_dd = gr.Dropdown(
                choices=neuron_choices,
                value=0,
                label="Select neuron (click here)",
                allow_custom_value=False,
            )
            neuron = gr.Slider(0, H - 1, value=0, step=1, label="Neuron index")
            top_k = gr.Slider(5, 40, value=20, step=1, label="Top words (+/−)")

        plot = gr.Plot(label="Overview (+ max / − min weight per neuron)")
        summary = gr.Markdown()

        with gr.Row():
            pos_table = gr.Dataframe(
                headers=["#", "word", "weight"],
                label="Positive words (activate neuron)",
                interactive=False,
                wrap=True,
            )
            neg_table = gr.Dataframe(
                headers=["#", "word", "weight"],
                label="Negative words (suppress neuron)",
                interactive=False,
                wrap=True,
            )
        comp_table = gr.Dataframe(
            headers=["composer", "output weight from this neuron"],
            label="Composer push (layer-2 column)",
            interactive=False,
        )

        outputs = [plot, summary, pos_table, neg_table, comp_table]

        def refresh(n, k):
            fig, md, pos, neg, comp, _ni = neuron_detail(n, k)
            return fig, md, pos, neg, comp

        def from_dropdown(n, k):
            n = int(n) if n is not None else 0
            fig, md, pos, neg, comp, ni = neuron_detail(n, k)
            return fig, md, pos, neg, comp, ni

        def from_slider(n, k):
            fig, md, pos, neg, comp, ni = neuron_detail(n, k)
            return fig, md, pos, neg, comp, ni

        demo.load(fn=refresh, inputs=[neuron, top_k], outputs=outputs)

        # Dropdown ↔ slider stay in sync; both refresh panels
        neuron_dd.change(
            fn=from_dropdown,
            inputs=[neuron_dd, top_k],
            outputs=outputs + [neuron],
        )
        neuron.change(
            fn=from_slider,
            inputs=[neuron, top_k],
            outputs=outputs + [neuron_dd],
        )
        top_k.change(fn=refresh, inputs=[neuron, top_k], outputs=outputs)

    return demo


def main() -> None:
    parser = argparse.ArgumentParser(description="Gradio neuron explorer")
    parser.add_argument("--ckpt", type=str, default=str(CKPT_PATH))
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=7860)
    parser.add_argument("--share", action="store_true")
    args = parser.parse_args()

    _load(Path(args.ckpt))
    print(
        f"Loaded neurons={_W0.shape[0]} vocab={_W0.shape[1]} classes={len(_ID2LABEL)}"
    )
    demo = build_app()
    demo.launch(server_name=args.host, server_port=args.port, share=args.share)


if __name__ == "__main__":
    main()
