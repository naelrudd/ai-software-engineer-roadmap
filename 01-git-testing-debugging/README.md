# Level 1 — Git + Testing + Debugging

> 🎯 **Target:** not just *"I've used it"*, but **can write a test that deliberately catches a bug**. Several Micro1 roles explicitly ask for Git/GitHub workflow, PRs, code review, branching, diff analysis, CI logs, and automated testing.

---

## 📚 Learn

### Git
```
git clone      git branch     git checkout   git switch
git add        git commit     git diff       git log
git reset      git revert     git stash      git merge
git rebase     git cherry-pick
```

### GitHub
`Pull Request` · `Issues` · `Code Review` · `Actions` · `Releases` · `Tags`

### Testing
- **Python:** `pytest` · `fixtures` · `mock` · `unit test` · `integration test`
- **JS:** `Vitest` · `Jest`

### Debugging
`pdb` · breakpoints · watch variables · stack traces · binary-search debugging · `git bisect`

### Free sources
- [Pro Git Book (free)](https://git-scm.com/book/en/v2) — chapters 1–3 are essential
- [Learn Git Branching (visual, interactive)](https://learngitbranching.js.org/)
- [Oh Shit, Git!?!](https://ohshitgit.com/) — how to escape common Git mistakes
- [GitHub Skills (official interactive courses)](https://github.com/skills)
- [GitHub Get Started](https://docs.github.com/en/get-started)
- [pytest docs](https://docs.pytest.org/en/stable/)
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pdb docs](https://docs.python.org/3/library/pdb.html)
- [Vitest Guide](https://vitest.dev/guide/)
- [Jest Getting Started](https://jestjs.io/docs/getting-started)

---

## 🧪 Exercise

### Git drills
In the `nael-algorithms` repo:
1. Create branch `feat/array-two-sum`, commit, open a PR, review it yourself, merge.
2. Deliberately create a merge conflict → resolve it.
3. Practice rebasing a branch onto `main`, then `cherry-pick` a commit.
4. Use `git bisect` to find the commit that broke a test.

### Testing drills
- Write tests with `fixture` + `parametrize` + `mock`.
- Write 3 tests that **must fail** first (catching a bug), then fix the code.
- Write 1 integration test that hits a real API (not a mock).

---

## 🐛 Bug Hunt

Take someone's code (or an AI solution), write a test that proves the bug, then:
```
1. git bisect to find the origin of the bug (if history exists)
2. write a regression test
3. fix
4. make sure all tests are green
```

---

## 🤖 AI Challenge

Ask an AI to write code **without tests**. Your job:
1. Write tests that probe edge cases.
2. Find at least 1 bug.
3. Write a report: *"The AI said X, but actually Y, because Z."*

---

## 📝 Evaluation

Simulate a **code review**: take 1 AI-generated PR and review it like a senior engineer. Write comments covering: correctness, edge cases, security, readability. Save to `reviews/pr-review-01.md`.

---

## 🏆 Final Task

- [ ] 1 real PR (branch → commit → PR → review → merge) documented
- [ ] ≥ 20 tests in `nael-algorithms`, including fixtures & mock
- [ ] 3 regression tests from bugs you actually found
- [ ] `reviews/` contains at least 1 written code review

---

## ✅ Level 1 pass checklist

- [ ] Can explain `merge` vs `rebase` vs `cherry-pick` without opening Google
- [ ] Comfortable with PRs, reviews, and branch workflows
- [ ] Can write a test that **fails because of a bug**, not just one that passes
- [ ] Can debug with `pdb` / a debugger, not just `print()`
- [ ] Can read CI logs
