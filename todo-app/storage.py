# /****************************************************
#  * File: storage.py
#  * 
#  * Description: This Python module provides functionality for saving 
#  * and loading tasks from a JSON file. It defines two primary functions: 
#  * save_tasks and load_tasks. The tasks are stored in a 
#  * file named 'tasks.json' in a JSON format, allowing for easy 
#  * serialization and deserialization of task data.
#  *
#  * Functions:
#  * 
#  * save_tasks(tasks):
#  *   Saves the provided list of tasks to a JSON file. This function opens 
#  *   the specified file in write mode and writes the tasks to it in 
#  *   JSON format. If the operation is successful, the tasks are 
#  *   stored in the file for future retrieval.
#  *
#  * Parameters:
#  *   tasks (list): A list containing task data to be saved. The 
#  *   task data must be serializable to JSON format.
#  *
#  * load_tasks():
#  *   Loads and returns the tasks from the JSON file. This function attempts 
#  *   to open the specified file in read mode and parse its contents as 
#  *   JSON. If the file does not exist or is empty (leading to a 
#  *   JSONDecodeError), an empty list is returned. This enables safe 
#  *   retrieval of task data while handling potential file read errors.
#  *
#  * Returns:
#  *   list: A list of tasks loaded from the JSON file. If the file 
#  *   does not exist or is invalid, an empty list is returned.
#  * 
#  * Exception Handling:
#  *   The load_tasks function handles two specific exceptions:
#  *   - FileNotFoundError: Raised when the JSON file does not exist.
#  *   - json.JSONDecodeError: Raised when the file contains invalid JSON.
#  *
#  * Notes:
#  *   - The tasks are assumed to be in a format compatible with JSON
#  *   serialization.
#  *   - The storage file is fixed as 'tasks.json' and should be accessible 
#  *   in the current working directory of the program.
#  *   - This module is designed to be imported into other Python 
#  *   programs where task management is implemented.
#  ****************************************************/

import json
FILE_NAME = 'tasks.json'


def save_tasks(tasks):
    """def save_tasks(tasks):
    ""\"
    Save the provided list of tasks to a JSON file.

    This function opens the file named 'tasks.json' in write mode and 
    writes the tasks to it in JSON format. It effectively stores the 
    current state of tasks for future retrieval.

    Parameters:
    tasks (list): A list of tasks to be saved. Each task should be 
                  serializable to JSON format.

    Returns:
    None: This function does not return a value. It directly writes 
          to the file specified.

    Example:
    >>> tasks = [{'title': 'Task 1', 'completed': False}, 
                  {'title': 'Task 2', 'completed': True}]
    >>> save_tasks(tasks)
    This will save the tasks to 'tasks.json' in JSON format.
    """
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f)


def load_tasks():
    """def load_tasks():
    ""\"
    Load and return the list of tasks from a JSON file.

    This function attempts to open the file named 'tasks.json' in read 
    mode and read its contents as JSON. If the file does not exist or 
    is empty (leading to a JSONDecodeError), it returns an empty list. 
    This function is useful for retrieving previously saved tasks.

    Parameters:
    None

    Returns:
    list: A list of tasks loaded from the 'tasks.json' file. If the 
          file does not exist or cannot be read, an empty list is returned.

    Example:
    >>> tasks = load_tasks()
    If 'tasks.json' contains valid task data, it will return that data 
    as a list. If the file does not exist, it will return an empty list.
    """
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
