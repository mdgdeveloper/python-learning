# 1. Write a Python program to check if a given positive integer is a power of two.
import sys

value = int(sys.argv[1])


def check_pow(number):
    if(float(number**(1/2)).is_integer()):
        return True
    else:
        return False


print(check_pow(value))
