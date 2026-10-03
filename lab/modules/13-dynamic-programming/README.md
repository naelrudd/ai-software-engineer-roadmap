# Module 13 — Dynamic programming

> ⏱ ~5h · 🎯 Turn exponential recursion into polynomial by remembering.

## Why this matters

DP is the hardest common interview topic and the most rewarding. It's recursion + memoization: solve each subproblem once, reuse it.

---

## Core concepts

### Two flavors

- **Top-down (memoization):** recursive + cache.
- **Bottom-up (tabulation):** iterative table.

Both are valid. Start top-down to get correctness, then optimize.

### When DP applies

1. **Optimal substructure** — the answer builds from subproblem answers.
2. **Overlapping subproblems** — the same subproblem recurs.

### Top-down template

```python
from functools import lru_cache


def fib(n):
    @lru_cache(maxsize=None)
    def f(k):
        if k < 2:
            return k
        return f(k - 1) + f(k - 2)

    return f(n)
```

### Bottom-up template

```python
def fib(n):
    if n < 2:
        return n
    prev, cur = 0, 1
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur
    return cur
```

### Classic families

- **1D:** climbing stairs, house robber, coin change.
- **2D grid:** unique paths, min path sum.
- **Subsequence:** longest common subsequence, edit distance.
- **Knapsack:** 0/1 knapsack, subset sum.
- **Interval:** longest palindromic substring.

### State design (the real skill)

Define what the state means before coding. Example, coin change:

```python
# dp[amount] = min coins to make `amount`
dp = [0] + [float("inf")] * amount
for a in range(1, amount + 1):
    for c in coins:
        if c <= a:
            dp[a] = min(dp[a], dp[a - c] + 1)
return dp[amount] if dp[amount] != float("inf") else -1
```

### Space optimization

Many 2D DPs only need the previous row — reduce O(n·m) space to O(m).

---

## Complexity

Usually `states × work per state`. E.g. coin change: O(amount × coins).

---

## Common pitfalls

- Forgetting `@lru_cache` arguments must be hashable.
- Wrong base cases.
- Wrong state definition → wrong transitions.
- Off-by-one in table dimensions.
- Using DP when a greedy solution works (and is simpler).

---

## Exercises

1. **Climbing stairs** — 1D.
2. **House robber** — 1D with a choice.
3. **Coin change** — min coins.
4. **Longest common subsequence** — 2D.
5. **Edit distance** — 2D.
6. **0/1 knapsack** — 2D → 1D optimization.

---

## Paired workshop

[Workshop 07 — Evaluate an AI solution](../../workshops/07-evaluate-an-ai-solution/README.md)

## Checklist

- [ ] Can identify overlapping subproblems
- [ ] Can write both top-down and bottom-up
- [ ] Define the state in one sentence before coding
- [ ] Know when greedy beats DP
- [ ] Wrote 3 lines in `NOTES.md`
