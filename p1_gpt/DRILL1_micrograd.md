# Drill 1 — micrograd (your first code that's actually yours)

**The mode just flipped.** Day 3 was "run someone's commands." This is "write it from the
math, by hand." No-paste contract is **active**: no model/engine code enters this folder that
your fingers didn't type. Claude is a *tutor* (explain / quiz / find-my-bug), never a *generator*.

**What you're building:** a tiny scalar autograd engine — a `Value` that wraps a number,
records the operations done to it, and can compute gradients by backpropagation. Then a
small neural net on top of it. ~150 lines total. This is the entire idea behind PyTorch,
shrunk until you can hold it in your head.

**Why this drill first:** if you understand how `.backward()` works at the scalar level, every
framework after this is just a faster, vectorized version of the same idea. Skip it and
autograd stays magic forever.

---

## The two passes (the second is the one that counts)

| Pass | What | Materials open? | Builds |
|---|---|---|---|
| **1 — Code-along** | Watch Karpathy, build alongside, pause to type | Video on | The map |
| **2 — Blank rebuild** | Next day. Empty file. From memory. | **Everything closed** | The skill |

You are not done after Pass 1. You're done when Pass 2 passes the acceptance test from a
blank file. Be honest about which pass you're on.

---

## Pass 1 — Code-along (today, ~2.5 hrs)

1. **▶ Watch + build:** Karpathy, *"The spelled-out intro to backpropagation: building
   micrograd"* — <https://www.youtube.com/watch?v=VMj-3S1tku0>
   - Build in `p1_gpt/micrograd/engine.py` as you watch. **Pause and type** — don't binge then copy.
2. **Build these pieces** (in your own words, following the video's *ideas* not its keystrokes):
   - A `Value` class holding `data`, a `grad` (init 0), and how it was produced (its "children" + the op).
   - Forward ops: `__add__`, `__mul__`, `tanh` (or `exp`/`pow`) — each returns a new `Value`
     and records a local `_backward` closure.
   - `backward()`: topologically sort the graph, then apply the chain rule from output back to inputs.
   - A tiny MLP (Neuron → Layer → MLP) built *on top of* your `Value`.
3. ✅ **End of Pass 1:** you have a working engine that trains a toy net. You followed along — that's fine, it's Pass 1.

---

## Between passes — the explain-back (10 min, do not skip)

Write `p1_gpt/micrograd/NOTES.md`, ~5 lines, **in your own words, no jargon-hiding:**
- What does `.backward()` actually *do*, step by step?
- Why do we **topologically sort** before propagating?
- Why does `grad` **accumulate** (`+=`) instead of being assigned (`=`)? (this one trips everyone)

If you can't write these cleanly, you traced without understanding — rewatch that segment.
This note *is* your interview prep; a residency interviewer asks exactly these.

---

## Pass 2 — Blank rebuild (next day, ~60–90 min) ← THE REP

1. New file: `p1_gpt/micrograd/engine_rebuild.py`. **Video closed. Pass-1 file closed. Claude closed.**
2. Rebuild `Value` + the ops + `backward()` from memory, from the chain rule.
3. Stuck? Use the **hint ladder** — climb one rung, stop when unblocked:
   - **L0:** re-read your `NOTES.md` / whiteboard the chain rule for one node.
   - **L1:** 3Blue1Brown backprop (intuition, no code) — <https://www.youtube.com/watch?v=Ilg3gGewQ5U>
   - **L2:** re-watch *just* the segment you're stuck on, then close it.
   - **L3:** open your Pass-1 file, read the *shape* of the function, **close it**, retype from memory.
   - **L4:** Claude as tutor — `"My backward for tanh gives the wrong grad. What property
     should it satisfy that I can test myself? Don't give me the formula."`
   - 🚫 Never: paste this spec and take generated code.

---

## ✅ Acceptance test (this is your pass/fail — write it yourself)

Build a small expression, run *your* backward, and compare against PyTorch:

```text
# pseudocode of the check — implement it in test_micrograd.py
1. In YOUR engine: a = Value(-4.0); b = Value(2.0); build c = (a*b + b).tanh(); c.backward()
2. In PyTorch:     same expression with requires_grad=True tensors; c.backward()
3. assert your a.grad ≈ torch a.grad  (abs diff < 1e-6), same for b
4. Also: train your MLP to separate a tiny 2-class toy set to loss < 0.05
```

- **Score 2** = the test passes from your **blank rebuild** (Pass 2).
- **Score 3** = also passed the explain-back + you can whiteboard the backward through a
  `*` node and a `tanh` node, cold.

---

## Diff-after (only now may you open the reference)

**After** your rebuild passes, clone the reference and `diff` against it — as an answer key,
not a source:
- `git clone https://github.com/karpathy/micrograd`
- Note ≥1 thing it does more cleanly than yours and *why*. Write it in `NOTES.md`. The
  learning is in the diff.

---

## Allowed / banned Claude prompts (for this drill)

- ✅ `"Explain why grad accumulates instead of overwrites in backprop. No code."`
- ✅ `"Quiz me with 5 questions on topological sort in autograd. Wait for each answer."`
- ✅ `"Here's my backward for __mul__. There's a bug — which line, and what concept? Don't fix it."`
- 🚫 `"Write the Value class / the backward method / the MLP."`
- 🚫 pasting this file and taking the output.

> Plumbing exception: the **plotting** of your toy decision boundary or loss curve — generate
> that freely. It's not the mechanic you're here to learn.

---

## When done — log it

In the private `progress_log.md`: drill score (0–3), Pass-2 rebuild time, one thing the
diff-after taught you. Commit `p1_gpt/micrograd/` to the public repo — **this is your first
portfolio code that's genuinely yours.**

**Next after this:** Drill 2 (makemore — bigram + MLP language model).
