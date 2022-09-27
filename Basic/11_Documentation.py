# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

import sys

functionToShow = sys.argv[1]

print(functionToShow.__doc__)
