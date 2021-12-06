"""
we use 'class' to create an object, that is a model of something
"""

class Person:
    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email

    def say_hello(self):
        return print("hello baby!")

test = Person("Brad", "Pitt", "bradpit@gmail.com")
print(test.name)
print(test.say_hello())
