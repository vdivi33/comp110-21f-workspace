"""An exercise in remainders and boolean logic."""

__author__ = "730470448"


# Begin your solution here...
integer: int = int(input("Enter an int: "))

if integer % 2 == 0:
    if integer % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if(integer % 7 == 0):
        print("HEELS")
    else:
        print("CAROLINA")
