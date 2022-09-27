# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

import sys


number = int(sys.argv[1])

if (number >= 100):
    if (number <= 1000):
        print(f"{number} is between 100 and 1000")
    else:
        if (number <= 2000):
            print(f"{number} is within 100 and 2000")
