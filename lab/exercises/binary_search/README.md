# Binary Search

## What I learned

The half-open interval `[lo, hi)` removes the ambiguity of `hi = mid` vs `hi = mid - 1`. Pick one convention and never mix it.

## Approach & complexity

- Approach: `[lo, hi)`, halve each step.
- Time: O(log n)
- Space: O(1)

## What tripped me up

- Using `while lo <= hi` with a half-open interval → out-of-bounds `mid`.
- Forgetting that `nums` may be empty.
- Not testing the last element (the classic missed case).

## Tests

Covered:
- [x] examples
- [x] empty list
- [x] single element (present/absent)
- [x] first and last index
- [x] target out of range
