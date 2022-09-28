# Write a Python program to test whether a passed letter is a vowel or not.
import sys
import re

regexp = "[aeiouy]"

letter = sys.argv[1].lower()


if(re.search(regexp, letter)):
    print("The letter is a vowel")
else:
    print("The letter is not a vowel")
