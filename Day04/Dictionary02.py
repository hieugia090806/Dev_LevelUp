#-- PRINT KEYS FROM THE LIST. --#
#-- #1. Use for loop. --#
print("-" * 20)
cars = {
    "Mercedes-Benz": 1886,
    "Peugeot": 1889,
    "Flat": 1899,
    "Ford": 1903
}
for car in cars:
    print(car) 
#-- #2. Use keys() method. --#
print("-" * 20)
fruits = {
    "apples": "red",
    "banana": "yellow",
    "grapes": "purple"
}
for fruit in fruits.keys():
    print(fruit)
#-- PRINT VALUES FROM THE LIST. --#
#-- #1. Use for loop. --#
print("-" * 20)
for car in cars:
    print(cars[car])
print("-" * 20)
for fruit in fruits.values():
    print(fruit)
#-- PRINT BOTH KEY-VALUES. --#
print("-" * 20)
for car, year in cars.items():
    print(car, year)
print("-" * 20)
for fruit, color in fruits.items():
    print(fruit, color)
#-- COPY DICTIONARY. --#
print("-" * 20)
copy_dictionary = cars.copy()
print(f"Copy Dictionary: {copy_dictionary}")
copy_fruitlist = dict(fruits)
print(f"Copy Fruit List: {copy_fruitlist}")
#-- NESTED DICTIONARY. --#
print("-" * 20)
myfamily = {
    "children1": {
        "Name": "Stepth",
        "Age": 7
    },
    "children2": {
        "Name":"Thomas",
        "Age":15
    },
    "children3": {
        "Name": "Rosie",
        "Age": 25
    }
}
print(myfamily)
print("-" * 20)
jenny = {
    "Name": "jenny",
    "Gender": "Female",
    "Major": "Marketing"
}
beth = {
    "Name": "beth",
    "Gender": "Male",
    "Major": "CS - AI"
}
lisa = {
    "Name": "lisa",
    "Gender": "Female",
    "Major": "Business"
}
classroom = {
    "student1": jenny,
    "student2": beth,
    "student3": lisa
}
print(classroom)
print(classroom["student2"]["Gender"])
for student, name in classroom.items():
    print(student)
    for names in name:
        print(student + ":" + name[names])