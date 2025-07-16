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
        print(f"\n{emoji_util.NOTE}The task list is empty. Nothing to be remove.")
        return

    # Looping and printing the task
    print(f"\n{emoji_util.QUESTION}Which task do you want to mark as Delete?\n")
    for index, task in enumerate(tasks, start=1):
        status = emoji_util.CHECK if task.get("done") else emoji_util.CROSS
        print(f"{index}.{task['name']} {status}")

    while True:
        try:
            choice = int(input("\nEnter the number of the task to delete: "))
            if 1 <= choice <= len(tasks):
                break
            else:
                print(f"Please enter a number between 1 and {len(tasks)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number")

    # Preview the selected task without removing it yet
    preview_task = tasks[choice - 1]
    print(f"\nSelected Task:")
    print(f"  Name: {preview_task['name']}")
    print(f"  Description: {preview_task['description']}")
    print(f"  Time: {preview_task['time']}")
    print(f"  Status: {'✔️ Done' if preview_task['done'] else '❌ Not done'}")

    # Confirmation message
    confirm = input(f"Are you sure you want to delete '{preview_task['name']}'? (y/n): ").lower()
    if confirm != 'y':
        print("Cancelled.")
        return

    # Delete after confirmation
    del tasks[choice - 1]

    # Save updated list
    save_task(tasks)

    print(f'\n{emoji_util.CHECK} Task "{preview_task["name"]}" has been deleted!')