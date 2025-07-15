from todo_list import run as run_todo_list
from unit_converter import run as run_unit_converter
from quiz import run as run_quiz
from password_generator import run as run_password_generator
from alarm_clock import run as run_alarm_clock

def main():
    while True:
        print("\nWelcome to the Python CLI App developed by Lance Miguel Damalerio" \
        "1. To-Do List" \
        "2. Unit Converter" \
        "3. Mini Quiz Game" \
        "4. Password Generator" \
        "5. Alarm Clock" \
        "6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            run_todo_list()
        elif choice == "2":
            run_unit_converter()
        elif choice == "3":
            run_quiz()
        elif choice == "4":
            run_password_generator()
        elif choice == "5":
            run_alarm_clock
        elif choice == "6":
            print("Thanks for using the toolkit!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()