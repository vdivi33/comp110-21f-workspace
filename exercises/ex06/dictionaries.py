"""Practice with dictionaries."""

__author__ = "730470448"


def invert(d) -> dict[str,str]:
    inverted: dict[str,str]
    inverted = dict()
    for i in d:
        inverted[inverted[i]] = i
    return inverted

print(invert({'a':1, 'b':2, 'c':3}))

# Define your functions below