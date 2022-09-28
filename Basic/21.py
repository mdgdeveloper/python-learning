# 21 Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
import sys

value = int(sys.argv[1])

if(value % 2 == 0):
    print(f"The number {value} is odd")
else:
    print(f"The number {value} is even")
