"""Tests for binary_search."""

import pytest

from .solution import binary_search


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([], 5, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([1, 2, 3, 4, 5], 1, 0),  # first index
        ([1, 2, 3, 4, 5], 5, 4),  # last index
        ([1, 2, 3, 4, 5], 6, -1),  # greater than max
        ([1, 2, 3, 4, 5], 0, -1),  # less than min
    ],
)
def test_binary_search(nums, target, expected):
    assert binary_search(nums, target) == expected
