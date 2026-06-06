# Day 3 — Train nanoGPT on a rented GPU

First real training run. Expect ~$1–3 total and ~20–40 min of active work.
**Golden rule: STOP THE POD when done.**

---

## Step 1 — Launch a GPU on RunPod (web UI)

1. <https://runpod.io> → **Pods** → **Deploy**.
2. GPU: pick a single **RTX 4090** (~$0.40–0.70/hr) or **RTX A5000/A40** — any is fine.
3. Template: **"RunPod PyTorch 2.x"** (has CUDA + PyTorch preinstalled).
4. Disk: default is fine. Click **Deploy On-Demand**.
5. When it shows **Running** → **Connect** → **Start Web Terminal** (or Jupyter Lab terminal).

> Tip: On-Demand (not Spot) for your first run — no preemption to worry about.

---

## Step 2 — On the pod terminal, set up

Paste your W&B key where shown (copy it from your local `.env`, or from
<https://wandb.ai/authorize>):

```bash
pip install -q wandb tiktoken
export WANDB_API_KEY=PASTE_YOUR_KEY_HERE
git clone https://github.com/karpathy/nanoGPT && cd nanoGPT
python data/shakespeare_char/prepare.py   # downloads + tokenizes tiny Shakespeare
```

---

## Step 3 — Train (logs to your 'pretraining' W&B project)

```bash
python train.py config/train_shakespeare_char.py \
  --device=cuda --compile=True \
  --wandb_log=True --wandb_project=pretraining --wandb_run_name=shakespeare-01 \
  --max_iters=2000 --eval_interval=250 --eval_iters=100 --log_interval=10
```

- Watch the loss fall in the terminal **and** live at
  <https://wandb.ai/vasilyu-/pretraining>.
- Finishes in a few minutes on a 4090. Val loss should land around ~1.4–1.5.

---

## Step 4 — Generate text from YOUR trained model

```bash
python sample.py --out_dir=out-shakespeare-char --num_samples=3 --max_new_tokens=300
```

You'll get (Shakespeare-flavoured) text from a transformer you just trained. 🎉

---

## Step 5 — ⚠️ STOP THE POD (do not skip)

RunPod dashboard → your pod → **Stop** (pause, keeps disk, small storage cost) or
**Terminate** (deletes everything, $0 going forward). For a one-off, **Terminate** is fine.

- [ ] Pod stopped/terminated.
- [ ] Billing shows ~$1–3 spent.

---

## Step 6 — Log it (back on your Mac)

Add an entry to the private `progress_log.md`: GPU used, cost, final val loss, W&B link,
one surprise. Screenshot the W&B curve into `notes/`. That's **Milestone 0 — done.**

---

### If something errors
- `--compile=True` fails on some GPUs → rerun with `--compile=False`.
- Out of memory → add `--batch_size=32` (or 16).
- Don't debug for more than 15 min on a paid pod — note it, terminate, ask for help.
