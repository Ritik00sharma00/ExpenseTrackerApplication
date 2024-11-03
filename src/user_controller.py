import csv
import os
import bcrypt

class UserController:
    FILE_PATH = 'C:\\Users\\ritik\\OneDrive\\Desktop\\Fynd_P\\ExpenseTrackerApplication\\data\\users.csv'

    def __init__(self):
        """Initialize the UserController and set up the CSV file if it doesn't exist."""
        self.initialize_csv()
        self.logged_in_user = None  # Track the logged-in user

    @classmethod
    def initialize_csv(cls):
        """Create the CSV file with headers if it doesn't already exist."""
        if not os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['username', 'password'])  
            print(f"Created '{cls.FILE_PATH}' with headers: username, password.")
        else:
            print(f"'{cls.FILE_PATH}' already exists.")

    @classmethod
    def user_exists(cls, username):
        """Check if a username already exists in users.csv."""
        print(f"Checking if user '{username}' exists.")
        if os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, 'r') as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    print(f"Found row: {row}")  # Debugging: print each row found
                    if row and row[0] == username:
                        print(f"User '{username}' exists.")
                        return True 
        print(f"User '{username}' does not exist.")
        return False  

    @classmethod
    def signup(cls):
        """Sign up a new user by saving their username and hashed password."""
        print("----- Signup for Expense Tracker -----")
        username = input("Enter a username: ")

        if cls.user_exists(username):
            print("Username already exists. Please choose a different one.")
            return

        password = input("Enter a password: ")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        with open(cls.FILE_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, hashed_password.decode('utf-8')]) 
            print(f"Created user: {username}")  # Debugging: confirm user creation

        print("Account created successfully!")

    @classmethod
    def login(cls):
        """Log in a user by checking their username and password."""
        print("----- Login to Expense Tracker -----")
        username = input("Enter your username: ")

        if not cls.user_exists(username):
            print("Username does not exist. Please sign up first.")
            return

        password = input("Enter your password: ")
        with open(cls.FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row and row[0] == username:
                    stored_password_hash = row[1]
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                        print("Login successful! Welcome.")
                        return
                    else:
                        print("Incorrect password. Please try again.")
                        return

        print("Login failed. Please check your username and password.")

    # def logout(self):
    #     """Log out the current user."""
    #     if self.logged_in_user:
    #         print(f"Logging out {self.logged_in_user}.")
    #         self.logged_in_user = None  # Clear the logged-in user
    #     else:
    #         print("No user is currently logged in.")
