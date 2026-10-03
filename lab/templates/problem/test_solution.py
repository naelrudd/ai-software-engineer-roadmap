"""Tests for <problem name>.

Write tests FIRST when you can (TDD). Cover:
    - the provided examples
    - at least one edge case (empty, single, duplicates, negatives)
"""

import pytest

from .solution import solve


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 3], 6, [0, 1]),
        # add edge cases here
    ],
)
def test_solve(nums, target, expected):
    assert solve(nums, target) == expected


def test_edge_case_empty():
    # e.g. solve([], 0) should raise or return a defined value — decide and assert it
    ...
