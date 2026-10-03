# Workshop 02 — TDD your first solution

> ⏱ ~90 min · 🎯 Solve a problem test-first and feel the difference.

TDD loop: **Red → Green → Refactor**. Write a failing test, make it pass, then clean up.

---

## The problem: `two_sum(nums, target)`

Return indices `[i, j]` (i < j) such that `nums[i] + nums[j] == target`. Exactly one solution exists. You may not use the same element twice.

---

## Step 1 — Scaffold

```bash
make new-problem PROBLEM=two_sum
# or: cp -r templates/problem exercises/two_sum && touch exercises/two_sum/__init__.py
cd exercises/two_sum
```

---

## Step 2 — Red

In `test_solution.py`, write the smallest failing test:

```python
from .solution import two_sum


def test_simple():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
```

Run `make test` → it fails (`NotImplementedError`). Good. That's the "red".

---

## Step 3 — Green

Implement the simplest thing that passes:

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

Run `make test` → green. Brute force is fine for green.

---

## Step 4 — Add cases

Add tests **before** improving:

```python
import pytest


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4], -7, [2, 3]),
    ],
)
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected
```

They should pass with the brute-force version too.

---

## Step 5 — Refactor (improve complexity)

Brute force is O(n²). Improve to O(n) with a hash map:

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```

Run the **same tests** → still green. That's the point: tests let you refactor safely.

---

## Step 6 — Prove it's faster

Add a quick timing check (not a test, just exploration):

```python
import time

nums = list(range(10_000))
start = time.perf_counter()
two_sum(nums, 19_997)
print(time.perf_counter() - start)
```

Compare with the brute-force version. Feel the difference.

---

## Deliverable

- [ ] `exercises/two-sum/` with solution + parametrized tests
- [ ] `README.md` in the exercise explaining the approach + complexity
- [ ] Committed via a branch + PR
- [ ] `NOTES.md` reflection: what felt different about writing tests first?

---

## Checklist

- [ ] Wrote a failing test before the implementation
- [ ] Made it pass with the simplest code
- [ ] Improved complexity while keeping tests green
- [ ] Covered duplicates and negatives
- [ ] Committed via PR
