# Contributing to your own repo

This is your repo, but treat it like a real project. The habits you build here are exactly what engineering roles test.

---

## The workflow (always)

Never commit directly to `main`. Use a branch + PR:

```bash
git switch main
git pull
git switch -c feat/arrays-two-sum

# ... do the work, run tests ...

git add -A
git commit -m "feat(arrays): solve two-sum with hash map"
git push -u origin feat/arrays-two-sum

gh pr create --fill
# review your own diff, then merge
gh pr merge --squash --delete-branch
```

Full guide: [`docs/git-workflow.md`](docs/git-workflow.md).

---

## Commit message style

Use Conventional Commits:

```
feat(arrays): add two-sum solution
fix(strings): handle empty input in is_palindrome
test(hashmaps): add parametrized tests for group_anagrams
docs(module-04): clarify collision handling
refactor(sorting): extract partition helper
```

Format: `type(scope): short description`.

Types: `feat`, `fix`, `test`, `docs`, `refactor`, `chore`.

---

## Definition of done for any exercise

- [ ] Solution implemented in `solution.py`.
- [ ] Tests written in `test_solution.py` **before** or alongside the solution.
- [ ] `make test` passes.
- [ ] `make lint` passes.
- [ ] At least one edge case tested (empty input, single element, duplicates).
- [ ] Committed via a branch + PR.

---

## Code style

- Type hints on public functions.
- Docstrings on public functions (short is fine).
- Prefer clarity over cleverness.
- No commented-out code.
- Follow the formatter/linter (`ruff`) — run `make fmt`.

---

## Testing style

- One test file per solution.
- Use `pytest.mark.parametrize` for multiple cases.
- Use fixtures for shared setup.
- Test behavior, not implementation details.

---

## When stuck

1. Re-read the module README.
2. Do the paired workshop.
3. Write a failing test that shows the problem.
4. Use `pdb` (see workshop 04) before asking anyone.
5. Only then ask an AI — and ask for a **hint**, not the answer.
