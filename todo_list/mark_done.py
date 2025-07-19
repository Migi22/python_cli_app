from .todo_list_utils import load_tasks, save_task
import emoji_util

# Function for marking done the task
def mark_done():
    """
    Prompts the user to select a task to mark it as Done.
    Then saves the changes.
    """
    print("\nMark done a Task...")

    # Load the current tasks
    tasks = load_tasks()

    # Checks if the task is empty
    if not tasks:
        print(f"\n{emoji_util.NOTE}The task is empty. Nothing to mark as Done.")
        return

    # Looping and printing the task
    print(f"\n{emoji_util.QUESTION}Which task do you want to mark as done?\n")
    for index, task in enumerate(tasks, start=1):
        status = emoji_util.CHECK if task.get("done") else emoji_util.CROSS
        print(f"{index}.{task['name']} {status}")

    while True:
        try:
            choice = int(input("\nEnter the number of the task to mark as Done: "))
            if 1 <= choice <= len(tasks):
                break
            else:
                print(f"Please enter a number between 1 and {len(tasks)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number")

    # This will access and update the selected task
    selected_task = tasks[choice - 1]
    if selected_task["done"]:
        print(f"\n{emoji_util.CHECK} The task has already been mark as done.")
    else:
        selected_task["done"] = True
        save_task(task)
        print(f'\n{emoji_util.CHECK} Task "{selected_task["name"]}" marked as done!')