"""List utility functions."""

__author__ = "123456789"

# TODO: Implement your functions here.


def all(list: list[int], match: int) -> bool:
    """Finds an integer in a list that matches a desired number. Returns True if found and returns False otherwise."""
    i: int = 0
    count: int = 0
    if(len(list) > 0):
        while i < len(list):
            if(list[i] == match):
                count = count + 1
            i = i + 1
        if(count == len(list)):
            return True
    return False


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Compares the elements of two lists and returns True if all the elements are the same."""
    i: int = 0
    j: int = 0
    count: int = 0
    if(len(list_one) < len(list_two)):
        while(i < len(list_one)):
            if(list_one[i] == list_two[j]):
                count = count + 1
            j = j + 1
            i = i + 1
    else:
        while(i < len(list_two)):
            if(list_one[i] == list_two[j]):
                count = count + 1
            j = j + 1
            i = i + 1
    print(count)
    if(count == len(list_one) and count == len(list_two)):
        return True
    return False


def max(input: list[int]) -> int:
    """Finds and returns the greatest integer in a list."""
    i: int = 1
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        max: int = input[0]
        while(i < len(input)):
            if(max < input[i]):
                max = input[i]
            i = i + 1
    return max

# print(is_equal([1,2,1,3,],[1,1,2,3]))