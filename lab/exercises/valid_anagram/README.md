# Valid Anagram

## What I learned

`Counter` equality is a clean O(n) anagram check. The length pre-check is a cheap early exit that also prevents false positives from count mismatches.

## Approach & complexity

- Approach: `Counter(a) == Counter(b)`, after a length check.
- Time: O(n)
- Space: O(k)

## What tripped me up

- Assuming anagrams are case-insensitive — they aren't unless specified.
- Using `==` vs `is` on booleans in tests (here `is` is fine because we return literals).

## Tests

Covered:
- [x] examples
- [x] both empty
- [x] different lengths
- [x] case sensitivity
- [x] repeated characters
