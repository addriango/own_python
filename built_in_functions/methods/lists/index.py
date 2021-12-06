"""
we can use 'index' to get the index of an item in an list.
Note: If items is several times in the list, the index method
will return the first index that matched.
"""
# Not repetead item
colors = ["black", "red", "blue", "gray", "blue"]
my_index = colors.index("black")
print(my_index)

# repeated items
another_index = colors.index("blue")
print(another_index)
