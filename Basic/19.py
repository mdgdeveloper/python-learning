# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
import sys

value = sys.argv[1]

if(value[0] == "I" and value[1] == "s"):
    print(value)
else:
    print("Is"+value)
