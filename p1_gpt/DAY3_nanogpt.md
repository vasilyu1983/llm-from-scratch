# Day 3 — Rent & Drive a Cloud GPU (ops rehearsal)

**This is NOT a coding milestone — it's an operations rehearsal.** Goal: prove you can
*provision → inspect → run → monitor → STOP* a rented GPU end-to-end on a $2 throwaway,
before you bet ~$200 on the GPT-2 reproduction in Phase 2. You'll write no model code today;
you're learning to drive the hardware.

**Done = these gates pass**, not "I trained a model":
- [ ] **Gate A** — GPU provisioned and I confirmed it with `nvidia-smi`
- [ ] **Gate B** — PyTorch sees CUDA (`torch.cuda.is_available() == True`)
- [ ] **Gate C** — a training run logged live to W&B from the remote box
- [ ] **Gate D** — I watched GPU utilization during the run (not stuck at ~0%)
- [ ] **Gate E** — **pod STOPPED/terminated**, billing shows ~$1–3

**Golden rule: STOP THE POD when done.** A forgotten GPU overnight is how budgets die.

---

## Step 1 — Provision a GPU (RunPod web UI)

1. <https://runpod.io> → **Pods** → **Deploy**.
2. GPU: a single **RTX 4090** (~$0.40–0.70/hr) or **A40/A5000** — any is fine for this.
3. Template: **"RunPod PyTorch 2.x"** (CUDA + PyTorch preinstalled).
4. **On-Demand** (not Spot) for your first run — no preemption to worry about.
5. Disk: default. **Deploy On-Demand** → wait for **Running** → **Connect** →
   **Start Web Terminal** (or Jupyter Lab → terminal).

> **What you're learning:** *On-Demand vs Spot* (Spot is cheaper but can be killed mid-run);
> GPU *type ↔ VRAM* (a 4090 has 24 GB — that caps your batch size / model size later).

---

## Step 2 — Inspect the GPU (this is the actual skill) ✅ Gate A + B

Before running anything, confirm what you rented. This is the habit most people skip.

```bash
nvidia-smi
```
Read it: **GPU name**, **memory** (e.g. `0MiB / 24564MiB` = 24 GB free), **driver/CUDA
version**, and any processes. This is your single most-used GPU command — run it any time
you wonder "what's happening on the card?"

Now confirm **PyTorch can actually see the GPU** (a different thing from `nvidia-smi`):

```bash
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0), torch.cuda.mem_get_info())"
```
Expect `True <GPU name> (free_bytes, total_bytes)`. If it prints `False`, the CUDA/PyTorch
build is wrong — **stop and fix this before spending time**, it's the #1 silent time-sink.

---

## Step 3 — Set up (paste your W&B key)

Copy your key from your local `.env` or <https://wandb.ai/authorize>:

```bash
pip install -q wandb tiktoken
export WANDB_API_KEY=PASTE_YOUR_KEY_HERE
git clone https://github.com/karpathy/nanoGPT && cd nanoGPT
python data/shakespeare_char/prepare.py   # downloads + tokenizes tiny Shakespeare
```

---

## Step 4 — Run + monitor utilization ✅ Gate C + D

Start the run (logs to your `pretraining` W&B project):

```bash
python train.py config/train_shakespeare_char.py \
  --device=cuda --compile=True \
  --wandb_log=True --wandb_project=pretraining --wandb_run_name=shakespeare-01 \
  --max_iters=2000 --eval_interval=250 --eval_iters=100 --log_interval=10
```

**While it runs, open a second terminal** (RunPod → new web terminal) and watch the card live:

```bash
watch -n 1 nvidia-smi          # refreshes every second
# look at the "GPU-Util %" column and the memory usage
```

- **GPU-Util pinned high (80–100%)** = the GPU is the bottleneck = good, you're using what
  you paid for.
- **GPU-Util low (~5–20%)** = you're bottlenecked elsewhere (data loader / CPU) = the
  lesson of this step. On a $200 run that's money burning while the GPU idles.

Also watch the loss fall in the terminal **and** live at <https://wandb.ai/vasilyu-/pretraining>.
Finishes in a few minutes on a 4090; val loss should land ~1.4–1.5.

---

## Step 5 — Generate text from the model you just trained

```bash
python sample.py --out_dir=out-shakespeare-char --num_samples=3 --max_new_tokens=300
```
Shakespeare-flavoured text from a transformer that didn't exist 10 minutes ago. 🎉

---

## Step 6 — ⚠️ STOP THE POD (do not skip) ✅ Gate E

RunPod dashboard → your pod → **Stop** (keeps disk, small storage cost) or **Terminate**
(deletes everything, $0 going forward). For a one-off, **Terminate** is fine.

- [ ] Pod stopped/terminated.
- [ ] Billing shows ~$1–3 spent.

> **Build the reflex now:** the *first* thing you do after a run finishes — before notes,
> before screenshots — is kill the pod. Make it muscle memory on the $2 run so it's automatic
> on the $200 one.

---

## Step 7 — Log it as what it is (back on your Mac)

In the private `progress_log.md`, log this honestly as an **ops rehearsal**, not a learning
milestone: *GPU type, cost, final val loss, W&B link, and which Gates A–E passed.* Note your
**peak GPU-Util %** — that's the number that matters for cost efficiency later. Screenshot the
W&B curve into `notes/`. That's **Milestone 0 — toolchain verified.**

---

## Troubleshooting (don't debug > 15 min on a paid pod — note it, terminate, ask)
- `torch.cuda.is_available()` is `False` → wrong template; redeploy with "RunPod PyTorch 2.x".
- `--compile=True` errors on some GPUs → rerun with `--compile=False`.
- Out of memory (`CUDA out of memory`) → add `--batch_size=32` (or 16). This is the 24 GB
  VRAM ceiling talking — exactly the constraint you're learning to feel.
- GPU-Util stuck near 0% → the data loader/CPU is the bottleneck, not the GPU.
