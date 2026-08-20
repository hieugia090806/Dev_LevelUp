class MyClass:
    value01 = 5
x = MyClass()
print(f"The value of x in the {MyClass} is: {x.value01}")
#-- Multiple Objects. --#
class MyScore:
    sem01 = 9.7
    sem02 = 8.4
    sem03 = 9.0
p1 = MyScore()
print(f"The value of sem01 in the {MyScore} is {p1.sem01}")
p2 = MyScore()
print(f"The value of sem01 in the {MyScore} is {p2.sem02}")
p3 = MyScore()
print(f"The value of sem01 in the {MyScore} is {p3.sem03}")
#-- The Pass Statement. --#
class Person:
    pass