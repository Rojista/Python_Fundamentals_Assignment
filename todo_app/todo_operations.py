
def add_task(task_list, task):
    """Adds a task to the list."""
    task_list.append(task)
    print(f"Task added: '{task}'")

def delete_task(task_list, index):
    """Deletes a task by its index from the list."""
    try:
        index = int(index)  # Convert input to integer
        task = task_list.pop(index)
        print(f"Task deleted: '{task}'")
    except (IndexError, ValueError):  # Handle invalid input
        print("Invalid index. Please enter a correct number.")

def view_tasks(task_list):
    """Displays all tasks in the list."""
    if not task_list:
        print("No tasks to display.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(task_list):
            print(f"{i}. {task}")