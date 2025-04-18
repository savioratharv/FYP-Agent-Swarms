# File Name: utils.py
# 
# Description:
# This module provides utility functions for task management, specifically for displaying tasks in a formatted manner. It includes a function to enumerate and print a list of tasks, facilitating user interaction within a task management application.
# 
# Function List:
# 1. display_tasks(tasks: list) -> None
#    - Description: Prints the list of tasks to the console in a numbered format.
#    - Parameters:
#      - tasks (list): A list of strings representing the tasks to be displayed.
#    - Return Type: None
#    - Example Usage:
#      Given a list of tasks, the function will print each task preceded by its corresponding number.
# 
# Standards Compliance:
# This file adheres to the IEEE 1016 standards for structured documentation and follows the GNU coding standards for clarity and consistency in coding practices. All technical terms are defined, and language is kept simple to ensure comprehensibility for users of varying technical backgrounds. 
# 
# Function Documentation:
# def display_tasks(tasks):
#     """
#     Displays a list of tasks in a numbered format.
# 
#     This function takes a list of tasks and prints each task to the console, 
#     preceded by its corresponding number. It is designed to provide an organized 
#     view of tasks for better readability.
# 
#     Parameters:
#         tasks (list): A list of strings representing the tasks to be displayed.
# 
#     Returns:
#         None
# 
#     Example:
#         >>> tasks = ['Buy groceries', 'Complete homework', 'Walk the dog']
#         >>> display_tasks(tasks)
#         1. Buy groceries
#         2. Complete homework
#         3. Walk the dog
#     """

def display_tasks(tasks):
    """
Displays a list of tasks in a numbered format.

This function takes a list of tasks and prints each task to the console, 
preceded by its corresponding number. It is designed to provide an organized 
view of tasks for better readability.

Parameters:
    tasks (list): A list of strings representing the tasks to be displayed.

Returns:
    None

Example:
    >>> tasks = ['Buy groceries', 'Complete homework', 'Walk the dog']
    >>> display_tasks(tasks)
    1. Buy groceries
    2. Complete homework
    3. Walk the dog
"""
    print('\nYour Tasks:')
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task}')
