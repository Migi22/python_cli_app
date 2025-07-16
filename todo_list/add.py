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
