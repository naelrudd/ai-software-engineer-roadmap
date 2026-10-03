# Binary Search

**Difficulty:** easy
**Topic:** arrays, binary search
**Source:** classic (LeetCode #704)

---

## Description

Given a sorted list of integers `nums` (ascending, distinct) and an integer `target`, return the index of `target` or `-1` if absent.

Must run in O(log n).

## Examples

```
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

```
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
```

## Constraints

- `1 <= len(nums) <= 10^4`
- `nums` is sorted ascending
- all values distinct

## Edge cases to consider

- empty list
- single element (present / absent)
- target at first or last index
- target absent

---

## Approach

Maintain the invariant `[lo, hi)`. Each step halves the range. Never mix `[lo, hi]` with `[lo, hi)` conventions — that's where off-by-one bugs come from.

Complexity: Time O(log n), Space O(1).
