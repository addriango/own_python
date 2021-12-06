"""
we use 'raise' to create an custom error
for example when user give us a wrong value
"""

number1 = int(input("give me the fist number: "))
number2 = int(input("give me the second number: "))

if number2 == 0:
    raise ValueError("you give me a wrong value")
else:
    result = number1/number2
    print(result)
