'''2.6: Range of floats'''

# The range function can only generate integers.
# Create a generator function that kan generate a sequence
# of floats similar to the bulit-in function range.

# You can use standard floats to achieve this but using Decimal will improve the precision.
from decimal import Decimal

# Define a function drange with arguments start, stop, step and endpoint.
# The endpoint arguments specifies if the endpoint is included or not.
# Give default values 1 for the step and False for endpoint.


def drange(start: Decimal, stop: Decimal, step: Decimal = 1.0, endpoint=False):
    '''Create a loop that calculates the numbers from start to end with an increment of step.'''
    # If endpoint is set to true also include the endpoint also.
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
