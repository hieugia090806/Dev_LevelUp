print("-"*12 + " Basic Calculator Program " + "-"*12)
num01 = float(input("Dear User, please input the first number: "))
print(f"CONFRIMATION! The first number is {num01}")
num02 = float(input("Dear User, please input the first number: "))
print(f"CONFRIMATION! The second number is {num02}")
operation = str(input("Dear user, please input your operation that you wanna: "))
#-- Sum Operation. --#
if operation.lower() == "sum" or operation.lower() == "addition":
    print(f"The {operation.lower()} of {num01} and {num02} is: {num01+num02}")
elif operation.lower() == "subtract" or operation.lower() == "subtraction" or operation.lower() == "minus":
    print(f"The {operation.lower()} of {num01} and {num02} is: {num01-num02}")
elif operation.lower() == "multiplication" or operation.lower() == "multiply":
    print(f"The {operation.lower()} of {num01} and {num02} is: {num01*num02}")
elif operation.lower() == "divide" or operation.lower() == "division":
    print(f"The {operation.lower()} of {num01} and {num02} is: {num01/num02}")
else:
    print("Thank you for using the Basic Calculator..See next time!")
    exit()