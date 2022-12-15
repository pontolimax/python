'''2.5: Banner'''

# Create a function that prints text surrounded by stars. Like a banner.
import re


def banner(text: str) -> None:
    '''Print a banner'''
    banner_text: str = '*  ' + text + '  *'
    banner_stars: str = re.sub(".", '*', banner_text)

    print(banner_stars)
    print(banner_text)
    print(banner_stars)


banner("Python Fundamentals 2.5: Banner")

# Output:
# *************************************
# *  Python Fundamentals 2.5: Banner *
# *************************************
