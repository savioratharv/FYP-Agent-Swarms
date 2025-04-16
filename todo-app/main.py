# """
# main.py
# 
# This Python script serves as the entry point for a TODO application. The application utilizes the TaskManager class from the 'task_manager' module to manage a list of tasks. Users can add, remove, and list tasks through a simple command-line interface. The program operates in an infinite loop, allowing continuous user interaction until the user decides to exit.
# 
# Dependencies:
# - TaskManager: This class is responsible for managing tasks including adding new tasks, removing existing ones, and listing all tasks. It ensures that tasks are persistently stored by loading and saving them to an external JSON file.
# 
# Functions:
# - main():
#     The main function contains the primary logic of the TODO application. It creates an instance of TaskManager and presents a menu to the user for interacting with tasks. 
# 
#     Workflow:
#     1. Display the main menu with options to add, remove, list tasks, or exit the application.
#     2. Accept user input for their menu choice.
#     3. Depending on the user's choice:
#        - Option 1: Prompt the user to enter a task to add to the task manager.
#        - Option 2: Prompt the user to enter a task to remove from the task manager.
#        - Option 3: Call the task manager's method to list current tasks.
#        - Option 4: Exit the application and terminate the program.
#        - Handle invalid choices and prompt the user to try again.
# 
# Usage:
# This script is intended to be run in a command-line environment. Upon execution, it initializes the task manager and continuously prompts the user until they choose to exit. Users interact by entering choices corresponding to the displayed options.
# 
# Notes:
# The TaskManager class is expected to handle the underlying logic concerning the storage and retrieval of tasks. It is assumed that error handling for task operations is managed within the TaskManager class.
# 
# Example Interaction:
# - User initiates the program and is presented with the main menu.
# - User selects '1' to add a task, enters a task description, and sees confirmation.
# - User can repeat the process for removing tasks or listing current tasks.
# - User selects '4' to exit the application.
# """

from task_manager import TaskManager


def main():
    """
Main function to run the TODO application.

This function serves as the entry point for the TODO application, providing a command-line interface that allows users to manage their tasks. Users can add tasks, remove tasks, list all tasks, or exit the application. The function operates in a loop to facilitate continuous interaction until the user decides to exit.

Parameters:
None

Returns:
None: This function does not return any value. It runs indefinitely until the user opts to exit.

Usage Example:
>>> if __name__ == '__main__':
...     main()
"""
    manager = TaskManager()
    while True:
        print('\nTODO App')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. List Tasks')
        print('4. Exit')
        choice = input('Enter choice: ').strip()
        if choice == '1':
            task = input('Enter task: ').strip()
            manager.add_task(task)
        elif choice == '2':
            task = input('Enter task to remove: ').strip()
            manager.remove_task(task)
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            print('Exiting TODO App.')
            break
        else:
            print('Invalid choice. Try again.')


if __name__ == '__main__':
    main()
