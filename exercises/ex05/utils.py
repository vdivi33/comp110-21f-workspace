"""List utility functions part 2."""

__author__ = "730470448"

# Define your functions below


def only_evens(lis: list[int]) -> list[int]:
    l2: list[int] = []
    for i in lis:
        if(i % 2 == 0):
            l2.append(i)
    return l2
        

def sub(lis: list[int], start: int, end: int):
    l2: list[int] = []
    if(start >= 0 and start <= len(lis) and end <= len(lis) and len(lis) > 0):
        i: int = start
        while i < end:
            l2.append(lis[i])
            i = i + 1
        return l2


def concat(lis: list[int], l2: list[int]):
    i: int = 0
    while i < len(l2):
        lis.append(l2[i])
        i = i + 1
    return lis