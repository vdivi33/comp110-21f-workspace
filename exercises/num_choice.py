"""Challenge Question #1"""

choice: int = int(input("Enter: "))

if choice > 50:
    if choice > 75:
        print("D")
    else:
        print("B")
else:
    if choice < 25:
        print("A")
    else:
        print("C")