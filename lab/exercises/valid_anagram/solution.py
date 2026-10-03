"""Valid Anagram — counting solution.

Approach:
    If lengths differ, it can't be an anagram. Otherwise count characters in
    `a`, then decrement while scanning `b`; any negative or leftover count
    means it's not an anagram.

Complexity:
    Time:  O(n)
    Space: O(k)  (k = alphabet size)
"""

from __future__ import annotations

from collections import Counter


def is_anagram(a: str, b: str) -> bool:
    """Return True if `b` is an anagram of `a` (case-sensitive)."""
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)
