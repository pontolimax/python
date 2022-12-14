'''is this a leapyear?'''

# Ask the user to input a year.
input_year: str = input('Year: ')

# Change the input to a number using int()
year: int = int(input_year)

# Calculate if the year is a leapyear
#   1. a year is a leapyear if the year can be divided by 4
#   2. but ( and ) the year can not be divided by 100
#   3. except ( or ) if the year can be divided by 400
can_be_divided_by_4: bool = year % 4 == 0
can_not_be_divided_by_100: bool = year % 100 != 0
can_be_divided_by_400: bool = year % 400 == 0

is_leapyear: bool = can_be_divided_by_4 and can_not_be_divided_by_100 or can_be_divided_by_400

# Print the result
print(year, " is a leap year : ", is_leapyear)

# > python .\leapyear.py
# Year: 2022
# 2022  is a leap year :  False
# > python .\leapyear.py
# Year: 2020
# 2020  is a leap year :  True
# > python .\leapyear.py
# Year: 2100
# 2100  is a leap year :  False
# > python .\leapyear.py
# Year: 2000
# 2000  is a leap year :  True
# >
