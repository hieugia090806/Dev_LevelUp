#-- Generate class Person with __init__ method. --#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Thomas", 20)
print(f"Hello, my name is {p1.name}!")
print(f"I'm {p1.age} years old.")

#-- Generate class without __init__ method. --#
class Animal:
    pass
my_animal = Animal()
my_animal.type = "dog"
my_animal.name = "Emily"
my_animal.age = 3
print(f"I have a {my_animal.type} and her name is {my_animal.name}. She's {my_animal.age} years old")

#-- Default values in __init___. --#
class Car:
    def __init__(self, name, time_used=20):
        self.name = name
        self.time_used = time_used
my_car = Car("Honda Supra")
friend_car = Car("Nissan GTR", 25)
print(f"I have a car named {my_car.name} and have driven for {my_car.time_used}")
print(f"My freind has a car named {friend_car.name} and have driven for {friend_car.time_used}")

#-- Several Parameter. --#
class NewCitizen():
    def __init__(self, name, age, gender, city, country):
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        self.country = country
c01 = NewCitizen("Emily", 25, "Female", "New York City", "USA")
print(f"Hello, everyone! My name is {c01.name}. I'm {c01.age} years old.")
print(f"I'm {c01.gender}. I'm from {c01.city},{c01.country}")
