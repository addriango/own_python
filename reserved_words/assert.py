"""
we use 'assert' word just in development phase to show
and error when user give us a wrong value
"""

def validate_age(age):
    assert age>0, "age can not be negative"
    print("age of user is : " + str(age))

#this should show an error because age is negative
# validate_age(-4)

#it works well
validate_age(7)



