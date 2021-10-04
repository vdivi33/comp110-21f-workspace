"""List utility functions part 2."""

__author__ = "730470448"

# Define your functions below


def only_evens(lis: list[int]) -> list[int]:
    """Given a list of integers, this function returns a list containing only even elements."""
    l2: list[int] = []
    for i in lis:
        if(i % 2 == 0):
            l2.append(i)
    return l2
        

def sub(lis: list[int], start: int, end: int):
    """Finds a specified portion of a list defined between two bounds."""
    l2: list[int] = []
    if(start < 0):
        start = 0
    if(start >= len(lis)):
        return l2
    if(end > len(lis)):
        end = len(lis)
    if(len(lis) == 0):
        return l2
    if(start >= 0 and start <= len(lis) and end <= len(lis) and len(lis) > 0):
        i: int = start
        while i < end:
            l2.append(lis[i])
            i = i + 1
        return l2


def concat(lis: list[int], l2: list[int]):
    """Merges two lists into one."""
    i: int = 0
    while i < len(l2):
        lis.append(l2[i])
        i = i + 1
    return lis