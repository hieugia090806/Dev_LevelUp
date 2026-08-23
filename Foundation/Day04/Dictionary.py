#-- Dictionary used to store data values in key:value pairs. --#
print("-" * 100)
print("Basic Dictionary Methos....")
this_dictionary = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Year": 2026,
    "colors": ["red", "blue", "green"]
}
#-- The second value for the key "Year" is overwrite to the the first value. --#
print(f"The dictionary is: {this_dictionary}")
#-- Print the value of the key "Brand". --#
print(f"The value of key Brand is: {this_dictionary["Brand"]}")
#-- Print the length of the dictionary. --#
print(f"The length of the dictionary is: {len(this_dictionary)}")
#-- Print type of the dictionary. --#
print(f"Type of the dictionary is: {type(this_dictionary)}")
#-- dict() Constructor. --#
second_dictionary = dict(name="John", age=40, country="Germany")
print(second_dictionary)
print("-" * 100)
print("Access Dictionary Items....")
#-- Accessing Items. --#
x = this_dictionary["Model"] #-- Get the Key. --
print(f"The value of the key Model is: {x}")
citizen = {
    "John": 56,
    "Marry": 24,
    "Thomas": 37,
    "Jonathan": 43
}
name = citizen.get("John") #-- Get the value of the key "John". --#
print(f"The age of John is: {name}")
key = citizen.keys()
print(f"All keys of the citizen dictionary is: {key}")
citizen["John"] = 45
print(f"Updated list: {citizen}")
citizen_items = citizen.items
print(citizen_items)
print("-" * 100)
print("Change, Add, and Remove Items....")
fruit_price = {
    "grapes": "$15.23 per kilogram",
    "apples": "$20.00 per kilogram",
    "bananna": "$7.56 per kilogram"
}
print(f"Fruit List: {fruit_price}")
#-- Update Fruit Dicionary. --#
fruit_price.update({"peache": "$26.72 per kilogram"})
fruit_price["watermelon"] = "Sold Out" #-- Add to the list. --#
#-- Update() means add new key-value to list. --#
print(f"Updated fruit list: {fruit_price}")
#- Remove Item from the List. --#
fruit_price.pop("watermelon")
print(f"Fruit list after pop: {fruit_price}")
fruit_price.popitem() #-- popitem() means delete the last item. --#
print(f"Fruit list after popitem(): {fruit_price}")
fruit_price.clear()
print(f"Fruit list after clear(): {fruit_price}")