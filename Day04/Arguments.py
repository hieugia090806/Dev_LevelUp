def hello(name): #-- name is PARAMETER. --#
    return print(f"Hello, {name}!")
hello("Nicky") #-- Nicky is ARGUMENT. --#

def greeting(firstname, lastname):
    return print(f"Hello, {firstname} {lastname}")
greeting("Truong", "Hieu") #-- NOTE: Num of ARGUEMENTS MUST BE EQUAL to PARAMATERS. --#

def my_function(name = "friend"): #-- Default parameters. --#
    print(f"Hello {name}")
my_function("Thomas")

def my_animal(animal, name):
    print(f"I have an {animal}")
    print(f"My {animal} name is {name}")
my_animal(animal="cat", name="Anne")