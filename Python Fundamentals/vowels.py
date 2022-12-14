'''1.8: Count vowels'''

# Get some tekst from input and put this in a variable
text: str = input("Enter some text: ")
# Loop through the vowels['a', 'e', 'i', 'o', 'u', 'y']
number_vowels: int = 0
for vowel in ['a', 'e', 'i', 'o', 'u', 'y']:
    # Count the number of occurances of each vowel in the text
    # Print a message for each vowel indicating the number of occurances
    count_vowel = text.count(vowel)
    number_vowels += count_vowel
    print(f'{vowel}: {count_vowel}')

# After looping through the vowels
# … print a message indicating the total length of the text
text_length: int = text.count('') - 1
print(f'Text length: {text_length}')
# … and the total number of vowels
print(f'Number of vowels: {number_vowels}')
