import csv
import os
from datetime import datetime
from collections import defaultdict

class ExpenseController:
    EXPENSES_FILE_PATH = 'C:\\Users\\ritik\\OneDrive\\Desktop\\Fynd_P\\ExpenseTrackerApplication\\data\\expenses.csv'

    @classmethod
    def menu(cls, username):
        expense = ExpenseController()
        print("1. Add expenses")
        print("2. Records of all expenses")
        print("3. Update the expenses")
        print("4. Delete Expenses")
        print("5. Expenses by category")
        print("6.Exit")
        entry = input("Choose your option: ")
        if entry == '1':
            expense.add_expense(username)
            expense.menu()
        elif entry == '2':
            expense.view_expenses(username)
            expense.menu()
        elif entry == '3':
            expense.view_expenses(username)
            print("Use this records what you wan tto update in your expenses")
            expense.update_expense(username)
            expense.menu()
        elif entry =='4': 
            expense.view_expenses(username)
            print("Use this records what you want to delete in your expenses")
            expense.delete_expense(username)
            expense.menu()
        elif entry =='5':
             expense.view_expenses_by_category()
        elif entry =='6':
            return
        else:
            return expense.menu()

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.EXPENSES_FILE_PATH):
            with open(cls.EXPENSES_FILE_PATH, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['username', 'category', 'expense_name', 'amount', 'date'])
            print(f"Created '{cls.EXPENSES_FILE_PATH}' with headers: username, category, expense_name, amount, date.")
        else:
            print(f"'{cls.EXPENSES_FILE_PATH}' already exists.")

    @classmethod
    def add_expense(cls, username):
        category = input("Category for expense: ")
        expense_name = input("What is the product/service name? ")
        amount = input("What is the price you have spent for it? ")
        date = datetime.now().strftime('%Y-%m-%d')

        with open(cls.EXPENSES_FILE_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, category, expense_name, amount, date])
        print(f"Expense '{expense_name}' of '{category}' for amount {amount} added for user '{username}' on '{date}'.")

    @classmethod
    def view_expenses(cls, username):
        if not os.path.exists(cls.EXPENSES_FILE_PATH):
            print("No expenses file found.")
            return

        with open(cls.EXPENSES_FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            user_expenses = [row for row in reader if row and row[0] == username]

        if user_expenses:
            print(f"\nExpenses for user '{username}':")
            print("+" + "-" * 13 + "+" + "-" * 20 + "+" + "-" * 10 + "+" + "-" * 10 + "+")
            print(f"| {'Category':<13} | {'Expense Name':<18} | {'Amount':<8} | {'Date':<10} |")
            print("+" + "-" * 13 + "+" + "-" * 20 + "+" + "-" * 10 + "+" + "-" * 10 + "+")

            for row in user_expenses:
                print(f"| {row[1]:<13} | {row[2]:<18} | {row[3]:<8} | {row[4]:<10} |")

            print("+" + "-" * 13 + "+" + "-" * 20 + "+" + "-" * 10 + "+" + "-" * 10 + "+")
        else:
            print(f"No expenses found for user '{username}'.")

    @classmethod
    def update_expense(cls, username):
        """Update an expense for a specific user."""
        if not os.path.exists(cls.EXPENSES_FILE_PATH):
            print("No expenses file found.")
            return

        with open(cls.EXPENSES_FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            expenses = list(reader)

        header = expenses[0]
        user_expenses = [row for row in expenses if row[0] == username]

        if not user_expenses:
            print(f"No expenses found for user '{username}'.")
            return

        print("Select an expense to update:")
        for index, row in enumerate(user_expenses):
            print(f"{index + 1}. {row[1]} - {row[2]} - {row[3]} - {row[4]}")

        try:
            choice = int(input("Enter the number of the expense to update: ")) - 1
            if not (0 <= choice < len(user_expenses)):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        expense_to_update = user_expenses[choice]

        print("Leave the field blank if you don't want to update it.")
        new_category = input(f"New category (current: {expense_to_update[1]}): ") or expense_to_update[1]
        new_expense_name = input(f"New expense name (current: {expense_to_update[2]}): ") or expense_to_update[2]
        new_amount = input(f"New amount (current: {expense_to_update[3]}): ") or expense_to_update[3]
        new_date = input(f"New date (current: {expense_to_update[4]}): ") or expense_to_update[4]

        
        updated_expense = [username, new_category, new_expense_name, new_amount, new_date]
        for i, expense in enumerate(expenses):
            if expense == expense_to_update:
                expenses[i] = updated_expense
                break

        
        with open(cls.EXPENSES_FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)

        print("Expense updated successfully.")


    @classmethod
    def update_expense(cls, username):
        """Update an expense for a specific user."""
        if not os.path.exists(cls.EXPENSES_FILE_PATH):
            print("No expenses file found.")
            return

        with open(cls.EXPENSES_FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            expenses = list(reader)

        header = expenses[0]
        user_expenses = [row for row in expenses if row[0] == username]

        if not user_expenses:
            print(f"No expenses found for user '{username}'.")
            return

        print("Select an expense to update:")
        for index, row in enumerate(user_expenses):
            print(f"{index + 1}. {row[1]} - {row[2]} - {row[3]} - {row[4]}")

        try:
            choice = int(input("Enter the number of the expense to update: ")) - 1
            if not (0 <= choice < len(user_expenses)):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        expense_to_update = user_expenses[choice]

        new_category = input(f"New category (current: {expense_to_update[1]}): ")
        new_amount = input(f"New amount (current: {expense_to_update[3]}): ")
        new_date = datetime.now().strftime('%Y-%m-%d')

        
        updated_expense = [
            username,
            new_category or expense_to_update[1],
            expense_to_update[2],  
            new_amount or expense_to_update[3],
            new_date  
        ]

        for i, expense in enumerate(expenses):
            if expense == expense_to_update:
                expenses[i] = updated_expense
                break

        # Write the updated list back to the CSV
        with open(cls.EXPENSES_FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)

        print("Expense updated successfully.")

    @classmethod
    def delete_expense(cls, username):
        """Delete an expense for a specific user by its unique name."""
        if not os.path.exists(cls.EXPENSES_FILE_PATH):
            print("No expenses file found.")
            return

        with open(cls.EXPENSES_FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            expenses = list(reader)

        header = expenses[0]
        user_expenses = [row for row in expenses if row[0] == username]

        if not user_expenses:
            print(f"No expenses found for user '{username}'.")
            return

        print("Select an expense to delete:")
        for index, row in enumerate(user_expenses):
            print(f"{index + 1}. {row[1]} - {row[2]} - {row[3]} - {row[4]}")

        try:
            choice = int(input("Enter the number of the expense to delete: ")) - 1
            if not (0 <= choice < len(user_expenses)):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        expense_to_delete = user_expenses[choice]


        confirmation = input(f"Are you sure you want to delete '{expense_to_delete[2]}'? (yes/no): ").strip().lower()
        if confirmation != 'yes':
            print("Deletion canceled.")
            return


        expenses.remove(expense_to_delete)
        with open(cls.EXPENSES_FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(expenses)

        print(f"Expense '{expense_to_delete[2]}' deleted successfully.")


    @classmethod
    def view_expenses_by_category(cls, username):
        """Display expenses grouped by category for a specific user."""
        if not os.path.exists(cls.EXPENSES_FILE_PATH):
            print("No expenses file found.")
            return

        with open(cls.EXPENSES_FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            user_expenses = [row for row in reader if row and row[0] == username]

        if not user_expenses:
            print(f"No expenses found for user '{username}'.")
            return

        # Aggregate expenses by category
        category_data = defaultdict(lambda: {"count": 0, "total_amount": 0, "products": []})

        for row in user_expenses:
            category = row[1]
            expense_name = row[2]
            amount = float(row[3])

            category_data[category]["count"] += 1
            category_data[category]["total_amount"] += amount
            category_data[category]["products"].append(expense_name)

        # Display the result
        print(f"\nExpenses for user '{username}' by category:")
        print("+" + "-" * 20 + "+" + "-" * 10 + "+" + "-" * 15 + "+" + "-" * 40 + "+")
        print(f"| {'Category':<18} | {'Count':<8} | {'Total Amount':<13} | {'Products':<38} |")
        print("+" + "-" * 20 + "+" + "-" * 10 + "+" + "-" * 15 + "+" + "-" * 40 + "+")

        for category, data in category_data.items():
            products = ", ".join(data["products"])
            print(f"| {category:<18} | {data['count']:<8} | {data['total_amount']:<13.2f} | {products:<38} |")

        print("+" + "-" * 20 + "+" + "-" * 10 + "+" + "-" * 15 + "+" + "-" * 40 + "+")
