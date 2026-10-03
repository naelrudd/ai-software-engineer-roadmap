"""Binary Search — half-open interval [lo, hi).

Approach:
    Keep the answer inside [lo, hi). Compare the middle element and discard
    the half that cannot contain the target. Loop until the range is empty.

Complexity:
    Time:  O(log n)
    Space: O(1)
"""

from __future__ import annotations


def binary_search(nums: list[int], target: int) -> int:
    """Return the index of `target` in sorted `nums`, or -1 if absent."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return -1
