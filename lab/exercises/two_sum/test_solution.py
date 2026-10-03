"""Tests for two_sum."""

import pytest

from .solution import two_sum


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4], -7, [2, 3]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1, 2], 3, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected


def test_returns_indices_in_order():
    result = two_sum([2, 7, 11, 15], 9)
    assert result[0] < result[1]
