#-- Python If Else. --#
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))

#-- Shorthand If --#
if age >= 18: print("You are an adult.")

# If - Elif - Else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print("Your grade is:", grade)

# Logical Operators (and, or, not)
if age >= 18 and score >= 70:
    print("You can apply for the scholarship.")
if age < 18 or score >= 95:
    print("Special consideration granted.")
if not (score < 50):
    print("You passed the exam.")

# Nested If
if age >= 18:
    print("Adult category")
    if score >= 80:
        print("Excellent performance")
    else:
        print("Needs improvement")
else:
    print("Minor category")

# Pass Statement
choice = input("Enter Y to continue: ")

if choice == "Y":
    pass  # Placeholder for future code
else:
    print("Program ended.")

print("Thank you for using the program!")