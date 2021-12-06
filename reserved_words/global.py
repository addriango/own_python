"""
we use 'global' keyword to create a global variable 
and make changes to the variable in a local context
"""

name = "frank"

#we put global word to be able to modify the global variable
def change_name():
    # global name
    name = "carlos"
    print(name)

change_name()
print(name)
