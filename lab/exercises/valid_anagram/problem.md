# Valid Anagram

**Difficulty:** easy
**Topic:** strings, hash maps
**Source:** classic (LeetCode #242)

---

## Description

Given two strings `a` and `b`, return `True` if `b` is an anagram of `a` (same characters, same counts), else `False`.

Anagrams are case-sensitive here (treat `"A"` and `"a"` as different).

## Examples

```
Input:  a = "anagram", b = "nagaram"
Output: True
```

```
Input:  a = "rat", b = "car"
Output: False
```

```
Input:  a = "", b = ""
Output: True
```

## Constraints

- `0 <= len(a), len(b) <= 5 * 10^4`
- lowercase and uppercase letters

## Edge cases to consider

- both empty
- different lengths (immediate `False`)
- same letters, different counts
- unicode (decide and document behavior)

---

## Approach

Two options:

1. Sort both strings and compare — O(n log n), simple.
2. Count characters with a map and compare — O(n), preferred.

Complexity: Time O(n), Space O(k) where k is the alphabet size.
