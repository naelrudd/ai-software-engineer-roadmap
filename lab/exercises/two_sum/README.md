# Two Sum

## What I learned

The hash map trades O(n) memory for O(n) time by answering "have I seen the complement?" in O(1). This "complement lookup" pattern generalizes to many sum/sequence problems.

## Approach & complexity

- Approach: one pass, store `value -> index`, look up `target - x`.
- Time: O(n)
- Space: O(n)

## What tripped me up

- Returning `[j, i]` instead of `[i, j]` when the complement is found first.
- Forgetting duplicates are fine because we insert only after checking.

## Tests

Covered:
- [x] example cases
- [x] duplicates (`[3, 3]`)
- [x] negatives
- [x] zero target
- [x] minimum length
