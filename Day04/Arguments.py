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

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
