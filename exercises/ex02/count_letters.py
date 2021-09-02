"""Counting letters in a string."""

__author__ = "730470448"


# Begin your solution here...
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
count: int = 0
length: int = len(word)
i: int = 1
while length > 0:
    if(word[length - 1] == letter):
        count = count + 1
    length = length - 1
print("Count: " + str(count))