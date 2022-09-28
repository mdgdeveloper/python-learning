# Write a Python program to count the number 4 in a given list

list = [2, 4, 2, 3, 2, 12, 21, 4, 2, 4]
count = 0

for i in list:
    if(i == 4):
        count = count + 1

print(count)
