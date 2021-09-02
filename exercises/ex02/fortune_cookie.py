"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730470448"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
random_int = randint(1, 4)
print(random_int)
if(random_int == 1):
    print("You will find exactly what you are looking for!")   
elif(random_int == 2):
    print("Fortune and sucess lies ahead!")
elif(random_int == 3):
    print("You will soon make lifelong friends")
elif(random_int == 4):
    print("Keep your eye out for someone special!")
print("Now, go spread positive vibes!")