"""
find method is almost equal to index method, because it return
the position of an character in a string. The only difference
is that find method return -1 when there is not match
"""

country = "argentina"
print(country.find("g"))

# if character is repeated, it return the first match position.
print(country.find("a"))
