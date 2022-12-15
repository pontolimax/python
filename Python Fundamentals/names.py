'''2.1: List of entered names'''

# Enter a number of names. If no name is entered (return ) continue with
# the rest of the program and print the entered names. Sorted if possible.

# Start with an empty list names = []
names: list[str] = []

# Use a while loop to ask for a name with name = input(...)
while True:
    name: str = input('Enter a name: ')
    # If no name has been entered break out of the loop
    if name == '':
        break
    # Add the entered name to the list with names.append(name)
    names.append(name)

# Print the entered names in a for loop.
# Sort the list with sorted(names)
for name in sorted(names):
    print(name)

# Output:
# > python .\names.py
# Enter a name: John
# Enter a name: Peter
# Enter a name: Mary
# Enter a name: Joanne
# Enter a name:
# Joanne
# John
# Mary
# Peter
