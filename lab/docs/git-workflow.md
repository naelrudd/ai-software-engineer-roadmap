# Git workflow

Every exercise and workshop uses the same loop. Build this habit now — it's exactly how real teams work.

---

## The loop

```bash
# 1. start clean
git switch main
git pull

# 2. branch (one branch per task)
git switch -c feat/arrays-two-sum

# 3. work + test
make test

# 4. commit (small, focused commits)
git add -A
git commit -m "feat(arrays): solve two-sum with hash map"

# 5. push + open a PR
git push -u origin feat/arrays-two-sum
gh pr create --fill

# 6. review your own diff, then merge
gh pr diff
gh pr merge --squash --delete-branch
```

---

## Branch naming

```
feat/<topic>-<problem>     feat/arrays-two-sum
fix/<topic>-<problem>      fix/strings-empty-input
test/<topic>-<problem>     test/hashmaps-anagrams
docs/<what>                docs/module-04-notes
workshop/<number>          workshop/02-tdd
```

---

## Commit messages

Conventional Commits:

```
feat(scope): add something
fix(scope): fix something
test(scope): add tests
docs(scope): update docs
refactor(scope): restructure without behavior change
chore(scope): tooling, config
```

One logical change per commit. If your message needs "and", split it.

---

## The commands that matter

| Goal | Command |
|------|---------|
| See what changed | `git status`, `git diff` |
| Unstage a file | `git restore --staged <file>` |
| Discard local changes | `git restore <file>` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Undo last commit (drop changes) | `git reset --hard HEAD~1` |
| Save work in progress | `git stash`, then `git stash pop` |
| See history | `git log --oneline --graph --all` |
| Who changed this line | `git blame <file>` |
| Find the commit that broke it | `git bisect start` |

---

## Practice drills (do these once)

1. **Resolve a conflict.** Edit the same line on `main` and a branch, merge, resolve.
2. **Rebase.** Make 2 commits on a branch, `git rebase main`, resolve if needed.
3. **Cherry-pick.** Pick one commit from another branch with `git cherry-pick <sha>`.
4. **Bisect.** Introduce a bug in an old commit, find it with `git bisect`.

These are covered in [`workshops/01-git-and-repo-setup`](../workshops/01-git-and-repo-setup/README.md).

---

## Reviewing your own PR

Before merging, read your own diff as if someone else wrote it:

- [ ] Does each change belong in this PR?
- [ ] Any leftover debug code, `print()`, or commented code?
- [ ] Are edge cases tested?
- [ ] Is the commit message accurate?

This is the habit that makes you a good reviewer — and good reviewers are what evaluation roles hire.
