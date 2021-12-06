"""
we use 'yield' when we want to iterate an list or object one by one.
And before to understand what a generator is, we have to understand
how a iterable works.
A Generator is a fnction that can be paused in steps
"""

# iterable charge all items in memory
def fruits():
    return ["apple", "pear", "orange"]

print(fruits())
# a generator is like a stoppable function that allow execute 
# a piece of code until the next yield
def gfruits():
    yield "apple"
    print("--------")
    yield "pear"
    print("--------")
    yield "orange"
    

f = gfruits()
print(next(f))
print(next(f))
print(next(f))
