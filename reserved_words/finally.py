"""
The finally block will always be executed, no
matter if the try block raises an error or not
"""
try:
    print(3 + 2)
    # say_hello() # error, because function not exist
except:
    print("there was an error")
finally:
    print("It will be always executed")
