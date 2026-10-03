# Module 01 — Complexity & Big-O

> ⏱ ~3h · 🎯 Predict how code scales before you run it.

## Why this matters

Big-O is how engineers talk about "will this survive real data?". It's the difference between a solution that works on 10 items and one that works on 10 million.

---

## Core concepts

Big-O describes how runtime/memory grows as input `n` grows, ignoring constants.

| Complexity | Name | Example |
|-----------|------|---------|
| O(1) | constant | dict lookup, `arr[i]` |
| O(log n) | logarithmic | binary search |
| O(n) | linear | one pass over a list |
| O(n log n) | linearithmic | good sorting |
| O(n²) | quadratic | nested loops over same data |
| O(2ⁿ) | exponential | naive subsets/recursion |
| O(n!) | factorial | naive permutations |

### Counting operations

```python
def has_duplicates(a):
    for i in range(len(a)):  # n iterations
        for j in range(i + 1, len(a)):  # ~n each
            if a[i] == a[j]:
                return True
    return False


# O(n^2)
```

vs.

```python
def has_duplicates(a):
    seen = set()
    for x in a:  # n iterations
        if x in seen:  # O(1) average
            return True
        seen.add(x)
    return False


# O(n) time, O(n) space
```

This trade — time for space — is the central theme of algorithms.

### Best / average / worst case

- Best: luckiest input.
- Worst: input that forces maximum work (usually what we quote).
- Average: expected over random inputs.

Quote worst case unless told otherwise.

### Space complexity

Count extra memory beyond the input. Recursion uses stack space: depth `d` → O(d).

### Rules of thumb

- Drop constants: O(2n) = O(n).
- Keep the dominant term: O(n² + n) = O(n²).
- Sequential loops add; nested loops multiply.
- Halving each step → O(log n).

---

## Common pitfalls

- Hidden loops: `x in list` is O(n); `x in set` is O(1). `list.insert(0, x)` is O(n).
- String concatenation in a loop is O(n²) in some languages; in Python prefer `"".join(parts)`.
- Recursion depth can blow the stack; convert to iterative when needed.
- Nested comprehensions are still nested loops.
- Sorting inside a loop → O(n² log n) surprises.

---

## Exercises

1. For 5 snippets (given in the workshop), write the time and space complexity and justify it.
2. Implement `has_duplicates` both ways (O(n²) and O(n)); benchmark on n = 1k, 10k.
3. Given `sum_of_all_pairs(a)`, prove its complexity and propose a faster version.
4. Analyze the space complexity of a recursive Fibonacci.
5. Take a solution you wrote earlier and improve its Big-O; note the trade-off.

---

## Paired workshop

[Workshop 05 — Profile & optimize](../../workshops/05-profile-and-optimize/README.md)

## Checklist

- [ ] Can read a function and state its time complexity
- [ ] Know the cost of common operations (list vs set vs dict)
- [ ] Understand time-vs-space trade-offs
- [ ] Can improve a brute-force solution's complexity
- [ ] Wrote 3 lines in `NOTES.md`
