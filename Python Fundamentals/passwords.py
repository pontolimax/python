'''2.3: Password generator'''
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

# Generate a password of at least 6 characters
# with at least 1 capital, 1 lowercase, 1 number and 1 special character.

part1: list[str] = random.choices(ascii_lowercase, k=3)
part2: list[str] = random.choices(ascii_uppercase, k=3)
part3: list[str] = random.choices(digits, k=3)
part4: list[str] = random.choices(punctuation, k=3)

characters: list[str] = part1 + part2 + part3 + part4
random.shuffle(characters)
password: str = ''.join(characters)

print(password)

# Output:
# > python .\passwords.py
# 5yM2V.2!Z?lk
# > python .\passwords.py
# +u3r9Eb_G0;S
