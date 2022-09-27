# 7. Write a Python program to accept a filename from the user and print the extension of that.
import sys

filename = sys.argv[1]
filenameArray = filename.split(".")

print(filenameArray[1])
