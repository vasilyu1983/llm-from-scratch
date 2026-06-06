"""W&B smoke test — run this BEFORE renting a GPU.

Proves your Weights & Biases auth + logging pipe works, for free, in ~10 seconds.
If you see a run appear at https://wandb.ai/<you>/pretraining with a rising curve,
you're ready for Day 3 (the real GPU run) with zero auth surprises.

Usage:
    python3 -m venv .venv && source .venv/bin/activate
    pip install wandb python-dotenv
    cp .env.example .env   # paste your WANDB_API_KEY into .env
    python scripts/wandb_smoke_test.py
"""
import math
import os

from dotenv import load_dotenv

load_dotenv()  # reads .env so WANDB_API_KEY is available

import wandb  # noqa: E402  (import after load_dotenv so the key is set)

project = os.environ.get("WANDB_PROJECT", "pretraining")

run = wandb.init(project=project, name="smoke-test", job_type="smoke")
print(f"Logging a fake training curve to W&B project '{project}'...")

# Simulate a decreasing loss curve so the dashboard shows something familiar.
for step in range(50):
    fake_loss = 3.0 * math.exp(-step / 15) + 0.1
    wandb.log({"loss": fake_loss, "step": step})

run.finish()
print("Done. Open the run URL above — if you see a falling 'loss' curve, your pipe works.")
