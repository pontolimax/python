'''1.5: A program that simulates throwing 5 dice.'''

# Import the random library
import random

# Generate a random number between 1 and 6 with random.randint(1, 6)
# and store the number in a variable dice1.
dice1: int = random.randint(1, 6)

# Repeat this 4 more times creating variables dice2 up to dice5.
dice2: int = random.randint(1, 6)
dice3: int = random.randint(1, 6)
dice4: int = random.randint(1, 6)
dice5: int = random.randint(1, 6)

# Print the values of the dice
print('Dice 1:', dice1)
print('Dice 2:', dice2)
print('Dice 3:', dice3)
print('Dice 4:', dice4)
print('Dice 5:', dice5)

# Also print the total sum of the values
print('Sum:', dice1 + dice2 + dice3 + dice4 + dice5)

# Output:
# > python .\dice.py
# Dice 1: 6
# Dice 2: 6
# Dice 3: 2
# Dice 4: 1
# Dice 5: 3
# Sum: 18
