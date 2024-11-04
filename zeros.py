"""
    In this program, we have to check if the number is 0, then swap condition will be implemented to the right.
"""

ZEROES = []
ADD = [] # List to add the non-zero numbers

def move_zeros(numbers):
    # If the number is non-zero, then append to the list else when we finish adding the numbers, it will add zeros to the end of the list
    for move in range(len(numbers)):
        if numbers[move] != 0:
            ADD.append(numbers[move])
        else:
            ZEROES.append(numbers[move])

# Calling the function
move_zeros([1, 3, 0, 10, 2, 0, 0, 0, 33, 3, 4])
print(ADD + ZEROES) #It will add the non-zero numbers with zeros to the list