# Module 14 — Sliding window

> ⏱ ~3h · 🎯 Scan subarrays/substrings in O(n) instead of O(n²).

## Why this matters

Sliding window turns "check every subarray" into a single pass. It's a top interview pattern for strings, arrays, and streaming.

---

## Core concepts

### Fixed-size window

```python
def max_sum_k(a, k):
    window = sum(a[:k])
    best = window
    for i in range(k, len(a)):
        window += a[i] - a[i - k]  # add new, drop old
        best = max(best, window)
    return best
```

### Variable-size window

Grow the window with `right`; shrink from `left` when a constraint is violated.

```python
def longest_unique_substring(s):
    last = {}
    left = 0
    best = 0
    for right, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = right
        best = max(best, right - left + 1)
    return best
```

### The template

```python
left = 0
for right in range(len(a)):
    add(a[right])
    while not valid():
        remove(a[left])
        left += 1
    update_answer()
```

### When it applies

- Contiguous subarray/substring.
- A monotonic constraint (e.g. "at most K distinct", "sum ≥ target").
- You can add/remove elements incrementally.

If the constraint isn't monotonic, a plain sliding window won't work.

---

## Complexity

O(n) time (each element enters and leaves the window once), O(k) space for the window state.

---

## Common pitfalls

- Shrinking with `if` instead of `while` (window may stay invalid).
- Forgetting to update `left` correctly on duplicates.
- Applying window to non-contiguous problems.
- Recomputing window sums from scratch each step → O(n²).

---

## Exercises

1. **Maximum sum subarray of size K**.
2. **Longest substring without repeating characters**.
3. **Minimum window substring**.
4. **Longest substring with at most K distinct characters**.
5. **Fruit into baskets** (same as #4).
6. **Permutation in string** — fixed window + counts.

---

## Paired workshop

[Workshop 05 — Profile & optimize](../../workshops/05-profile-and-optimize/README.md)

## Checklist

- [ ] Can write the variable-window template
- [ ] Know `while` vs `if` for shrinking
- [ ] Can state why it's O(n)
- [ ] Test empty, all-same, all-distinct
- [ ] Wrote 3 lines in `NOTES.md`
