#-- Basic Computer Calculations. --#
print("-- Basic Computer Calculation Programme. --")
#-- User Input Numbers. --#
num01 = float(input("Enter First Number: ")) #-- User input for first number type float. --#
num02 = float(input("Enter Second Number: ")) #-- User input for second number type float. --#
#-- Basic calculations. --#
sum = num01 + num02 #-- Addition. --#
difference = num01 - num02 #-- Subtraction. --#
product = num01 * num02 #-- Multiplication. --#
quotient = num01 / num02 #-- Division. --#
#-- Displaying the results. --#
print(f"The sum of {num01} and {num02} is: {sum} and type of {sum} is {type(sum)}.") #-- Displaying the sum. --#    
print(f"The difference of {num01} and {num02} is: {difference} and type of {difference} is {type(difference)}.") #-- Displaying the difference. --#
print(f"The product of {num01} and {num02} is: {product} and type of {product} is {type(product)}.") #-- Displaying the product. --#
print(f"The quotient of {num01} and {num02} is: {quotient} and type of {quotient} is {type(quotient)}.") #-- Displaying the quotient. --#