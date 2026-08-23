#-- Python For Loops. --#
#-- Print each item in the list. --#
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("-" * 50)
#-- Print each letter in the string. --#
for letter in 'grape':
    print(letter)
print("-" * 50)
#-- Break statement --#
cars = ['Mazda', 'Toyota', 'Honda', 'Ford']
for car in cars:
    print(car)
    if car.lower() == 'honda':
        break
print("-" * 50)
#-- Continue statement --#
companies = ['Google', 'Microsoft', 'Apple', 'Amazon']
for company in companies:
    if company.lower() == 'apple':
        continue #-- Means that if company is Apple, it will skip the print statement and continue to the next iteration. --#
    print(company)
print("-" * 50)
#-- The range() Function. --#
for num in range(10):
    print(num)
print("-" * 50)
#-- Else in the Loop. --#
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#-- Nested Loops. --#
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
#-- Pass Statement. --#
for x in [0, 1, 2]:
  pass