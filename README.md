# llm-from-scratch

Learning LLM pre-training and data engineering by building from scratch —
trained models, datasets, and experiments, in the open.

## Structure

| Folder | Phase | What lives here |
|--------|-------|-----------------|
| `p1_gpt/` | Phase 1 | GPT from scratch — own tokenizer, own model (Raschka + Karpathy) |
| `p2_pretrain/` | Phase 2 | Real pre-training, systems, GPT-2 124M reproduction (CS336) |
| `p3_data/` | Phase 3 | Data curation + synthetic data pipelines (datatrove, FineWeb-style) |
| `p4_posttrain/` | Phase 4 | SFT, DPO/RLHF, evals |
| `scripts/` | — | Utilities (e.g. W&B smoke test) |
| `notes/` | — | Paper notes, screenshots, learnings |

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then paste your real tokens into .env (gitignored)
```

## Track record

Experiments logged to Weights & Biases (`pretraining` project).

## Milestones

- [x] M0 — nanoGPT trained + logged (Phase 0) — RTX 4090, val loss 1.47, [W&B run](https://wandb.ai/vasilyu-/pretraining/runs/yse7n9ae)
- [ ] M1 — own GPT + own tokenizer, trained from scratch (Phase 1)
- [ ] M2 — reproduced GPT-2 124M (Phase 2)
- [ ] M3 — 2 published datasets + ablation report (Phase 3)
- [ ] M4 — base→instruct model pair + research note (Phase 4)
- [ ] M5 — OSS contributions + reproduced recent result + paper (Year 2)
