# Module 05 — Stacks & queues

> ⏱ ~3h · 🎯 Model "last in" and "first in" behavior.

## Why this matters

Stacks and queues show up in parsing, scheduling, BFS, undo/redo, and expression evaluation. Recognizing when a problem is "last-in-first-out" is a big unlock.

---

## Core concepts

### Stack (LIFO)

```python
stack = []
stack.append(x)  # push, O(1)
stack.pop()  # pop, O(1) — removes the LAST
top = stack[-1]  # peek, O(1)
```

### Queue (FIFO)

```python
from collections import deque

q = deque()
q.append(x)  # enqueue, O(1)
q.popleft()  # dequeue, O(1) — removes the FIRST
```

Never use `list.pop(0)` as a queue — it's O(n).

### Classic uses

- **Stack:** balanced parentheses, reverse polish notation, DFS (iterative), monotonic stack (next greater element), undo history.
- **Queue:** BFS, task scheduling, sliding-window maximum (monotonic deque).

### Monotonic stack (important pattern)

Find the next greater element in O(n):

```python
def next_greater(a):
    res = [-1] * len(a)
    stack = []  # indices with decreasing values
    for i, x in enumerate(a):
        while stack and a[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res
```

### Balanced parentheses

```python
def is_balanced(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack
```

---

## Complexity cheat sheet

| Operation | Stack (list) | Queue (deque) |
|-----------|--------------|---------------|
| push/enqueue | O(1) | O(1) |
| pop/dequeue | O(1) | O(1) |
| peek | O(1) | O(1) |

---

## Common pitfalls

- `list.pop(0)` as a queue → O(n) per dequeue.
- Forgetting to check empty before `pop()`.
- Monotonic stack: getting the `<` vs `<=` wrong (duplicates).
- Confusing LIFO and FIFO when the problem is about order.

---

## Exercises

1. **Valid parentheses** — stack.
2. **Min stack** — O(1) `min()` via an auxiliary stack.
3. **Daily temperatures** — monotonic stack.
4. **Reverse polish notation** — evaluate with a stack.
5. **Implement queue with two stacks** — classic.
6. **Sliding window maximum** — monotonic deque.

---

## Paired workshop

[Workshop 04 — Debugging with pdb](../../workshops/04-debugging-with-pdb/README.md)

## Checklist

- [ ] Know when a problem is a stack problem
- [ ] Use `deque` for queues, never `list.pop(0)`
- [ ] Can implement a monotonic stack
- [ ] Test empty input and unmatched brackets
- [ ] Wrote 3 lines in `NOTES.md`
