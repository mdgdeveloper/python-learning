# 5. Write a Python program to check if an integer is the power of another integer.

import sys

value1 = int(sys.argv[1])
value2 = int(sys.argv[2])


def powOfAnother(num1, num2):
    if(float(num1**(1/num2)).is_integer() or float(num2**(1/num1)).is_integer()):
        return True
    else:
        return False


print(powOfAnother(value1, value2))
