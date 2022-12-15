'''2.7: Sort a list'''

# Create a function called number_of_vowels to count the number of vowels
# tip:


def number_of_vowels(word: str) -> int:
    '''Count the number of vowels in "word"'''
    return sum([word.count(v) for v in 'aeiou'])


# Enter a piece of tekst and split into words
words: list[str] = input("Enter a text: ").split()

# Use the sorted function to sort these words
for sorted_word in sorted(words, key=number_of_vowels):
    print(sorted_word)

# Output:
# > python .\sort.py
# Enter a text: Create a function called number_of_vowels to count the number of vowels.
# a
# to
# the
# of
# called
# count
# number
# vowels.
# Create
# function
# number_of_vowels
