
# Welcome the user
print("Welcome to the homework chatbot!")

# Collect the user's name and age
name = input("What is your name? ")
age = input("How old are you? ")

print(f"Hi {name}, age {age}! How can I assist you today?")

# Display a menu of options
while True:
    print("\nPlease choose an option from the menu below:")
    print("1. Placeholder Option 1")
    print("2. Placeholder Option 2")
    print("3. Exit the conversation")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You selected Placeholder Option 1. (This will be implemented later.)")
    elif choice == "2":
        print("You selected Placeholder Option 2. (This will be implemented later.)")
    elif choice == "3":
        print("Goodbye! Thank you for chatting with me.")
        break
    else:
        print("Invalid choice. Please select a valid option.")