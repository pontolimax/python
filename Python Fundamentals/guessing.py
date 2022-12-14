'''1.9: Guessing game'''

import random
secret_number = random.randint(1, 100)
nr_guesses: int = 0

print('Guess a number between 1 and 100')

while True:
    guess: int = int(input("What is your next guess? "))
    nr_guesses += 1
    if guess > secret_number:
        print("lower")
    elif guess < secret_number:
        print("higher")
    elif guess == secret_number:
        print(f'YEAAAH! You guessed it in {nr_guesses} guesses')
        break
    else:
        print("try again!")
