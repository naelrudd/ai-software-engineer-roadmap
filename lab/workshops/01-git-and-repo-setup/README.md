# Workshop 01 — Git & repo setup

> ⏱ ~90 min · 🎯 Set up your workflow and complete your first branch → PR → merge cycle.

Do this **first**, before any module. It builds the habit you'll use for every exercise.

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
make test                         # should pass (no tests yet is fine)
```

Create your first branch and confirm tooling:

```bash
git switch -c chore/initial-setup
git add -A
git commit -m "chore: initial repo setup"
git push -u origin chore/initial-setup
gh pr create --fill
```

---

## Exercise 1 — Complete the loop

1. Open a PR from your branch.
2. `gh pr diff` — read your own changes.
3. Merge with `gh pr merge --squash --delete-branch`.
4. `git switch main && git pull`.

You just did the core workflow. Every exercise from now on uses it.

---

## Exercise 2 — Resolve a conflict

1. Create `conflict.txt` on `main` with `line = A`. Commit.
2. Branch `fix/conflict`, change the same line to `line = B`. Commit.
3. On `main`, change it to `line = C`. Commit.
4. `git switch fix/conflict && git merge main` → conflict.
5. Resolve by hand, commit, merge the PR.

**Deliverable:** a note in `docs/` describing what you learned about conflicts.

---

## Exercise 3 — Rebase

1. Branch off `main`, make 2 commits.
2. Meanwhile, add a commit to `main`.
3. `git switch your-branch && git rebase main`.
4. Resolve any conflict, then `git rebase --continue`.

Understand the difference: rebase rewrites history for a linear log; merge preserves it.

---

## Exercise 4 — Cherry-pick

1. On a branch, make 3 commits.
2. Copy one of them onto `main` with `git cherry-pick <sha>`.
3. Verify only that change landed.

---

## Exercise 5 — Bisect

1. Make 5 commits, one of which introduces a failing test.
2. `git bisect start`
3. `git bisect bad` (current), `git bisect good <old-sha>`
4. Test at each step, mark `good`/`bad`.
5. Git identifies the culprit commit.
6. `git bisect reset`

---

## Exercise 6 — Stash

1. Make uncommitted changes.
2. `git stash` → working tree clean.
3. `git stash pop` → changes back.

---

## Deliverable

Create `docs/git-drills.md` documenting each exercise: the command(s), what happened, and what surprised you.

Commit it via a branch + PR.

---

## Checklist

- [ ] Completed a full branch → PR → merge cycle
- [ ] Resolved a merge conflict by hand
- [ ] Rebased a branch onto `main`
- [ ] Cherry-picked a single commit
- [ ] Found a bug commit with `git bisect`
- [ ] Used `git stash`
- [ ] Wrote `docs/git-drills.md`
