"""Practice with dictionaries."""

__author__ = "730470448"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary input of two strings and switches each key and value."""
    inverted: dict[str, str]
    inverted = dict()
    for i in d:
        if(d[i] in inverted):
            raise KeyError("Duplicate Keys")
        inverted[d[i]] = i
    return inverted


def favorite_color(color_dict: dict[str, str]) -> str:
    """Takes in a dict[str, str] argument and returns a string of the most common color among the values."""
    count: int = 0
    color_set: dict[str, int]
    color_set = dict()
    color_set["Blank"] = 0
    greatest: str = "Blank"
    for i in color_dict:
        for j in color_dict:
            if(color_dict[j] == color_dict[i]):
                count += 1
        color_set[color_dict[i]] = count
        count = 0
    for y in color_set:
        if(color_set[greatest] < color_set[y]):
            greatest = y
    return greatest


def count(lis: list[str]) -> dict[str, int]:
    """Takes in a list[int] argument and returns a dictionary with the count of each integer in the list."""
    d: dict[str, int]
    d = dict()
    for i in lis:
        if(str(i) in d):
            d[str(i)] += 1
        else:
            d[str(i)] = 1
    return d
# Define your functions below