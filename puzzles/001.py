# 1. Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.

test1 = [19, 19, 15, 5, 3, 5, 5, 2]
test2 = [19, 15, 15, 5, 3, 3, 5, 2]


def prob1(values):
    five = 0
    nineteen = 0
    for k in values:
        if k == 5:
            five = five + 1

        if k == 19:
            nineteen = nineteen + 1

    if(nineteen == 2 and five >= 3):
        return True
    else:
        return False


print(prob1(test1))
print(prob1(test2))
