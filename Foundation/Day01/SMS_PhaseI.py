#----------------------------------------------#
#-- Project: Student Management System.      --#
#-- Phase I: Student Information Collection. --#
#-- Author: Mr.Truong Ngoc Gia Hieu.         --#
#----------------------------------------------#
print("Welcome to Student Management System - Phase I: Student Information Collection")
print("-" * 79)
#-- Ask teacher for entering student name. --#
user = str(input("Please enter your name: "))
#-- Ask teacher gender. --#
gender = str(input(f"Hello {user}, which gender are you? (M/F): "))
if gender.lower() == "m" or gender.lower() == "male":
    print(f"Welcome Mr.{user} to Student Management System - Phase I: Student Information Collection")
elif gender.lower() == "f" or gender.lower() == "female":
    print(f"Welcome Ms.{user} to Student Management System - Phase I: Student Information Collection")
#-- Ask teacher for entering student information. --#
student_name = input(f"Dear {user}, please enter the student name: ")
student_age = int(input(f"Dear {user}, please enter the student age: "))
student_grade = input(f"Dear {user}, please enter the student grade (A/B/C/D/F): ")
student_gender = input(f"Dear {user}, please enter the student gender (M/F): ")
student_living_location = input(f"Dear {user}, please enter the student living location: ")
#-- Print the student information. --#
print("-" * 79)
print(f"Student Name: {student_name}")
print(f"Student Age: {student_age}")
print(f"Student Grade: {student_grade}")
print(f"Student Gender: {student_gender}")
print(f"Student Living Location: {student_living_location}")
