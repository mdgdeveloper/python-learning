# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
import sys

value = sys.argv[1]
copies = sys.argv[2]

if(len(value) < 2):
    print(value*int(copies))
else:
    print((value[0]+value[1])*int(copies))
