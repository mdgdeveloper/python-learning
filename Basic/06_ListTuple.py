# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
import sys

numList = sys.argv[1]

arrayList = numList.split(",")
tupleList = tuple(arrayList)

print("Array:", arrayList)
print("Tuple:", tupleList)
