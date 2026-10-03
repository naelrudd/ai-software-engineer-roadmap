# Module 10 — Trees

> ⏱ ~4h · 🎯 Traverse hierarchies fluently, recursively and iteratively.

## Why this matters

Trees model hierarchies (file systems, DOM, parse trees, decision trees) and appear constantly in interviews. Binary search trees power ordered maps; heaps power priority queues.

---

## Core concepts

### Binary tree node

```python
from __future__ import annotations


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None
```

### Traversals

- **DFS preorder** (node, left, right) — copy/serialize.
- **DFS inorder** (left, node, right) — sorted order in a BST.
- **DFS postorder** (left, right, node) — compute aggregates.
- **BFS / level order** — queue; shortest path in unweighted trees.

```python
def inorder(node, out):
    if not node:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)
```

### Recursion pattern

Most tree problems: "solve for left, solve for right, combine at node."

```python
def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

### Binary search tree (BST)

Invariant: `left < node < right` (strictly, for distinct keys).

```python
def search_bst(node, target):
    while node:
        if target == node.val:
            return node
        node = node.left if target < node.val else node.right
    return None
```

Search/insert/delete are O(h); balanced `h = log n`, skewed `h = n`.

### Iterative traversal

Use an explicit stack to avoid recursion limits.

---

## Complexity

| Operation | Balanced | Skewed |
|-----------|----------|--------|
| search/insert/delete | O(log n) | O(n) |
| traversal | O(n) | O(n) |

---

## Common pitfalls

- Base case `if not node` returning wrong value.
- Confusing preorder/inorder/postorder.
- Assuming a tree is balanced.
- BST invariant violated by using `<=` carelessly.
- Recursion depth on a skewed tree.

---

## Exercises

1. **Max depth / min depth**.
2. **Invert a binary tree**.
3. **Same tree / symmetric tree**.
4. **Level order traversal** — BFS.
5. **Validate BST** — with min/max bounds.
6. **Lowest common ancestor**.

---

## Paired workshop

[Workshop 06 — Code review](../../workshops/06-code-review/README.md)

## Checklist

- [ ] Can write all four traversals
- [ ] Understand the BST invariant
- [ ] Can convert recursion to an explicit stack
- [ ] Test null, single node, skewed tree
- [ ] Wrote 3 lines in `NOTES.md`
