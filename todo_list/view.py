from .utils import load_tasks
import emoji_util

def view_tasks():
    '''
    Loads tasks from the JSON file and display them in a numbered list.
    This will shows the task name, description, time, and whether it is done or not.
    '''

    # load the tasks
    tasks = load_tasks()

    # check if there is a task, if none then print message and return
    if not tasks:
        print(f"\n{emoji_util.LIST} No tasks found.")
        return

    print(f"\n{emoji_util.LIST} Your To-Do List:\n")

    for index, task in enumerate(tasks, start=1):
        status = f"{emoji_util.CHECK} Done" if task.get("done") else f"{emoji_util.CROSS} Not Done"
        print(f"{index}. {task['name']}")
        print(f'    {emoji_util.NOTE} Description: {task['description']}')
        print(f'    {emoji_util.CLOCK} Time: {task['time']}')
        print(f'    {emoji_util.PIN} Status: {status}')
    
    print("\n=== END OF THE VIEWING THE LIST OF TASKS ===")