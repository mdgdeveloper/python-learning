# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
import sys

name = sys.argv[1]

nameArray = list(name)
result = []

for letter in nameArray:
    result.insert(0, letter)

print(" ".join(result))
