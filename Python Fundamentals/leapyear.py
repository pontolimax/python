'''is this a leapyear?'''
input_year = input('Year: ')
year = int(input_year)

is_leapyear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(year, " is a leap year : ", is_leapyear)
