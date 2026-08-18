print("-" * 100)
print("Project Name: Student Grade Management System\n" 
      "This program is designed to manage student grades and provide insights based on their performance.\n"
      "You can input student names, their scores, and the system will calculate their grades accordingly.\n"
      "Let's get started!")
print("-" * 100)
print("Belows are following options:\n"
      "  1. Add students name to the list.\n"
      "  2. Insert and Category Grades.\n"
      "  3. Exit the program")
#-- Aloow user input choice. --#
print("-" * 100)
choice = float(input("Please insert your choice: "))
print(f"Dear User, your choice is: {int(choice)}")
#-- Generate student list and grade list. --#
student_list = []
grade_list = []
#-- If-else Condition. --#
if choice == 1:
      student = str(input("Please enter the student name (at least three students): "))
      student_list.extend(student.split())
      print(f"Your current student list is: {student_list}")
elif choice == 2:
      print("-" * 100)
      print("Dear User, The grade system is marked as follows:\n"
            "  A: 90-100\n"
            "  B: 80-89\n"
            "  C: 70-79\n"
            "  D: 60-69\n"
            "  F: Below 60")
      grade = str(input("Please enter the student grade (at least three grades): "))
      grade_list.extend(grade.split())
      print(f"Your current student grades are: {grade_list}")
      for grade in grade_list:
            if 90 <= int(grade) <= 100:
                  print(f"Student with grade {grade} is in category A.")
            elif 80 <= int(grade) <= 89:
                  print(f"Student with grade {grade} is in category B.")
            elif 70 <= int(grade) <= 79:
                  print(f"Student with grade {grade} is in category C.")
            elif 60 <= int(grade) <= 69:
                  print(f"Student with grade {grade} is in category D.")
            else:
                  print(f"Student with grade {grade} is in category F.")
      print("-" * 100)
      answer = str(input("Dear User, Do you want to continue? (yes/no): "))
      if answer.lower() == "yes":
            print("Here are the following options:\n"
                  "  1. Add students name to the list.\n"
                  "  2. Delete student from the list.\n"
                  "  3. Find student in the list.\n"
                  "  4. Sort student list.\n"
                  "  5. Reverse student list.\n"
                  "  6. Find the highest and lowest grade.\n")
            sub_choice = float(input("Please insert your choice: "))
            print(f"Dear User, your choice is: {int(sub_choice)}")
            if sub_choice == 1:
                  student = str(input("Please enter the student name to add: "))
                  student_list.append(student)
                  print(f"Your updated student list is: {student_list}")
            elif sub_choice == 2:
                  student = str(input("Please enter the student name to delete: "))
                  if student in student_list:
                        student_list.remove(student)
                        print(f"Your updated student list is: {student_list}")
                  else:
                        print("Student not found in the list.")
            elif sub_choice == 3:
                  student = str(input("Please enter the student name to find: "))
                  if student in student_list:
                        print(f"Student {student} is in the list.")
                  else:
                        print(f"Student {student} is not in the list.")
            elif sub_choice == 4:
                  student_list.sort()
                  print(f"Your sorted student list is: {student_list}")
            elif sub_choice == 5:
                  student_list.reverse()
                  print(f"Your reversed student list is: {student_list}")
            elif sub_choice == 6:
                  if grade_list:
                        print(f"The highest grade is: {max(grade_list)}")
                        print(f"The lowest grade is: {min(grade_list)}")
                  else:
                        print("No grades available.")
      else:
            print("Thank you for using the Student Grade Management System. Goodbye!")
            exit()
elif choice == 3:
      print("Thank you for using the Student Grade Management System. Goodbye!")
      exit()