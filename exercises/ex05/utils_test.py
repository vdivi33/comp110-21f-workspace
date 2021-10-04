"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens

__author__ = "730470448"


def only_evens_test_onlyOdds() -> None:
    assert only_evens([1,3,5,7]) == []


def only_evens_test_empty() -> None:
    assert only_evens([]) == []


def only_evens_test_normal() -> None:
    assert only_evens([1,2,3,4,5,6,7,8]) == [2,4,6,8]