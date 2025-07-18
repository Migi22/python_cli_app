from todo_list import run as run_todo_list
from currency_converter import run as run_currency_converter
from quiz import run as run_quiz
from password_generator import run as run_password_generator
from alarm_clock import run as run_alarm_clock

def main():
    while True:
        print("""
        Welcome to the Python CLI App developed by Lance Miguel Damalerio!
        1. To-Do List
        2. Unit Converter
        3. Mini Quiz Game
        4. Password Generator
        5. Alarm Clock
        6. Exit
        """)

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            try:
                run_todo_list()
            except Exception as e:
                print("There is an error occured in To-Do list:", e)
        elif choice == "2":
            try:
                run_currency_converter()
            except Exception as e:
                print("There is an error occured in Currency Converter:", e)
        elif choice == "3":
            try:
                run_quiz()
            except Exception as e:
                print("There is an error occured in Mini Quiz Game:", e)
        elif choice == "4":
            try:
                run_password_generator()
            except Exception as e:
                print("There is an error occured in Password Generator:", e)
        elif choice == "5":
            try:
                run_alarm_clock()
            except Exception as e:
                print("There is an error in Alarm Clock:", e)
        elif choice == "6":
            print("\nThanks for using the toolkit!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()