# 7. Write a Python program to find a missing number from a list.

test1 = [1, 2, 4, 5, 6, 7, 8]


def missing(listValue):
    for idx, value in enumerate(listValue):
        if (value != idx+1):
            return idx+1

    return None


print(missing(test1))
