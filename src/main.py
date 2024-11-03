from user_controller import UserController

def main():
    user_controller = UserController()  # Initialize the UserController, which also sets up the CSV file if it doesn't exist

    while True:
        print("\n--- Expense Tracker Application ---")
        print("1. Sign up")
        print("2. Log in")
        print("3. Exit ")

        choice = input("Choose an option (1/2): ")

        if choice == '1':
            user_controller.signup() 
        elif choice == '2':
            user_controller.login()
        elif choice =='3':
            print("Exiting the application")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
