from .utils import load_tasks, save_task
import emoji_util

# Function for deleting a task
def delete_task():
    """
    Prompts the user to  select a task to be deleted.
    Then save the changes
    """

    # Load the current tasks
    tasks = load_tasks()

    # Checks if the task is empty
    if not tasks:
        print(f"\n{emoji_util.NOTE}The task is empty. Nothing to be remove.")
        return

    # Looping and printing the task
    print(f"\n{emoji_util.QUESTION}Which task do you want to mark as Delete?\n")
    for index, task in enumerate(tasks, start=1):
        status = emoji_util.CHECK if task.get("done") else emoji_util.CROSS
        print(f"{index}.{task['name']} {status}")

    while True:
        try:
            choice = int(input("\nEnter the number of the task to be remove: "))
            if 1 <= choice <= len(tasks):
                break
            else:
                print(f"Please enter a number between 1 and {len(tasks)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number")

    # Remove the task from the list directly
    preview_task = tasks.pop(choice - 1)

    # Confirmation message
    confirm = input(f"Are you sure you want to delete '{preview_task['name']}'? (y/n): ").lower()
    if confirm != 'y':
        print("Cancelled.")
        return

    # Save updated list
    save_task(tasks)

    print(f'\n{emoji_util.CHECK} Task "{removed_task["name"]}" has been deleted!')