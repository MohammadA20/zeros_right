"""
    In this program, we have to check if the number is 0, then swap condition will be implemented to the right.
"""

ZEROES = []
ADD = []

def move_zeros(numbers):
    for move in range(len(numbers)):
        if numbers[move] != 0:
            ADD.append(numbers[move])
        else:
            ZEROES.append(numbers[move])

move_zeros([1, 3, 0, 10, 2, 0, 0, 0, 33, 3, 4])
print(ADD + ZEROES)