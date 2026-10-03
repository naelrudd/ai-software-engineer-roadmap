# Two Sum

**Difficulty:** easy
**Topic:** arrays, hash maps
**Source:** classic (LeetCode #1)

---

## Description

Given a list of integers `nums` and an integer `target`, return the indices `[i, j]` with `i < j` such that `nums[i] + nums[j] == target`.

Exactly one solution exists. You may not use the same element twice.

## Examples

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] == 9
```

```
Input:  nums = [3, 3], target = 6
Output: [0, 1]
```

## Constraints

- `2 <= len(nums) <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- exactly one valid answer exists

## Edge cases to consider

- duplicates (`[3, 3]`)
- negative numbers (`[-1, -2, -3, -4]`)
- target formed by the last two elements
- large input (hint: O(n²) is too slow)

---

## Approach

Brute force checks every pair → O(n²). A hash map stores `value -> index` and, for each element, checks whether its complement (`target - x`) was seen → O(n).

Complexity: Time O(n), Space O(n).
