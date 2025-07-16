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
