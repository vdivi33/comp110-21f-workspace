"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730470448"


def test_base_case_invert() -> None:
    """Follows an expected input to reverse key and value"""
    assert invert({'a': 'A', 'b': 'B'}) == {'A': 'a', 'B': 'b'}


def test_edge_case_invert() -> None:
    """Tests an obscure input where the key and value are the same"""
    assert invert({'a': 'a', 'b': 'b'}) == {'a': 'a', 'b': 'b'}


def test_base_case_invert2() -> None:
    """Tests another expected input to invert key and value"""
    assert invert({'a': 'b', 'c': 'd', 'e': 'f'}) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_base_case_favorite_color() -> None:
    """Tests a standard input that returns the favorite color."""
    assert favorite_color({"Marc": "yellow", "Jane": "yellow", "Bob": "yellow", "John": "green", "Tom": "green", "Ezri": "blue", "Kris": "blue", "Gary": "blue"}) == 'yellow'


def test_base_case_favorite_color2() -> None:
    """Tests another standard input for favorite color"""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_edge_case_favorite_color() -> None:
    """Tests an obscure inout where there is only one color choice. Returns that color."""
    assert favorite_color({"Marc": "yellow"}) == "yellow"


def test_base_case_count() -> None:
    """Tests an expected input which converts a list into a dictionary with each number having its own count."""
    assert count(["1", "2", "2", "1", "3"]) == {"1": 2, "2": 2, "3": 1}


def test_base_case_count2() -> None:
    """Tests another expected input which converts a list into a dictionary with each number having its own count."""
    assert count(["1", "1", "2", "1", "3", "5", "4", "3"]) == {"1": 3, "2": 1, "3": 2, "4": 1, "5": 1}


def test_edge_case_count() -> None:
    """Tests an empty list which outputs an empty dictionary"""
    assert count([]) == {}