"""Tests for is_anagram."""

import pytest

from .solution import is_anagram


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "a", False),
        ("Listen", "Silent", False),  # case-sensitive
        ("aaab", "abaa", True),
    ],
)
def test_is_anagram(a, b, expected):
    assert is_anagram(a, b) is expected
