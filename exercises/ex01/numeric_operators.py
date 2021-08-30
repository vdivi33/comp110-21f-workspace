"""Demonstartion of numeric operators."""
__author__ = "730470448"
left_side: str = input("Left-hand side: ")
right_side: str = input("Right-hand side: ")
left: int = int(left_side)
right: int = int(right_side)
print(left_side + " ** " + right_side + " is " + str(left**right))
print(left_side + " / " + right_side + " is " + str(left / right))
print(left_side + " // " + right_side + " is " + str(left // right))
print(left_side + " % " + right_side + " is " + str(left % right))