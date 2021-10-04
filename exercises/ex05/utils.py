"""List utility functions part 2."""

__author__ = "730470448"

# Define your functions below

def only_evens(l: list[int]) -> list[int]:
    l2: list[int] = []
    for i in l:
        if(i % 2 == 0):
            l2.append(i)
    return l2
        
print(only_evens([444,44,4]))


def sub(l: list[int], start: int, end: int):
    l2: list[int] = []
    i: int = start
    while i < end:
        l2.append(l[i])
        i = i + 1
    return l2
print(sub([10,20,30,40], 1, 3))

def concat(l: list[int], l2: list[int]):
    i: int = 0
    while i < len(l2):
        l.append(l2[i])
        i = i + 1
    return l

print(concat([1, 2, 3, 4],[6, 7, 8, 9]))