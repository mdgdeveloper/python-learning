# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

import sys

integerStr = sys.argv[1]
value1 = int(f"{integerStr}")
value2 = int(f"{integerStr}{integerStr}")
value3 = int(f"{integerStr}{integerStr}{integerStr}")

print(value1+value2+value3)
