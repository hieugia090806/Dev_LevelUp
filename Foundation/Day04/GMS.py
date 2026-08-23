#--------------- GRADE MANAGEMENT SYSTEM. ---------------#
#-- Function username(). --#
def username(firstname, middlename, lastname): #-- Parameters (firstname, middlename, lastname). --#
    #-- Return greeting statement. --#
    return f"Hello, {firstname} {middlename} {lastname}! Welcome to Grade Management System...."

#-- Function menu(). --#
def menu():
    #-- Display menu() option. --#
    print("Here are the following options:\n"
          "  1. Add Student and Grade.\n"
          "  2. Look up/Search Student and Grade.\n"
          "  3. Calculate Average Grade\n" 
          "  4. Show high/low/pass student list\n"
          "  5. Exit Program")
    
#-- Function AddStudentGrade(). --#
student_list = {} #-- Global Dictionary. --#
def AddStudentGrade():
    #-- Input Student Name. --#
    student_name = input("Please enter students name (at least three students): ").split()
    #-- Input Student Grade. --#
    student_grade = list(map(int, input("Please enter studen grades (matching with student): ").split()))
    #-- For Loop for matching each student with each grade. --#
    for name, grade in zip(student_name, student_grade):
        student_list[name] = grade
    #-- Print the student dictionary. --#
    print(f"Here is the list: {student_list}")

#-- Function LookUp(). --#
def LookUp():
    #-- Call AddStudentGrade() Function. --#
    AddStudentGrade()
    #-- Enter student name that wanna lookup. --#
    student_lookup = str(input("Please enter student that you want to lookup: "))
    #-- Using If condition to check that does it exists or not. --#
    if student_lookup in student_list: #-- If exists. --#
        #-- Print statement. --#
        print(f"Grade of {student_lookup.lower()} is {student_list[student_lookup]}")
    else: #-- Does not exist. --#
        #-- Print statement. --#
        print(f"ERROR! Student {student_lookup} is NOT FOUND in the list.")

#-- Function AvgGrade(). --#
def AvgGrade():
    #-- Call function. --#
    AddStudentGrade()
    #-- Check lenght of the dictionary. --#
    if len(student_list) == 0: #-- If len equal to 0. --#
        #-- Print announcement. --#
        print(f"ERROR: Length of student list is empty! Please check again.")
    else:
        #-- Count total grade. --#
        total_grade = sum(student_list.values())
        #-- Calculate Average. --#
        average_grade = total_grade/len(student_list)
        #- Print the result. --#
        print(f"Average Grade of Class is: {average_grade}")

#-- Function Ranking Students. --#
def GetGradeClassification(grade):
    #-- Pass Level (P). --#
    if 50 <= grade < 60:
        return "P"
    #-- Credit Level (C). --#
    elif 60 <= grade < 70:
        return "C"
    #-- Distinction Level (D). --#
    elif 70 <= grade < 80:
        return "D"
    #-- High Distinction A (HD01). --#
    elif 80 <= grade < 90:
        return "HD01"
    #-- High Distinction B (HD02. --#)
    elif 90 <= grade <= 100:
        return "HD02"
    #-- Under Pass(P) Level. --#
    else:
        return "Fail"

def RankingStudents():
    AddStudentGrade()
    #-- Check len of dictionary. --#
    if len(student_list) == 0:
        print("No students found.")
        return
    #-- Highest and lowest student. --#
    highest_student = max(student_list, key=student_list.get)
    lowest_student = min(student_list, key=student_list.get)
    #-- Report. --#
    print("\n===== STUDENT REPORT =====")
    print(
        f"Highest Student: {highest_student} "
        f"({student_list[highest_student]})"
    )
    print(
        f"Lowest Student: {lowest_student} "
        f"({student_list[lowest_student]})"
    )
    print("\nPass Students:")
    for name, grade in student_list.items():
        if grade >= 50:

            classification = GetGradeClassification(grade)

            print(f"{name}: {grade} ({classification})")

#-- Funtion main(). --#
def Main():
    print("-"*15 + " GRADE MANAGEMENT SYSTEM " + "-"*15)
    #-- Enter FirstName. --#
    firstname = str(input("Dear User, Please enter your firstname: "))
    #-- Enter MiddleName. --#
    middlename = str(input("Dear User, Please enter your middlename: "))
    #-- Enter LastName. --#
    lastname = str(input("Dear User, please enter your lastname: "))
    #-- Call and print the welcome statement. --#
    print(username(firstname, middlename, lastname))
    #-- Input User Choice. --#
    choice = str(input(f"Dear {firstname} {middlename} {lastname}! Please enter your choice: "))
    #-- CONFIRMATION. --#
    print(f"CONFIRMATION: Dear {firstname} {middlename} {lastname}, your choice is {int(choice)}")
    #-- While Loop. --#
    while True:
        #-- If choice == 1. --#
        if int(choice) == 1: 
            #-- Call function. --#
            AddStudentGrade()
            break
        #-- If choice == 2. --#
        elif int(choice) == 2:
            #-- Call function. --#
            LookUp()
            break
        #-- If choice == 2. --#
        elif int(choice) == 3:
            #-- Call function. --#
            AvgGrade()
            break
        #-- If choice == 4. --#
        elif int(choice) ==4 :
            RankingStudents()
            break
        #-- If choice == 5. --#
        elif int(choice) == 5:
            #-- Print statement. --#
            print("Thank you for using...See next time!")
            break
        else:
            return "Invald choice! Please choose again by restarting the program"
            break

#-- Call function main(). --#
Main()