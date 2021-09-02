"""Repeating a beat in a loop."""

__author__ = "730470448"


# Begin your solution here...


beat = input("What beat do you want to repeat? ")
repetitions: int = int(input("How many times do you want to repeat it? "))
sequence: str = ""
if(repetitions <= 0):
    {
        print("No beat...")
    }
else:
    while(repetitions > 1):
        sequence = sequence + beat + " "
        repetitions = repetitions - 1
    sequence = sequence + beat

print(sequence)