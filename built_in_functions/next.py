"""
we use 'next' to execute a paused function (generator), step by step
each call will execute an step until the next yield keyword.
"""

def create_pair_numbers(limit):
    for number in range(limit):
        if number == 0:
            continue
        if (number%2 == 0):
            yield number

my_generator = create_pair_numbers(10)
print(next(my_generator))

print("more code ...")

print(next(my_generator))
# print(next(my_generator))
