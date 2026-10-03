"""Two Sum — hash map solution.

Approach:
    Iterate once. Keep a map value -> index of elements seen so far. For each
    element x, check whether target - x is already in the map; if so, we have
    the pair. Otherwise record x and continue.

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices [i, j] (i < j) with nums[i] + nums[j] == target.

    Assumes exactly one solution exists.
    """
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
