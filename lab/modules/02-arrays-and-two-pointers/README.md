# Module 02 — Arrays & two pointers

> ⏱ ~4h · 🎯 Master the most common interview pattern.

## Why this matters

Arrays are the base of almost everything. Two pointers and prefix sums solve a huge class of problems in O(n) instead of O(n²).

---

## Core concepts

### Array basics in Python

```python
a = [1, 2, 3]
a.append(4)  # O(1) amortized
a.pop()  # O(1)
a.insert(0, 0)  # O(n) — shifts everything
a[1:3]  # O(k) — creates a copy
```

Lists are dynamic arrays: indexing is O(1), inserting/removing in the middle is O(n).

### Two pointers

Use when the array is **sorted** or you can process from both ends.

```python
def two_sum_sorted(a, target):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        s = a[lo] + a[hi]
        if s == target:
            return [lo, hi]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return []
```

### Same-direction (fast/slow) pointers

```python
def remove_duplicates(a):
    if not a:
        return 0
    write = 1
    for read in range(1, len(a)):
        if a[read] != a[write - 1]:
            a[write] = a[read]
            write += 1
    return write
```

### Prefix sums

Precompute cumulative sums to answer range-sum queries in O(1).

```python
prefix = [0]
for x in a:
    prefix.append(prefix[-1] + x)
# sum of a[i:j] == prefix[j] - prefix[i]
```

### In-place vs extra space

Ask: can I do it with O(1) extra space? Often yes, using pointers.

---

## Complexity cheat sheet

| Operation | List |
|-----------|------|
| index `a[i]` | O(1) |
| append / pop end | O(1) |
| insert / pop front | O(n) |
| search `x in a` | O(n) |
| slice `a[i:j]` | O(j-i) |

---

## Common pitfalls

- Off-by-one at boundaries (`lo < hi` vs `lo <= hi`).
- Forgetting the array may be empty or length 1.
- Using two pointers on an **unsorted** array when order matters.
- Creating new lists inside a loop (hidden O(n²)).
- Mutating while iterating.

---

## Exercises

1. **Two-sum (sorted)** — two pointers, O(n).
2. **Two-sum (unsorted)** — hash map, O(n). (Compare the two approaches.)
3. **Reverse in place** — O(1) space.
4. **Move zeroes** — stable, in place.
5. **Container with most water** — two pointers, prove why it's correct.
6. **Range sum query** — build prefix sums, answer O(1).

---

## Paired workshop

[Workshop 02 — TDD your first solution](../../workshops/02-tdd-your-first-solution/README.md)

## Checklist

- [ ] Can apply two pointers to sorted-array problems
- [ ] Can choose between hash map and two pointers
- [ ] Understand prefix sums
- [ ] Handle empty/single/duplicate edge cases in tests
- [ ] Wrote 3 lines in `NOTES.md`
