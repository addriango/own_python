"""
we use 'yield from' when we need to iterate in anninated cycles.
"""

def get_cities(*cities):
    for element in cities:
        # for sub_element in element:
            yield from element

obtained_cities = get_cities("Bogota", "Cartagena", "Riohacha")
print(next(obtained_cities))
print(next(obtained_cities))
print(next(obtained_cities))
