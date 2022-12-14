'''1.6: Experiment with strings.'''

# Ask the user to input some tekst and store the response in a variable t
t: str = input("Input some text: ")

# Print the tekst in all uppercase and also in all lowercase characters
print("UPPER:", t.upper())
print("lower:", t.lower())

# Use the capitalize() and title() methods and print the results
print("Capitalize:", t.capitalize())
print("title:", t.title())

# Print the first three characters by using slicing
print("First three characters:", t[:3])

# Check if the tekst ends with a question mark
print("Ends with '?' :", t[-1] == '?')

# Print the text in lowercase with all spaces replaced by an underscore
# by using the method replace(). This is called snake_case
print("snake_case:", t.lower().replace(' ', '_'))

# Output:
# > python .\strings.py
# Input some text: this is THE TEXT for ExPeRiMeNtInG With Strings.
# upper: THIS IS THE TEXT FOR EXPERIMENTING WITH STRINGS.
# lower: this is the text for experimenting with strings.
# capitalize: This is the text for experimenting with strings.
# title: This Is The Text For Experimenting With Strings.
# First three characters: thi
# Ends with '?': False
# snake_case: this_is_THE_TEXT_for_ExPeRiMeNtInG_With_Strings.
