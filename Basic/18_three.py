import sys

numbers = sys.argv[1:]

# Three(numbers)
# @param int[] number
# List of numbers obtained
#
# @return List[int]


def three(numbers):
    if(numbers[0] == numbers[1] and numbers[0] == numbers[2]):
        return(3*3*int(numbers[0]))
    else:
        return(int(numbers[0])+int(numbers[1])+int(numbers[2]))


print(three(numbers))
