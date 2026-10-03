# Module 09 — Binary search

> ⏱ ~3h · 🎯 Halve the search space without an off-by-one.

## Why this matters

Binary search is O(log n) and shows up far beyond "find a number": rotated arrays, boundaries, "smallest value that satisfies a condition", and answer-space search.

---

## Core concepts

### The invariant

Keep a range `[lo, hi)` and maintain that the answer is inside it. Halve until the range is empty.

```python
def binary_search(a, target):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return -1
```

### The three boundary variants

- **First index where `a[i] >= x`** (lower bound).
- **First index where `a[i] > x`** (upper bound).
- **Last index where `a[i] <= x`**.

Getting these right is 80% of binary-search bugs.

### Binary search on the answer

Instead of searching an array, search the answer space when a predicate is monotonic.

```python
def min_capacity(weights, days):
    def feasible(cap):
        # can we ship within `days` with capacity `cap`?
        ...

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

### Template discipline

Pick **one** template and reuse it. Most bugs come from mixing `[lo, hi]` and `[lo, hi)` styles.

---

## Complexity

| | Time | Space |
|---|---|---|
| binary search | O(log n) | O(1) |

---

## Common pitfalls

- `mid = (lo + hi) // 2` overflow (irrelevant in Python, matters in C/Go).
- Infinite loop when `lo`/`hi` don't strictly shrink.
- Using `<=` vs `<` inconsistently.
- Searching an unsorted array.
- Forgetting the target may be absent.

---

## Exercises

1. **Classic search** — return index or -1.
2. **First/last occurrence** — lower/upper bound.
3. **Search insert position**.
4. **Search in rotated sorted array**.
5. **Find minimum in rotated array**.
6. **Koko eating bananas / ship packages** — binary search on the answer.

---

## Paired workshop

[Workshop 03 — Fixtures & parametrize](../../workshops/03-fixtures-and-parametrize/README.md)

## Checklist

- [ ] Can write the `[lo, hi)` template without bugs
- [ ] Can do lower/upper bound
- [ ] Understand binary search on the answer
- [ ] Test: empty, single, absent, duplicates
- [ ] Wrote 3 lines in `NOTES.md`
