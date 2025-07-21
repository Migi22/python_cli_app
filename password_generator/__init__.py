from .password_util import generate_password, custom_password_generator

def run():
    print("\n\nLaunching Password Generator module...")

    # Welcome message
    print("""
    \nWelcome to the password generator of the toolkit. Have fun ;)
    """)

    while True:
        print("\n--- PASSWORD GENERATOR MENU ---")
        print("1. Generate Automated Password")
        print("2. Generate Custom Password")
        print("3. Go Back to Main Menu")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            print("Generated Password:", generate_password())
        elif choice == "2":
            custom_password_generator()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")