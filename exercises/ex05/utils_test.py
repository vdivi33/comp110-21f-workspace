"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730470448"


def test_edge_case_evens_only1() -> None:
    assert only_evens([1, 3, 5, 7]) == []


def test_edge_case_evens_only2() -> None:
    assert only_evens([]) == []


def test_base_case_evens_only1() -> None:
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]


def test_base_case_evens_only2() -> None:
    assert only_evens([1, 6, 3, 8]) == [6, 8]


def test_edge_case_sub() -> None:
    assert sub([0], 0, 0) == []


def test_base_case_sub1() -> None:
    assert sub([1, 2, 3, 4, 5], 1, 3) == [2, 3]


def test_base_case_sub2() -> None:
    assert sub([1, 2, 3, 4, 5], 0, 5) == [1, 2, 3, 4, 5]


def test_edge_case_concat() -> None:
    assert concat([], []) == []


def test_base_case_concat1() -> None:
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_base_case_concat2() -> None:
    assert concat([1], [8, 9, 0]) == [1, 8, 9, 0]