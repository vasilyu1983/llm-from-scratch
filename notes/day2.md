# Day 2 — Deep Dive into LLMs (mental map)

> **Source:** Karpathy, *"Deep Dive into LLMs like ChatGPT"* — <https://www.youtube.com/watch?v=7xTGNNLPyMI>
> **Goal of this note:** explain pre-training vs post-training **in your own words**, from
> memory, *after* the video. Don't paste definitions — if you can't write it cold, rewatch
> that segment. The struggle to phrase it is the learning.

**Date watched:** YYYY-MM-DD · **Speed:** ___× · **Stopped at (if split):** ___

---

## 1. The one-sentence version (write last, after filling the rest)

> Pre-training is ________. Post-training is ________. The difference that matters is ____.

## 2. Pre-training — in my own words (3–4 lines)

- **What it does:**
- **What data:** (where does it come from? how much?)
- **What the model learns:** (predict ____ → it ends up knowing ____)
- **What it canNOT yet do well:**

## 3. Post-training — in my own words (3–4 lines)

- **What it does on top of pre-training:**
- **What data:** (how is it different from pre-training data — who makes it?)
- **The stages I heard named:** (SFT → ___ → ___?)
- **What problem each stage fixes:**

## 4. Things that surprised me / didn't click (be honest — this is the gold)

- 🟢 Clicked:
- 🔴 Fuzzy / want to revisit:
- ❓ Question I'd ask an OpenAI researcher:

## 5. Where this maps onto MY plan

- Pre-training is **Phases 1–3** of my track (the part I'm betting on). My edge lives in: ____
- Post-training is **Phase 4**. I'll only touch it after I own a base model.

---

### Jargon I met today (one line each, my words — leave blank if not covered)

| Term | My one-line meaning |
|---|---|
| token |  |
| context window |  |
| base model vs instruct model |  |
| hallucination (why it happens) |  |
| RLHF |  |

> ✅ When this file is filled in: commit it (`git add notes/day2.md && git commit -m "Day 2 notes"`),
> then log one line in the private `progress_log.md`, and you're cleared for **Day 3 — nanoGPT**.
