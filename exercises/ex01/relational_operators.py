"""Relational operator demonstration"""
__author__ = "730470448"

left_hand: str = input("Left-hand side: ")
right_hand: str = input("Right-hand side: ")

if(left_hand < right_hand):
    {
        print(left_hand +" < " + right_hand + " is True")
    }
else: 
    print(left_hand + " < " + right_hand + " is False")



if(left_hand >= right_hand):
    {
        print(left_hand + " >= " + right_hand + " is True")
    }
else:
    print(left_hand + " >= " + right_hand + " is False")



if(left_hand == right_hand):
    {
        print(left_hand + " == " + right_hand+ " is True")
    }
else:
    print(left_hand + " == " + right_hand + " is False")



if(left_hand != right_hand):
    {
        print(left_hand + " != " + right_hand + " is True")
    }
else:
    print(left_hand + " != " + right_hand + " is False")


