# How to use this repo

This repo is a **self-paced course**. It only works if you actually write the code and the tests yourself.

---

## The method

### 1. Read the module
Open `modules/NN-name/README.md`. Read the concepts, the patterns, and the pitfalls. Don't skim the pitfalls — those are where real bugs live.

### 2. Do the workshop
Each module pairs with a workshop (see [`SYLLABUS.md`](../SYLLABUS.md)). Workshops are step-by-step. Do them in a branch.

### 3. Solve the exercises
For each problem, copy the template:

```bash
make new-problem PROBLEM=two_sum
# or manually: cp -r templates/problem exercises/two_sum && touch exercises/two_sum/__init__.py
```

Each exercise is its own Python package (note the `__init__.py`), so its
`solution.py` won't collide with other exercises. Import it with a relative
import in tests: `from .solution import ...`.

Then:
- Write the **test first** when you can (TDD).
- Implement the solution.
- Run `make test` until green.
- Add at least one edge case.

### 4. Commit via PR
Follow [`git-workflow.md`](git-workflow.md). Every exercise gets its own branch + PR.

### 5. Explain it
Write 3 lines in the module's `NOTES.md` explaining the concept in your own words. If you can't, you don't understand it yet.

---

## Rules of engagement

- **No solution without a test.** Untested code is unfinished code.
- **No copy-paste of answers.** Use hints and docs, not someone's solution.
- **Stuck > 20 minutes?** Use `pdb` (workshop 04), re-read the module, then ask for a *hint*.
- **Prefer the standard library.** Before reaching for a trick, check what Python already gives you.

---

## Asking an AI for help (the right way)

Good:
> "I'm solving two-sum with a hash map. My test fails on duplicate values. Give me a hint about what I'm missing, don't give the code."

Bad:
> "Write two-sum for me."

After an AI writes something, treat it as a **candidate solution to review** — not the truth. Find its bug. (Workshop 07 trains exactly this.)

---

## Time budget

- 3–5 hours per module is normal.
- If a module takes much longer, that's a signal — slow down, do the workshop, re-read.
- If a module feels trivial, still do the tests and edge cases. That's the real skill.

---

## What "done" means

See the completion rule in [`SYLLABUS.md`](../SYLLABUS.md#module-completion-rule). Short version: concept explained + workshop done + exercises pass with tests + committed via PR.
