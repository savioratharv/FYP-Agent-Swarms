# """
# main.py
# 
# TODO Application:
#     This module implements a command-line interface (CLI) for a simple To-Do application, allowing users to manage tasks through a console-based system. The application supports functionalities for adding, removing, and listing tasks as part of its task management capabilities.
# 
#     The primary function of this module is to create and manage an instance of the TaskManager class, which is responsible for executing task-related operations. The program continuously presents a menu to the user until a choice is made to exit the application.
# 
# Functions:
#     main() -> None
#         The main entry point of the To-Do application. It initializes an instance of the TaskManager class and orchestrates a command-line interface for user interaction. The function manages a loop that displays menu options and handles user input accordingly. Based on the user's selection, it calls corresponding methods from the TaskManager to facilitate task management.
# 
#         Parameters:
#             None
# 
#         Returns:
#             None
# 
#         Usage Example:
#             Upon execution, the program displays a menu prompt to the user:
#             
#             TODO App
#             1. Add Task
#             2. Remove Task
#             3. List Tasks
#             4. Exit
#             
#             Users may enter their choice to manage tasks appropriately.
# 
# Error Handling:
#     The main function includes basic error handling for user input. If the user selects an option that does not correspond to the provided menu choices, an error message is displayed, prompting the user to try again.
# 
# Initialization:
#     The TaskManager instance is initialized at the beginning of the main() function. This instance is utilized to manage tasks throughout the application's lifecycle.
# 
# Termination:
#     The application will terminate when the user selects the option to exit. Before exiting, a message confirming the exit will be displayed to the user.
# """

from task_manager import TaskManager


def main():
    """    
Main entry point of the TODO application.

This function initializes an instance of the TaskManager class and presents 
a command-line interface to the user for managing tasks. The user can add, 
remove, and list tasks through a menu-driven interface. The function 
continues to run in a loop until the user chooses to exit the application.

Parameters:
    None

Returns:
    None

Usage Example:
    When executed, the function will display a menu to the user:
    
    TODO App
    1. Add Task
    2. Remove Task
    3. List Tasks
    4. Exit

    The user can enter their choice to manage tasks accordingly.
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
