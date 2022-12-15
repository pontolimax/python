'''2.6: Range of floats'''

# A generator function that can generate a sequence
# of floats similar to the built-in function range.

# Using Decimal will improve the precision.
from decimal import Decimal


def drange(start: Decimal, stop: Decimal, step: Decimal = 1.0, endpoint=False) -> list[Decimal]:
    '''Create a loop that calculates the numbers from start to end with an increment of step.'''
    # The endpoint arguments specifies if the endpoint is included or not.
    number: Decimal = start
    numbers: list[Decimal] = []
    while number < stop or (endpoint and number <= stop):
        numbers.append(number)
        number += step
    return numbers


print(drange(0.0, 10.0, 1.1, True))

# Output:
# > python .\floats.py
# [0.0, 1.1, 2.2, 3.3000000000000003, 4.4, 5.5, 6.6,
#  7.699999999999999, 8.799999999999999, 9.899999999999999]
