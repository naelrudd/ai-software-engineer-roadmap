# Module 08 — Sorting & searching

> ⏱ ~4h · 🎯 Understand what `sort()` really does, and sort things yourself once.

## Why this matters

Sorting is a prerequisite for binary search, two pointers, and many greedy algorithms. Implementing the classics once builds intuition for complexity and stability.

---

## Core concepts

### The comparison sorts

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | no |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | no |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | no |

Python's `sorted()` / `list.sort()` uses Timsort: O(n log n), stable.

### Stable vs unstable

Stable = equal elements keep their original order. Matters when sorting by multiple keys.

### Merge sort (divide & conquer)

```python
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


def merge(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out
```

### Python sorting tips

```python
sorted(items, key=lambda x: x.score)  # ascending
sorted(items, key=lambda x: -x.score)  # descending
sorted(items, key=lambda x: (x.grade, x.name))  # multi-key
sorted(items, key=len)  # by length
```

`key` is computed once per element — always prefer it over `cmp`-style hacks.

---

## Common pitfalls

- Quicksort worst case O(n²) on sorted input with bad pivot choice.
- Assuming a sort is stable when it isn't.
- Sorting repeatedly when one sort + a pass would do.
- Using `list.sort()` expecting a return value (it returns `None`, sorts in place).
- Comparing incomparable types (raises `TypeError`).

---

## Exercises

1. Implement **bubble, insertion, selection** sorts; test on edge cases.
2. Implement **merge sort**; verify stability with tuples.
3. Implement **quicksort**; analyze worst case.
4. Sort by **multiple keys** (grade desc, name asc).
5. **Merge two sorted arrays** in place.
6. **Sort colors** (Dutch national flag) — three-way partition.

---

## Paired workshop

[Workshop 05 — Profile & optimize](../../workshops/05-profile-and-optimize/README.md)

## Checklist

- [ ] Can implement merge sort from memory
- [ ] Know the complexity table
- [ ] Understand stability
- [ ] Use `key=` correctly for multi-key sorts
- [ ] Wrote 3 lines in `NOTES.md`
