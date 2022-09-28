# Write a Python program to test whether a passed letter is a vowel or not.
import sys

VOWELS = ["a", "e", "i", "o", "u"]

letter = sys.argv[1].lower()

vowel = False
for i in VOWELS:
    if (i == letter):
        vowel = True

if(vowel):
    print("The letter is a vowel")
else:
    print("The letter is not a vowel")
