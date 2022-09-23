import math
"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]


    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

median = None
numbers.sort()
if len(numbers) == 1:
    median = numbers[0]
# Even list
elif len(numbers) % 2 == 0:

    median = (numbers[math.floor(len(numbers) / 2)] + numbers[math.floor(len(numbers) / 2) - 1]) / 2
# Odd list
else:
    median = numbers[math.floor(len(numbers) / 2)]

print(median)
