# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
import sys

value = sys.argv[1]
n = sys.argv[2]
result = ""
for i in range(int(n)):
    result = result + value

print(result)
