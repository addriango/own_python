"""
we use 'try' to give order to program to make something
but if it is not able to do it and return and error we can hanlde it
with an 'except' otherwise the program will be stopped
"""

try:
    5 / 0
except:
    print("division by zero is not allowed, try it again")
