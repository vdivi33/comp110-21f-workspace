"""Drawing forests in a loop."""

__author__ = "730470448"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
forest: str = ""

depth: int = int(input("Depth: "))
i: int = 0
j: int = 0
while i < depth:
    while j >= 0:
        j = j - 1
        forest = forest + TREE
    print(forest)
    i = i + 1
    j = 0
    