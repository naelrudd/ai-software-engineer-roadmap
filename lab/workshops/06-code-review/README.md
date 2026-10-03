# Workshop 06 — Code review

> ⏱ ~75 min · 🎯 Review code like a senior engineer — and review your own.

Code review is a core skill for engineering and evaluation roles. You'll review a PR the way a good reviewer does: correctness first, then clarity, then style.

---

## Part A — The review checklist

For any diff, ask in this order:

1. **Correctness** — does it do what it claims? Edge cases handled?
2. **Tests** — is the behavior covered? Do tests actually assert the right thing?
3. **Security** — injection, unvalidated input, secrets, unsafe defaults?
4. **Performance** — hidden O(n²), repeated work, wrong data structure?
5. **Clarity** — names, structure, dead code, comments where needed?
6. **Consistency** — matches the project's conventions?

Comment severity tags:

- `[blocker]` must fix before merge.
- `[suggestion]` would improve it.
- `[nit]` trivial, optional.
- `[question]` you don't understand something.

---

## Part B — Review a real diff

Review the brute-force two-sum (pretend it's a PR):

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

Write review comments:

```
solution.py:2 [suggestion] O(n^2). A hash map makes this O(n). Acceptable if n is small; flag if not.
solution.py:7 [nit] Return type could be annotated -> list[int].
test_solution.py [question] No test for duplicates like [3, 3]. Is that intentional?
```

That's the format: `file:line [severity] comment`.

---

## Part C — Review your own PR

Before merging any PR in this repo, read your own diff and run the checklist. You'll catch most issues yourself.

```bash
gh pr diff
```

Ask:
- Does every change belong in this PR?
- Any leftover `print()` or commented code?
- Are edge cases tested?
- Is the commit message accurate?

---

## Part D — Review an AI diff

AI diffs often look clean but hide subtle bugs. Review one like a PR:

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

Find the issues:
- Punctuation not removed (`"A man, a plan..."` fails).
- Unicode edge cases.

Write comments in the same format.

---

## Exercises

1. Write 5 review comments on the brute-force two-sum.
2. Review one of your own merged PRs; list what you'd change now.
3. Review an AI-generated solution for `is_palindrome`; find ≥ 2 issues.
4. Write a reusable review checklist in `docs/review-checklist.md`.

---

## Deliverable

- [ ] `docs/review-checklist.md` — your reusable checklist
- [ ] At least 3 written reviews in `reviews/` (format `file:line [severity] comment`)
- [ ] Committed via PR

---

## Checklist

- [ ] Review correctness before style
- [ ] Use severity tags
- [ ] Review your own PR before merging
- [ ] Can find bugs in AI code beyond "it runs"
- [ ] Wrote the checklist
