# """
# task_manager.py
# 
# This module defines the TaskManager class, which provides functionality to manage a list of tasks. This includes adding, removing, and listing tasks. The TaskManager relies on external functions to load and save tasks to a JSON file, facilitating persistent storage across sessions.
# 
# Classes:
#     TaskManager: A class that manages tasks, allowing the user to add, remove, and list tasks.
# 
# TaskManager Class:
#     __init__(self):
#         Initializes the TaskManager instance by loading tasks from a JSON file.
# 
#         This constructor initializes the TaskManager by retrieving any previously saved tasks from 'tasks.json'. 
#         If the file contains invalid JSON or does not exist, an empty list of tasks is created.
# 
#         Parameters:
#             self: The instance of TaskManager being created.
# 
#         Returns:
#             None
# 
#         Usage Example:
#             >>> task_manager = TaskManager()
#             >>> print(task_manager.tasks)  # Output may vary based on saved tasks
#     
#     add_task(self, task):
#         Adds a new task to the list of tasks.
# 
#         This method appends the specified task to the internal list of tasks and saves the updated list to a JSON file. 
#         It also prints a confirmation message indicating that the task has been successfully added.
# 
#         Parameters:
#             self: The instance of TaskManager in which the task is being added.
#             task (str): The description of the task to be added.
# 
#         Returns:
#             None
# 
#         Usage Example:
#             >>> task_manager = TaskManager()
#             >>> task_manager.add_task('Buy groceries')
#             Task 'Buy groceries' added.
#             >>> print(task_manager.tasks)
#             ['Buy groceries']
# 
#     remove_task(self, task):
#         Removes a specified task from the list of tasks.
# 
#         This method checks if the given task exists in the internal list of tasks. 
#         If the task is found, it is removed, and the updated list is saved to a JSON file. 
#         If the task is not found, an error message is printed.
# 
#         Parameters:
#             self: The instance of TaskManager in which the task is being removed.
#             task (str): The description of the task to be removed.
# 
#         Returns:
#             None
# 
#         Usage Example:
#             >>> task_manager = TaskManager()
#             >>> task_manager.add_task('Complete project')
#             Task 'Complete project' added.
#             >>> task_manager.remove_task('Complete project')
#             Task 'Complete project' removed.
#             >>> print(task_manager.tasks)
#             []
# 
#     list_tasks(self):
#         Displays all existing tasks to the user.
# 
#         This method retrieves the current list of tasks and, if available, calls the 
#         external function `display_tasks` to print them in a numbered format. 
#         If there are no tasks, it prints a message indicating that no tasks are available.
# 
#         Parameters:
#             self: The instance of TaskManager from which tasks are being listed.
# 
#         Returns:
#             None
# 
#         Usage Example:
#             >>> task_manager = TaskManager()
#             >>> task_manager.add_task('Write report')
#             Task 'Write report' added.
#             >>> task_manager.list_tasks()
#             Your Tasks:
#             1. Write report
# 
# External Functions:
# The TaskManager class uses the following functions defined in other files:
# 
# - display_tasks(tasks): Displays a list of tasks in a numbered format. This function is essential for presenting tasks to the user in an organized and clear manner.
# 
# - load_tasks(): Loads a list of tasks from a JSON file named 'tasks.json'. If the file does not exist or contains invalid JSON, it returns an empty list.
# 
# - save_tasks(tasks): Saves a list of tasks to a JSON file named 'tasks.json'. This function writes the provided list in JSON format, overwriting any existing data in the file.
# 
# This module facilitates efficient task management by allowing users to create, delete, and view tasks while ensuring data persistence.
# """

from storage import save_tasks, load_tasks
from utils import display_tasks


class TaskManager:

    def __init__(self):
        """
    __init__(self):
        Initialize the TaskManager instance by loading tasks from a JSON file.

        This constructor initializes the TaskManager by retrieving any previously saved tasks from 'tasks.json'. 
        If the file contains invalid JSON or does not exist, an empty list of tasks is created.

        Parameters:
            self: The instance of TaskManager being created. 

        Returns:
            None

        Usage Example:
            >>> task_manager = TaskManager()
            >>> print(task_manager.tasks)  # Output may vary based on saved tasks
"""
        self.tasks = load_tasks()

    def add_task(self, task):
        """
    add_task(self, task):
        Add a new task to the list of tasks.

        This method appends the specified task to the internal list of tasks and saves the updated list to a JSON file. 
        It also prints a confirmation message indicating that the task has been successfully added.

        Parameters:
            self: The instance of TaskManager in which the task is being added.
            task (str): The description of the task to be added.

        Returns:
            None

        Usage Example:
            >>> task_manager = TaskManager()
            >>> task_manager.add_task('Buy groceries')
            Task 'Buy groceries' added.
            >>> print(task_manager.tasks)
            ['Buy groceries']
"""
        self.tasks.append(task)
        save_tasks(self.tasks)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        """
    remove_task(self, task):
        Remove a specified task from the list of tasks.

        This method checks if the given task exists in the internal list of tasks. 
        If the task is found, it is removed, and the updated list is saved to a JSON file. 
        If the task is not found, an error message is printed.

        Parameters:
            self: The instance of TaskManager in which the task is being removed.
            task (str): The description of the task to be removed.

        Returns:
            None

        Usage Example:
            >>> task_manager = TaskManager()
            >>> task_manager.add_task('Complete project')
            Task 'Complete project' added.
            >>> task_manager.remove_task('Complete project')
            Task 'Complete project' removed.
            >>> print(task_manager.tasks)
            []
"""
        if task in self.tasks:
            self.tasks.remove(task)
            save_tasks(self.tasks)
            print(f"Task '{task}' removed.")
        else:
            print('Task not found.')

    def list_tasks(self):
        """
    list_tasks(self):
        Display all existing tasks to the user.

        This method retrieves the current list of tasks and, if available, calls the 
        external function `display_tasks` to print them in a numbered format. 
        If there are no tasks, it prints a message indicating that no tasks are available.

        Parameters:
            self: The instance of TaskManager from which tasks are being listed.

        Returns:
            None

        Usage Example:
            >>> task_manager = TaskManager()
            >>> task_manager.add_task('Write report')
            Task 'Write report' added.
            >>> task_manager.list_tasks()
            Your Tasks:
            1. Write report
"""
        if self.tasks:
            display_tasks(self.tasks)
        else:
            print('No tasks available.')
