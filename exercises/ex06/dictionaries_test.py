"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730470448"

def test_base_case_invert() -> None:
    assert invert({'a' : 'A', 'b' : 'B'}) == {'A' : 'a', 'B' : 'b'}

def test_edge_case_invert() -> None:
    assert invert({'a' : 'a', 'b' : 'b'}) == {'a' : 'a', 'b' : 'b'}

def test_base_case_invert2() -> None:
    assert invert({'a' : 'b', 'c' : 'd', 'e' : 'f'}) == {'b' : 'a', 'd' : 'c', 'f' : 'e'}

def test_base_case_favorite_color() -> None:
    assert favorite_color({"Marc": "yellow","Jane" : "yellow","Bob":"yellow", "John" : "green", "Tom": "green", "Ezri": "blue", "Kris": "blue","Gary":"blue"}) == 'yellow'

def test_base_case_favorite_color2() -> None:
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"

def test_edge_case_favorite_color() -> None:
    assert favorite_color("Marc":"yellow") == "yellow"