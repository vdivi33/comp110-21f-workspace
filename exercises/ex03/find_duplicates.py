"""Finding duplicate letters in a word."""

__author__ = "730470448"

string: str = input("Enter a word: ")
length: int = len(string)
i: int = 0
j: int = 1
boolean: bool = False

while i < length:
    while j < length:
        if(string[j] == string[i]):
            boolean = True
        j = j + 1
    i = i + 1
    j = i + 1

print("Found duplicate: " + str(boolean))
