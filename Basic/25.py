# 25. Write a Python program to check whether a specified value is contained in a group of values.
import sys

test = int(sys.argv[1])

value = [1, 2, 3, 4, 5, 10, 11, 12]

found = False

for i in value:
    if test == i:
        found = True

if(found):
    print(f"The value {test} is present")
else:
    print(f"The value {test} is not present")
