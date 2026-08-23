#-- CREATE FUNCTION. --#
def hello_world():
    print("Hello, World!")
#-- Calling function. --#
hello_world()
#-- CALCULATE TEMPERATURE DEGREE. --#
def fahrenheit_to_celsius(fahrenheit):
    return print(f"The celcius degree is: {(fahrenheit - 32) * 5/9} celcius degree")
fahrenheit_to_celsius(78)
def get_greeting():
    return "Hello, everyone!"
message = get_greeting()
print(message)
def say_konichiwa():
    return "Konichiwa"
print(say_konichiwa())
def nothing():
    pass