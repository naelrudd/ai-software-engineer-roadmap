# Workshop 08 — Capstone

> ⏱ ~6h · 🎯 Build your own problem set with tests, CI, and a review — end to end.

This proves you can run the whole loop: design, implement, test, review, and ship.

---

## Goal

Create a **themed problem set** of 5 problems on a topic you choose, with:
- solutions
- tests (including edge cases)
- one deliberate bug exercise for others to find
- a reference review of one AI solution
- green CI

---

## Step 1 — Choose a theme

Pick a coherent topic, e.g.:
- "String manipulation essentials"
- "Graph traversal starter pack"
- "Dynamic programming warm-ups"
- "Hash map patterns"

Write a one-paragraph description in `exercises/capstone/README.md`.

---

## Step 2 — Write 5 problems

For each, follow the template (`templates/problem/`):
- `problem.md` — description, examples, constraints, edge cases
- `solution.py` — your implementation, typed + documented
- `test_solution.py` — parametrized tests + edge cases
- `README.md` — approach + complexity

Rules:
- At least 2 problems must use different data structures.
- At least 1 problem must have a non-trivial complexity improvement (brute force → better).

---

## Step 3 — Plant a bug

Create `exercises/capstone/bug-hunt/` with:
- A function that contains **one subtle bug** (off-by-one, aliasing, wrong init, etc.).
- A `BUG.md` explaining the intended behavior (but not the bug).
- A `test_bug.py` that is **xfail** until fixed (`@pytest.mark.xfail`).

This mirrors the coding-agent evaluation work: you build the challenge.

---

## Step 4 — Reference review

Pick one problem and ask an AI to solve it. Then:
- Review its solution with your rubric.
- Document in `evaluation/capstone-ai-review.md` whether it's correct, and why.

---

## Step 5 — Wire up CI

Confirm `.github/workflows/ci.yml` runs on your branch and passes:

```bash
git push -u origin feat/capstone
gh pr checks
```

The PR must show a green check before you merge.

---

## Step 6 — README

In `exercises/capstone/README.md`, document:
- The theme and why.
- The list of problems with their complexities.
- The bug you planted and the intended fix.
- What you learned.

---

## Deliverable

- [ ] 5 problems, each with solution + tests + README
- [ ] 1 planted-bug exercise (`xfail` test)
- [ ] 1 AI solution review
- [ ] CI green on the PR
- [ ] Capstone README
- [ ] Merged via PR

---

## Final checklist

- [ ] Every solution is tested and typed
- [ ] Edge cases covered everywhere
- [ ] Complexity documented per problem
- [ ] CI passes on the PR
- [ ] You can explain every line you wrote
- [ ] You can find the planted bug from memory

---

## Where next

You've finished the lab. Next steps (see the roadmap repo):
- Move to **pytest at scale**, mocking, and integration tests.
- Build a real project (`nael-api-lab`): FastAPI + PostgreSQL + Docker + CI.
- Start **AI evaluation** work: rubrics, pairwise, coding-agent verifiers.

You now have the habits that matter: tests first, review everything, measure before optimizing, and never trust code you didn't verify.
