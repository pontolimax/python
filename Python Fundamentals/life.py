'''1.7: Print the stage of life depending on the age entered by the user.'''

# Use input() to ask for the age
age_input: str = input("Wat is your age? : ")

# Assign the integer value to a variable. Use int().
age: int = int(age_input)

# Age	Life stage
# 0 – 2	Baby
# 2 – 4	Toddler
# 4 – 13	Kid
# 13 – 20	Teenager
# 20 – 65	Adult
# 65 or older	Elder

# Print Life stage based on Age
if 0 <= age < 2:
    print('You are a baby')
elif 2 <= age < 4:
    print('You are a toddler')
elif 4 <= age < 13:
    print('You are a kid')
elif 13 <= age < 20:
    print('You are a toddler')
elif 20 <= age < 65:
    print('You are a toddler')
elif 65 <= age:
    print('You are a toddler')
else:
    print('You have not been born yet')
