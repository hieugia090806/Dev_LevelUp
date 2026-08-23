#---------------------- GRADE MANAGEMENT SYSTEM. ----------------------#
#-- Student Class: Manage each student information (name and grade). --#
class Student:
    #-- Constructor def. --#
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    #-- Classify Students based on Grade Level. --#
    def classification(self):
        if 50 <= self.grade < 60:
            return "Pass(P)"
        elif 60 <= self.grade < 70:
            return "Credit(C)"
        elif 70 <= self.grade < 80:
            return "Distinction(D)"
        elif 80 <= self.grade < 90:
            return "High Distinction(HD1)"
        elif 90 <= self.grade <= 100:
            return "High Distinction(HD2)"
        else:
            return "Fail(F)"

#------------------- Grade Student Management Class. -------------------#
class GradeManagementSystem:
    def __init__(self):
        self.students = {}

    #-- Function add_student(). --#
    def add_student(self):
        names = input("Please enter student names separated by spaces: ").split()
        while True:
            try:
                grades = list(map(int,input("Enter student grades separated by spaces: ").split()))
                if len(names) != len(grades):
                    print("Number of names and grades must match.")
                    continue
                valid = True
                for grade in grades:
                    if grade < 0 or grade > 100:
                        valid = False
                        break
                if valid:
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid grade. Please enter integers only.")
        for name, grade in zip(names, grades):
            student = Student(name, grade)
            self.students[name] = student
        print("NOTIFICATION: Students added successfully!")

    #-- Function lookup_student(). --#
    def lookup_student(self):
        if len(self.students) == 0:
            print("No student records found.")
            return

        search_name = input("Enter student name to search: ")

        if search_name in self.students:

            student = self.students[search_name]

            print("\nStudent Found")
            print("--------------------")
            print("Name:", student.name)
            print("Grade:", student.grade)
            print("Result:", student.classification())

        else:
            print("Student not found.")

    #-- Function AvgGrade(). --#
    def avg_grade(self):
        if len(self.students) == 0:
            print("No student records found.")
            return

        total = 0

        for student in self.students.values():
            total += student.grade

        average = total / len(self.students)

        print(f"Average Grade: {average:.2f}")

    #-- Function ranking Students. --#
    def show_student_ranking(self):
        if len(self.students) == 0:
            print("No student records found.")
            return

        rankings = {
            "Fail(F)": [],
            "Pass(P)": [],
            "Credit(C)": [],
            "Distinction(D)": [],
            "High Distinction(HD1)": [],
            "High Distinction(HD2)": []
        }

        for student in self.students.values():
            result = student.classification()
            rankings[result].append(student)

        for category, student_list in rankings.items():

            print(f"\n{category.upper()} STUDENTS")
            print("-" * 30)

            if len(student_list) == 0:
                print("None")

            else:

                student_list.sort(
                    key=lambda student: student.grade,
                    reverse=True
                )

                for student in student_list:
                    print(
                        f"{student.name:<15}"
                        f"{student.grade}"
                    )

    #-- Function Display all Students. --#
    def display_all_students(self):
        if len(self.students) == 0:
            print("No student records found.")
            return

        print("\nAll Students")
        print("------------------------------")

        for student in self.students.values():
            print(
                f"Name: {student.name:<15}"
                f" Grade: {student.grade:<6}"
                f" Result: {student.classification()}"
            )

    #-- Function login(). --#
    def login(self):
        print("===================================")
        print("WELCOME TO GRADE MANAGEMENT SYSTEM")
        print("===================================")

        while True:
            username = input("Please enter your name: ")

            confirm = input(
                f"Is '{username}' correct? (Y/N): "
            ).lower()

            if confirm == "y" or confirm == "yes":
                print(f"\nWelcome {username}!")
                break

            elif confirm == "n" or confirm == "no":
                print("Please enter your name again.\n")

            else:
                print("Invalid input. Please enter Y or N.")

    #-- Function menu(). --#
    def menu(self):
        while True:
            print("========== MENU ==========")
            print("1. Add Student")
            print("2. Look Up Student")
            print("3. Calculate Average Grade")
            print("4. Ranking Students")
            print("5. Display All Students")
            print("6. Exit")
            print("==========================")

            try:
                choice = int(input("Enter your choice (MUST BE INTEGER): "))
            except ValueError:
                print("Invalid choice.")
                continue

            if choice == 1:
                self.add_student()

            elif choice == 2:
                self.lookup_student()

            elif choice == 3:
                self.avg_grade()

            elif choice == 4:
                self.show_student_ranking()

            elif choice == 5:
                self.display_all_students()

            elif choice == 6:
                print("\nThank you for using GMS.")
                print("Bye Bye!")
                break

            else:
                print("Invalid choice.")
                continue

            while True:
                again = input(
                    "\nDo you want to continue? (Y/N): "
                ).lower()

                if again == "y" or again == "yes":
                    break

                elif again == "n" or again == "no":
                    print("\nThank you for using GMS.")
                    print("Bye Bye!")
                    return

                else:
                    print("Please enter Y or N.")

#-- Main Program. --#
gms = GradeManagementSystem()
gms.login()
gms.menu()