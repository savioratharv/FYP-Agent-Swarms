# """
# Task Manager Module Documentation
# 
# Module Name: task_manager.py
# 
# Description:
# This module defines the TaskManager class, which provides functionalities to manage a list of tasks.
# The primary operations include adding, removing, and listing tasks. The tasks are persisted using 
# external functions for saving and loading from a JSON file. This module operates within a larger 
# software application that manages user-defined tasks.
# 
# Classes:
# - TaskManager: A class responsible for managing a list of tasks. It provides methods to add, 
#   remove, and list tasks, closely integrating with external storage functionalities.
# 
# Methods:
# - __init__(self):
#     Initializes a new instance of the TaskManager class. On instantiation, it loads tasks from 
#     an external JSON file using the load_tasks function. The tasks are stored in an instance 
#     variable for internal management.
# 
# - add_task(self, task):
#     Adds a new task to the internal task list.
#     
#     Parameters:
#     task (str): A string representing the task to be added. 
# 
#     This method appends the task to the list, saves the updated task list to the external 
#     JSON file using the save_tasks function, and provides feedback to the user indicating that 
#     the task has been successfully added.
# 
# - remove_task(self, task):
#     Removes a specified task from the internal task list if it exists.
# 
#     Parameters:
#     task (str): A string representing the task to be removed. 
#     
#     This method checks if the specified task is present in the internal task list. If found, 
#     it removes the task, updates the task list in the external JSON file using the save_tasks 
#     function, and provides feedback to the user. If the task is not found, it informs the user 
#     that the task does not exist.
# 
# - list_tasks(self):
#     Displays all tasks currently in the internal task list.
# 
#     This method calls the display_tasks function to present the tasks in a clear, enumerated 
#     format. If no tasks are available, it informs the user that there are no tasks to display.
# 
# Dependencies:
# This module relies on the following external functions defined in other files:
# - display_tasks: A function that takes a list of tasks and prints them to the console in a 
#   clear format.
# - save_tasks: A function that saves the current list of tasks to a JSON file.
# - load_tasks: A function that retrieves the list of tasks from a JSON file.
# 
# Usage Example:
# To use the TaskManager, create an instance and call its methods to manage tasks:
#     
#     manager = TaskManager()
#     manager.add_task("Complete project report")
#     manager.list_tasks()
#     manager.remove_task("Complete project report")
#     manager.list_tasks()
# 
# This documentation follows the IEEE 1016 standard for software design documentation and adheres 
# to the GNU coding standards for consistency.
# """

from storage import save_tasks, load_tasks
from utils import display_tasks


class TaskManager:

    def __init__(self):
        """
 Initializes a new instance of the TaskManager class.

 This constructor method loads tasks from an external JSON file using the `load_tasks` 
 function and stores them in an instance variable for further management. This setup 
 allows the TaskManager to operate with the previously saved tasks upon instantiation.

 Parameters:
 None

 Returns:
 None: This method does not return any value. It initializes the TaskManager instance 
       and populates the task list.

 Usage Example:
 >>> manager = TaskManager()
 >>> print(manager.tasks)  # Output will depend on the contents of 'tasks.json'
"""
        self.tasks = load_tasks()

    def add_task(self, task):
        """
 Adds a new task to the internal task list.

 This method appends a specified task to the list of current tasks and saves 
 the updated task list to an external JSON file using the `save_tasks` 
 function. It also provides feedback to the user about the operation's 
 success.

 Parameters:
 task (str): A string representing the task description to be added to the 
              task list.

 Returns:
 None: This method does not return any value. It performs an operation that 
       modifies the internal task list and the external storage.

 Usage Example:
 >>> manager = TaskManager()
 >>> manager.add_task("Complete the project report")
 Task 'Complete the project report' added.
 >>> print(manager.tasks)  # This will show the updated task list including the new task
"""
        self.tasks.append(task)
        save_tasks(self.tasks)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        """
 Removes a specified task from the internal task list if it exists.

 This method checks for the presence of the provided task in the list of current 
 tasks. If the task is found, it removes the task from the list and saves 
 the updated task list to an external JSON file using the `save_tasks` function. 
 The method also provides feedback to the user about the operation's success or 
 failure.

 Parameters:
 task (str): A string representing the task description to be removed from 
              the task list.

 Returns:
 None: This method does not return any value. It performs an operation that 
       modifies the internal task list and the external storage.

 Usage Example:
 >>> manager = TaskManager()
 >>> manager.add_task("Complete the project report")
 >>> manager.remove_task("Complete the project report")
 Task 'Complete the project report' removed.
 >>> print(manager.tasks)  # This will show the updated task list without the removed task
"""
        if task in self.tasks:
            self.tasks.remove(task)
            save_tasks(self.tasks)
            print(f"Task '{task}' removed.")
        else:
            print('Task not found.')

    def list_tasks(self):
        """
 Displays all tasks currently in the internal task list.

 This method checks the internal task list and uses the `display_tasks` function 
 to present the tasks in a clear, enumerated format. If no tasks are available, 
 it informs the user that there are no tasks to display.

 Parameters:
 None

 Returns:
 None: This method does not return any value. It performs an operation that 
       outputs task information to the console.

 Usage Example:
 >>> manager = TaskManager()
 >>> manager.add_task("Complete the project report")
 >>> manager.list_tasks()
 Your Tasks:
 1. Complete the project report
"""
        if self.tasks:
            display_tasks(self.tasks)
        else:
            print('No tasks available.')
