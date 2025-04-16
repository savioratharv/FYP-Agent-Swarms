# File Name: utils.py
# 
# Description: 
# This module provides utility functions to assist with task management within an application. The primary function included is display_tasks, which is responsible for displaying a list of tasks to the user in a numbered format.
# 
# Function Documentation:
# 
# 1. Function Name: display_tasks
#    Purpose: 
#    Displays a list of tasks to the user with each task enumerated. This function enhances user interaction by presenting tasks in a clear and organized manner.
# 
#    Parameters:
#    - tasks (list): A list of strings, where each string represents a task. This list must be non-empty and contain valid string elements.
# 
#    Returns: 
#    This function does not return any value. It outputs the tasks to the standard output.
# 
#    Description of Behavior: 
#    The function prints a header "Your Tasks:" followed by the list of tasks. Each task is prefixed with its corresponding number, beginning with 1. The enumeration aids in identifying each task easily, facilitating user tasks management.
# 
#    Example:
#    If the input list of tasks is ["Task 1", "Task 2", "Task 3"], the output will be:
#    Your Tasks:
#    1. Task 1
#    2. Task 2
#    3. Task 3
# 
# Notes:
# - It is important that the 'tasks' list is properly formatted and does not contain any non-string types to avoid unexpected results.
# - This function is designed to be called after the tasks are defined and populated, ensuring that the user sees the most current task list.

def display_tasks(tasks):
    """def display_tasks(tasks):
    ""\"Display a numbered list of tasks.

    This function takes a list of tasks and prints them to the console in a 
    clear, enumerated format, allowing users to easily view and manage their tasks.

    Parameters:
    tasks (list of str): A list of task descriptions, where each task is a 
                         string. The list must be non-empty.

    Returns:
    None: This function does not return a value; it prints the tasks directly 
          to standard output.

    Example:
    >>> tasks = ["Finish report", "Email client", "Prepare presentation"]
    >>> display_tasks(tasks)
    Your Tasks:
    1. Finish report
    2. Email client
    3. Prepare presentation
    """
    print('\nYour Tasks:')
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task}')
