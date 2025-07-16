from datetime import datetime
import json
import os

# Global name of the file so other functions in To-Do can use the same file
TODO_FILE = "todo.json"

# Will load the task
def load_tasks():
    """Load tasks from a JSON file. If not exists, return an empty list."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save the task to a JSON File
def save_task(tasks):
    """Save task list to JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=1)

# Function for adding task
def add_task():
    """
    Prompts the user to enter a task that includes name, description, and a time.
    Then saves the task to a local todo.json file.
    """
    print("\nAdding task...\n")
    task_name = input("What is the name of the task? ").strip()
    task_description = input("What is the description of the task? ").strip()
    
    while True:
        task_time_input = input("Enter task time (format: YYYY-MM-DD HH:MM): ").strip()
        try:
            # Wil try to parse the input to a datetime object
            task_time = datetime.strptime(task_time_input, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("You have entered an invalid time format. Please use YYYY-MM-DD HH:MM.")
        
    # Structure
    task = {
        "name": task_name,
        "description": task_description,
        "time": task_time.strftime("%Y-%m-%d %H:%M"), # this will store as string
        "done": False
    }

    # Load the current tasks
    tasks = load_tasks()

    # Add the new one
    tasks.append(task)

    # Save back to file
    save_task(tasks)

    print("\n Task added successfully!")
    print(task)

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
            #add_task()
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