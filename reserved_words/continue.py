"""
we use 'continue' when we want to jump a iteration in a cycle
when a condition is riched
"""

for i in range(10):
    if i == 7:
        print("this number is not printed")
        continue
    print(i)
