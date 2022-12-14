'''1.4: A program that calculates the area and circumference of a circle.'''

# Import the math library.
import math

# Ask the user to input the radius.
input_radius: str = input('Give the radius: ')

# Change the input to a number using float() and assign to a variable r.
r: float = float(input_radius)

# Calculate the area with area = πr2
area: float = math.pi * r**2

# Calculate the circumference with circumference = 2πr
circumference: float = 2 * math.pi * r

# Print the results
print('Radius:', r)
print('Area:', area)
print('Circumference:', circumference)

# Output:
# > python .\circle.py
# Give the radius: 100
# Radius: 100.0
# Area: 31415.926535897932
# Circumference: 628.3185307179587
