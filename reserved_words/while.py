"""
we use 'while' cycle when we want to keep doing something
while a condition is true or false
"""

password = "crypto"
user_input = input("Give me the password : ")

while user_input != password:
    user_input = input("try it again : ")

print("yeah!, you log in")
