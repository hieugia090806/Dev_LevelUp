#-- Day02: Python Lists --#
#-- 2.1 Creating fruit_list and printing it --#
fruit_list = ['apple', 'banana', 'grape', 'orange', 'kiwi', 'mango', 'pineapple', 'strawberry', 'blueberry', 'watermelon']
print(f"Fruit List: {fruit_list}")
#-- 2.2 Print the length of fruit_list --#
print(f"Length of fruit_list: {len(fruit_list)}")
print(f"Type of fruit_list: {type(fruit_list)}")
#-- 2.3 Converting car_logo_list to a list and printing it --#
car_logo_list = ('Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW')
car_logo_list = list(car_logo_list)
print(f"Car Logo List: {car_logo_list}")
#-- 2.4 Accessing elements in car_logo_list --#
print(f"First car logo: {car_logo_list[0]}") #-- Index[0] starts from left to right --#
print(f"Last car logo: {car_logo_list[-1]}") #-- Index[-1] starts from right to left --#
print(f"Car logos: {car_logo_list[1:4]}") #-- Slicing from index 1 to 3 (4 is exclusive) --#
print(f"Car logos from index 1 to end: {car_logo_list[1:]}") #-- Slicing from index 1 to the end --#
print(f"Car logos from start to index 3: {car_logo_list[:4]}") #-- Slicing from start to index 3 (4 is exclusive) --#
print(f"Car logos from index 1 to 3 with step 2: {car_logo_list[1:4:2]}") #-- Slicing from index 1 to 3 with step 2 --#
print(f"Car logos from index -4 to -1: {car_logo_list[-4:-1]}") #-- Slicing from index -4 to -1 (exclusive) --#
#-- Change item value in the list. --#
car_logo_list[2] = 'Mercedes'
print(f"Updated Car Logo List: {car_logo_list}")
#-- Change a range of item values in the list. --#
car_logo_list[1:3] = ['Audi', 'Volkswagen']
print(f"Updated Car Logo List after range change: {car_logo_list}")
#-- Add a new item to the list. --#
car_logo_list.append('Ferrari')
print(f"Car Logo List after appending: {car_logo_list}")
car_logo_list.insert(4, 'Lamborghini')
print(f"Car Logo List after inserting at index 4: {car_logo_list}")
#-- Extend the list. --#
europe_car_logo_list = ['Porsche', 'Jaguar', 'Maserati']
car_logo_list.extend(europe_car_logo_list)
print(f"Car Logo List after extending: {car_logo_list}")
latest_car_logo_list = ('Tesla', 'Rivian')
car_logo_list.extend(latest_car_logo_list)
print(f"Car Logo List after extending with latest logos: {car_logo_list}")
#-- Remove an item from the list. --#
fruit_list.remove('kiwi')
print(f"Fruit List after removing 'kiwi': {fruit_list}")
fruit_list.pop(2) #-- Remove item at index 2 --#
print(f"Fruit List after popping index 2: {fruit_list}")
del fruit_list[3] #-- Delete item at index 3 --#
print(f"Fruit List after deleting index 3: {fruit_list}")
del fruit_list
print("Fruit List deleted.")
#-- Loop List. --#
for num, logo in enumerate(car_logo_list):
    print(f"Car Logo {num + 1}: {logo}")
animal_list = ['dog', 'cat', 'rabbit', 'hamster', 'parrot']
for i in range(len(animal_list)):
    print(f"Animal {i + 1}: {animal_list[i]}")
water_animal_list = ['fish', 'dolphin', 'shark', 'whale', 'octopus']
i = 0
while i < len(water_animal_list):
    print(f"Water Animal {i + 1}: {water_animal_list[i]}")
    i += 1
plant_list = ['rose', 'tulip', 'sunflower', 'daisy', 'orchid']
[print(x) for x in plant_list]
#-- Sort the list. --#
car_logo_list.sort()
print(f"Sorted Car Logo List: {car_logo_list}")
car_logo_list.sort(reverse=True)
print(f"Sorted Car Logo List in reverse order: {car_logo_list}")
#-- Copy the list. --#
new_car_logo_list = car_logo_list.copy()
print(f"Copied Car Logo List: {new_car_logo_list}")
#-- Join the list. --#
letter = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5]
all = letter + numbers
print(f"Joined List: {all}")