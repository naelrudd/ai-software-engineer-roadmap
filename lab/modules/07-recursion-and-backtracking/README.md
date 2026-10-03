# Module 07 — Recursion & backtracking

> ⏱ ~4h · 🎯 Think in subproblems and explore choices systematically.

## Why this matters

Recursion is the gateway to trees, graphs, and dynamic programming. Backtracking is how you enumerate all valid solutions (permutations, subsets, N-Queens).

---

## Core concepts

### Anatomy of recursion

Every recursive function needs:
1. **Base case** — when to stop.
2. **Recursive case** — reduce the problem.
3. **Progress** — each call must move toward the base case.

```python
def factorial(n):
    if n <= 1:  # base
        return 1
    return n * factorial(n - 1)  # reduce
```

### The call stack

Each call adds a frame. Depth `d` → O(d) space. Deep recursion can overflow; convert to iteration or increase the limit (rarely the right fix).

### Recursion vs iteration

Anything recursive can be iterative (with an explicit stack). Recursion is often clearer for trees/divide-and-conquer.

### Backtracking template

```python
def backtrack(path, choices, result):
    if is_solution(path):
        result.append(path.copy())
        return
    for choice in choices:
        if is_valid(choice, path):
            path.append(choice)  # choose
            backtrack(path, next_choices(choice), result)
            path.pop()  # un-choose
```

### Subsets / permutations / combinations

- Subsets: include/exclude each element → O(2ⁿ).
- Permutations: choose each remaining element → O(n!).
- Combinations: choose, then recurse on the rest.

### Divide and conquer

Merge sort, quicksort, binary search — split, solve, combine.

---

## Complexity

| Problem | Time |
|---------|------|
| subsets | O(2ⁿ) |
| permutations | O(n!) |
| recursion depth | O(depth) space |

---

## Common pitfalls

- Missing or wrong base case → infinite recursion.
- Not copying `path` when appending to results (aliasing bug).
- Forgetting to **undo** the choice after recursing.
- Mutating shared state and not restoring it.
- Ignoring pruning — backtracking without bounds explodes.

---

## Exercises

1. **Factorial / Fibonacci** — recursive, then compare with iterative.
2. **Generate all subsets** — power set.
3. **Generate permutations** — with backtracking.
4. **Combination sum** — with pruning.
5. **N-Queens** — validity check + backtrack.
6. **Word search** — grid + backtracking.

---

## Paired workshop

[Workshop 02 — TDD your first solution](../../workshops/02-tdd-your-first-solution/README.md)

## Checklist

- [ ] Always identify the base case first
- [ ] Copy mutable state when storing results
- [ ] Remember to undo choices
- [ ] Can state the recursion's complexity
- [ ] Wrote 3 lines in `NOTES.md`
