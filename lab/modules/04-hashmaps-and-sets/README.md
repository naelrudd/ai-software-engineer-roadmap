# Module 04 — Hash maps & sets

> ⏱ ~4h · 🎯 Turn O(n²) into O(n) by trading memory.

## Why this matters

The hash map is the single most useful tool for making code fast. "Have I seen this before?" and "how many times?" are answered in O(1).

---

## Core concepts

### Dict & set

```python
counts = {}
counts[x] = counts.get(x, 0) + 1  # count occurrences

seen = set()
if x in seen:  # O(1) average
    ...

seen.add(x)
```

### `defaultdict` and `Counter`

```python
from collections import defaultdict, Counter

groups = defaultdict(list)
for word in words:
    groups["".join(sorted(word))].append(word)

freq = Counter("aabbb")  # {'b': 3, 'a': 2}
```

### How hashing works (conceptually)

A hash function maps a key → bucket index. Collisions are resolved (chaining or open addressing). Average O(1); worst case O(n) with adversarial keys. Keys must be **hashable** (immutable: int, str, tuple — not list, dict, set).

### The "seen" pattern

```python
def contains_duplicate(a):
    seen = set()
    for x in a:
        if x in seen:
            return True
        seen.add(x)
    return False
```

### The "complement" pattern

```python
def two_sum(a, target):
    seen = {}  # value -> index
    for i, x in enumerate(a):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```

### Grouping pattern

Group items by a computed key (sorted string, tuple, mod, etc.).

---

## Complexity cheat sheet

| Operation | Average | Worst |
|-----------|---------|-------|
| lookup / insert / delete | O(1) | O(n) |
| iterate | O(n) | O(n) |

Space: O(n) for the map/set.

---

## Common pitfalls

- Using a list where a set is needed (`x in list` is O(n)).
- Unhashable keys (list/dict) → use tuples instead.
- Relying on dict ordering for logic.
- Forgetting that hashing mutable objects breaks lookups.
- Assuming O(1) always — worst case is O(n) under collisions.

---

## Exercises

1. **Contains duplicate** — set, O(n).
2. **Two-sum** — complement map, O(n).
3. **Group anagrams** — key = sorted word.
4. **Top K frequent** — Counter + heap or sort.
5. **Longest consecutive sequence** — set + walk.
6. **Subarray sum equals K** — prefix sum + map.

---

## Paired workshop

[Workshop 02 — TDD your first solution](../../workshops/02-tdd-your-first-solution/README.md)

## Checklist

- [ ] Reach for a set/dict to avoid nested loops
- [ ] Know what makes a key hashable
- [ ] Comfortable with `Counter` and `defaultdict`
- [ ] Can explain the complement pattern
- [ ] Wrote 3 lines in `NOTES.md`
