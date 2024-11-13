""" 1. In a new folder, todo_app, create the following modules to build a basic to-do list
application:
○ main.py: Handles user interaction with the app.
○ todo_operations.py: Contains functions to add, delete, and view tasks.
○ utils.py: Contains utility functions, like clearing the screen and reading user input.
2. Features to implement:
○ Display a menu for the user to:
■ Add a new to-do item.
■ View all to-do items.
■ Delete an item by its index.
○ Use if and while loops to keep the menu active until the user chooses to exit.
○ Test your app by adding a few items and deleting one.
 """

# main.py
import to do_operations  # Importing functions for task operations
import utils  # Importing utility functions

# List to store tasks
tasks = []
print("Welcome to Your To-Do List App!")
print("-------------------------------")

# Loop to display menu until the user decides to exit
while True:
    print("\nChoose an option:")
    print("1. Add a new task")
    print("2. Delete a task by index")
    print("3. View all tasks")
    print("4. Clear the screen")
    print("5. Exit")

    # Get the user's choice
    choice = input("Enter your choice: ")

    # Perform actions based on user's choice
    if choice == '1':
        new_task = input("Enter the task: ")
        todo_operations.add_task(tasks, new_task)
    elif choice == '2':
        index = input("Enter the index of the task to delete: ")
        todo_operations.delete_task(tasks, index)
    elif choice == '3':
        todo_operations.view_tasks(tasks)
    elif choice == '4':
        utils.clear_screen()
    elif choice == '5':
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

