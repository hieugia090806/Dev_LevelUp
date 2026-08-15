#-- Project Title: PERSONAL EXPENSE TRACKER. --#
print("-" * 50)
print("Welcome to the Personal Expense Tracker!")
print("This program will help you keep track of your personal expenses.")
print("You can add, view, and manage your expenses easily.")
print("Let's get started!")
print("-" * 50)
#-- Generate expense list. --#
print("Dear User, Please enter your expenses in the following format: 'Expense Name, Amount'.")
expenses_list = []
amount = input("Enter the amount of your expense (At least three): ")
expenses_list = [int(x) for x in amount.split()]
print(f"Your current expenses are: {expenses_list}")
print("-" * 50)
#-- Insert New Expenses. --#
answer_add = str(input("Dear User, Do you want to add more expenses? (yes/no)?: "))
if answer_add.lower() == "yes":
    new_expense = input("Please enter new expenses: ")
    expenses_list.append(int(new_expense))
    print(f"Your updated expenses are: {expenses_list}")
    print("-" * 50)
    #-- Extra expenses. --#
    answer_extra = str(input("Dear User, Do you want to add extra expenses? (yes/no)?: "))
    if answer_extra.lower() == "yes":
        extra_list = []
        extra_expense = input("Please enter extra expenses: ")
        extra_list = [int(x) for x in extra_expense.split()]
        print(f"Your extra expenses are: {extra_list}")
        print("-" * 50)
        #-- Count total expenses. --#
        answer_total = str(input("Dear User, Do you want to view and calculate the total expenses? (yes/no)?: "))
        if answer_total.lower() == "yes":
            total_list = expenses_list + extra_list
            print(f"Your total expenses are: {total_list}")
            total_expenses = sum(total_list)
            print(f"Your total expenses are: {total_expenses}")
            print("-" * 50)
            #-- Remove by Index. --#
            answer_remove = str(input("Dear User, Do you want to remove an expense by index? (yes/no)?: "))
            if answer_remove.lower() == 'yes':
                index_to_remove = int(input("Please enter the index of the expense you want to remove: "))
                if index_to_remove in total_list:
                    total_list.remove(index_to_remove)
                    print(f"Updated expenses after removal: {total_list}")
                    print("-" * 50)
                    #-- Searching and Counting Index. --#
                    search_index = str(input("Dear User, Do you want to search for an expense by index? (yes/no)?: "))
                    if search_index.lower() == 'yes':
                        index_to_search = int(input("Please enter the index of the expense you want to search for: "))
                        if index_to_search in total_list:
                            count = total_list.count(index_to_search)
                            print(f"The expense {index_to_search} appears {count} times in the list.")
                            print("-" * 50)
                            #-- Sorting and Reversing. --#
                            sort_reverse = str(input("Dear User, Do you want to sort and reverse the expenses? (yes/no)?: "))
                            if sort_reverse.lower() == 'yes':
                                total_list.sort()
                                print(f"Sorted expenses: {total_list}")
                                total_list.reverse()
                                print(f"Reversed expenses: {total_list}")
                                print("-" * 50)
                                print("SUMMARY: Your final expenses list is:", total_list)
                                print("Goodbye! Thank you for using the Personal Expense Tracker.")
                            else:
                                print("Sorting and reversing skipped.")
                                print("Goodbye! Thank you for using the Personal Expense Tracker.")
                        else:
                            print(f"The expense {index_to_search} is not found in the list.")
                            print("Goodbye! Thank you for using the Personal Expense Tracker.")
                else:
                    print("Invalid index. No expenses removed.")
                    print("Goodbye! Thank you for using the Personal Expense Tracker.")
            else:
                print("No expenses removed.")
                print("Goodbye! Thank you for using the Personal Expense Tracker.")
        else:
            print("Total expenses calculation skipped.")
            print("Goodbye! Thank you for using the Personal Expense Tracker.")
    else:
        print("No extra expenses added.")
        print("Goodbye! Thank you for using the Personal Expense Tracker.")
else:
    print("No new expenses added.")
    print("Goodbye! Thank you for using the Personal Expense Tracker.")