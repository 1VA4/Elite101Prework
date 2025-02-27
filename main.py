import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to BankBot, your personal banking assistant!")

# Collect user details
name = input("What is your name? ")
age = int(input(f"Hello {name}, how old are you? "))

if age < 18:
    print("We're sorry, but you must be at least 18 years old to open an account online. Please visit a local branch with a guardian for assistance.")
else:
    print("Great! Let's find the best account type for you.")

    while True:
        clear_screen()
        print("\nPlease choose the type of account you are interested in:")
        print("1. Checking Account")
        print("2. Savings Account")
        print("3. Learn about Credit Cards")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        clear_screen()
        
        if choice == "1":
            print("A Checking Account is great for daily transactions, direct deposits, and bill payments.")
            overdraft = input("Would you like overdraft protection? (yes/no): ").strip().lower()
            if overdraft == "yes":
                print("Overdraft protection will be added to your account.")
            print("Let's proceed with your Checking Account application. Please visit our website or a local branch to complete the process.")
            input("Press Enter to return to the main menu...")
        
        elif choice == "2":
            print("A Savings Account helps you save money while earning interest.")
            goal = input("Do you have a specific savings goal in mind? (yes/no): ").strip().lower()
            if goal == "yes":
                savings_goal = input("Great! What are you saving for? ")
                print(f"That's a wonderful goal! A savings account will help you work towards {savings_goal}.")
            print("Let's proceed with your Savings Account application. Please visit our website or a local branch to complete the process.")
            input("Press Enter to return to the main menu...")
        
        elif choice == "3":
            print("Credit Cards can help you build credit and offer various rewards.")
            credit_history = input("Do you have prior credit history? (yes/no): ").strip().lower()
            if credit_history == "yes":
                print("Great! You may qualify for premium credit card options with better rewards.")
            else:
                print("No worries! We have starter credit cards that can help you build your credit score.")
            print("You can apply for a credit card online or at our nearest branch.")
            input("Press Enter to return to the main menu...")
        
        elif choice == "4":
            print("Thank you for using BankBot! If you have further questions, visit our website or contact customer support.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
            input("Press Enter to return to the main menu...")
