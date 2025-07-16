from .add import add_task


def run():
    print("Todo List module running...") # placeholder logic for the actual to-do list implementation

    while True:
        print("""
            === TO-DO LIST MENU ===
            1. Add Task
            2. View Task
            3. Delete Task
            4. Mark Task as Done
            5. Back
        """)

        # Receive input and then strip the spaces includes.
        choice = input("Enter your choice (1-5): ").strip()
        
        # checks if the input are from 1-5 only.
        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        # Choices and the functions
        if choice == "1":
            print("add task")
            add_task()
        elif choice == "2":
            print("view task")
            #view_task()
        elif choice == "3":
            print("delete task")
            #delete_task()
        elif choice == "4":
            print("mark task")
            #mark_task()
        elif choice == "5":
            print("Returning to main menu...")
            break