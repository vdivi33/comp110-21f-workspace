"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730470448"


def test_edge_case_evens_only1() -> None:
    """Tests the only_evens function with only odds. Should return an empty list."""
    assert only_evens([1, 3, 5, 7]) == []


def test_edge_case_evens_only2() -> None:
    """Tests and empty list in the only_evens function. SHould return and empty list."""
    assert only_evens([]) == []


def test_base_case_evens_only1() -> None:
    """Tests a list containing both even and odd integers. Returns list with only evens."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]


def test_base_case_evens_only2() -> None:
    """Tests a list containing both even and odd integers. Returns list with only evens."""
    assert only_evens([1, 6, 3, 8]) == [6, 8]


def test_edge_case_sub() -> None:
    """Tests the sub function with a list length of 1 and an index from 0 to 0."""
    assert sub([0], 0, 0) == []


def test_base_case_sub1() -> None:
    """Tests the sub function with an index within the bounds of the list."""
    assert sub([1, 2, 3, 4, 5], 1, 3) == [2, 3]


def test_base_case_sub2() -> None:
    """Tests the sub function with an index within the bounds of the list."""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_edge_case_concat() -> None:
    """Concatenates two empty lists and returns an empty list."""
    assert concat([], []) == []


def test_base_case_concat1() -> None:
    """Concatenates 2 lists of the same length into one combined list."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_base_case_concat2() -> None:
    """Combines the elements of two distinct lists of integers."""
    assert concat([1], [8, 9, 0]) == [1, 8, 9, 0]