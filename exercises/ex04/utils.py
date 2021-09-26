"""List utility functions."""

__author__ = "123456789"

l = [1,2,3,4]
l2 = [1,1,1,1]
# TODO: Implement your functions here.


def all(list, match: int) -> bool:
    int i = 0
    int count = 0
    while i < len(list):
        if(list[i] == match):
            count+=count
    if(count == len(list)):
        return True
    return False

print(all(l, 1))
print(all(l2, 1))
