# Module 11 — Heaps & priority queues

> ⏱ ~3h · 🎯 Always have the min (or max) ready in O(log n).

## Why this matters

Heaps give O(1) access to the min/max and O(log n) insert/remove. They power schedulers, Dijkstra, top-K problems, and streaming medians.

---

## Core concepts

### `heapq` (min-heap)

```python
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)
heapq.heappop(h)  # 1
h[0]  # smallest, O(1)
```

### Max-heap trick

Python has no max-heap; push negated values.

```python
heapq.heappush(h, -x)  # then -heapq.heappop(h) gives the max
```

### `heapify` in O(n)

```python
a = [3, 1, 2]
heapq.heapify(a)  # O(n), faster than n pushes
```

### Top-K pattern

Keep a size-K heap while streaming:

```python
def top_k(nums, k):
    h = nums[:k]
    heapq.heapify(h)
    for x in nums[k:]:
        if x > h[0]:
            heapq.heapreplace(h, x)
    return h
```

### Heap of tuples

`heapq` compares tuples lexicographically — great for `(priority, item)` and tie-breaking with a counter.

### Two-heaps (streaming median)

Maintain a max-heap for the lower half and a min-heap for the upper half; rebalance so their sizes differ by ≤ 1.

---

## Complexity

| Operation | Time |
|-----------|------|
| peek min | O(1) |
| push / pop | O(log n) |
| heapify | O(n) |
| build by n pushes | O(n log n) |

---

## Common pitfalls

- Forgetting to negate for a max-heap.
- Comparing unorderable items in a heap of tuples (add a tie-break counter).
- Using a sorted list instead of a heap when data streams.
- `heapify` on an already-heapified list (harmless but pointless).
- Assuming `heapq` is stable — it isn't.

---

## Exercises

1. **Kth largest element** — size-K min-heap.
2. **Top K frequent** — Counter + heap.
3. **Merge K sorted lists** — heap of heads.
4. **Last stone weight** — max-heap via negation.
5. **Streaming median** — two heaps.
6. **Task scheduler / Dijkstra preview** — priority queue.

---

## Paired workshop

[Workshop 06 — Code review](../../workshops/06-code-review/README.md)

## Checklist

- [ ] Know `heapq` API and the negation trick
- [ ] Can solve top-K with a bounded heap
- [ ] Understand heapify vs repeated push
- [ ] Test k=1, k=n, duplicates
- [ ] Wrote 3 lines in `NOTES.md`
