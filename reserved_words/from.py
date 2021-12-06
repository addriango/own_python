"""
we use 'from' keyword when we want to specify
a labrary and not to import the entire library
It allows more efficiency in the program having less unused packages
"""

import math # bad practice

value = math.sqrt(5) # bad practice
print(value)

print("----------")

from math import sqrt #good practice

value = sqrt(5)  # more efficient,less code, and more readable
print(value)
