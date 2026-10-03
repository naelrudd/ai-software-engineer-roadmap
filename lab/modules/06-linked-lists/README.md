# Module 06 — Linked lists

> ⏱ ~4h · 🎯 Master pointer manipulation without losing the list.

## Why this matters

Linked lists train pointer discipline and the two-pointer/dummy-node techniques. They also appear in real code (LRU caches, adjacency lists) and interviews.

---

## Core concepts

### Node & list

```python
from __future__ import annotations


@dataclass
class Node:
    val: int
    next: Node | None = None
```

### Traversal

```python
cur = head
while cur:
    print(cur.val)
    cur = cur.next
```

### Dummy node trick

Removes special-casing at the head:

```python
dummy = Node(0, head)
prev = dummy
# ... modify prev.next ...
return dummy.next
```

### Reversal (know this cold)

```python
def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```

### Fast & slow pointers

Find the middle, detect cycles (Floyd's algorithm):

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

### Merge two sorted lists

```python
def merge(a, b):
    dummy = Node(0)
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next
```

---

## Common pitfalls

- Losing the rest of the list: save `cur.next` **before** rewiring.
- Off-by-one in "nth from end" (use two pointers n apart).
- Not handling empty list / single node.
- Infinite loops from a cycle you didn't detect.
- Comparing nodes with `==` instead of `is` when identity matters.

---

## Exercises

1. **Reverse a linked list** — iterative and recursive.
2. **Merge two sorted lists** — dummy node.
3. **Middle of the list** — fast/slow.
4. **Detect cycle** — Floyd's.
5. **Remove nth node from end** — two pointers.
6. **Palindrome linked list** — reverse second half.

---

## Paired workshop

[Workshop 04 — Debugging with pdb](../../workshops/04-debugging-with-pdb/README.md)

## Checklist

- [ ] Can reverse a list without bugs
- [ ] Use a dummy node to simplify head operations
- [ ] Can detect a cycle with fast/slow pointers
- [ ] Test empty, single, and even/odd lengths
- [ ] Wrote 3 lines in `NOTES.md`
