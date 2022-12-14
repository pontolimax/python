'''1.6: Experiment with strings.'''

# Ask the user to input some tekst and store the response in a variable t
t: str = input("Input some text: ")

# Print the tekst in all uppercase and also in all lowercase characters
print("TEXT IN UPPER:", t.upper())
print("text in lower:", t.lower())

# Use the capitalize() and title() methods and print the results
print("Capitalized text:", t.capitalize())
print("Text In Title:", t.title())

# Print the first three characters by using slicing
print("First three characters:", t[:3])

# Check if the tekst ends with a question mark
print("Ends with '?' :", t[-1] == '?')

# Print the text in lowercase with all spaces replaced by an underscore
# by using the method replace(). This is called snake_case
print("text_in_snake_case:", t.lower().replace(' ', '_'))

# Output:
# > python .\strings.py
# Input some text: this is THE TEXT for ExPeRiMeNtInG With Strings?
# TEXT IN UPPER: THIS IS THE TEXT FOR EXPERIMENTING WITH STRINGS?
# text in lower: this is the text for experimenting with strings?
# Capitalized text: This is the text for experimenting with strings?
# Text In Title: This Is The Text For Experimenting With Strings?
# First three characters: thi
# Ends with '?': True
# text_in_snake_case: this_is_the_text_for_experimenting_with_strings?
