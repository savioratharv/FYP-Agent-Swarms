# /********************************************************************************
#  * Filename: storage.py
#  * 
#  * Description:
#  * This module provides functionality for saving and loading tasks to and from 
#  * a JSON file. It defines two primary functions: save_tasks and load_tasks.
#  * The tasks are stored in a file named 'tasks.json'. The module handles 
#  * exceptions that may arise during file operations, ensuring robustness.
#  * 
#  * Functions:
#  * 
#  * 1. save_tasks(tasks)
#  *    Purpose:
#  *    Saves a list of tasks to a JSON file. The tasks are expected to be in a 
#  *    format that is compatible with JSON serialization. 
#  *    
#  *    Parameters:
#  *    - tasks: A list containing task data to be saved. Each item in the list 
#  *              should be serializable to JSON format.
#  * 
#  *    Returns: 
#  *    None
#  *    
#  *    Behavior:
#  *    The function opens the designated JSON file ('tasks.json') in write mode 
#  *    and writes the serialized task data to it. If the operation is successful, 
#  *    the tasks are saved permanently until overwritten.
#  * 
#  * 
#  * 2. load_tasks()
#  *    Purpose:
#  *    Loads and returns a list of tasks from a JSON file. If the file is not 
#  *    found or if the data within the file is not valid JSON, the function 
#  *    returns an empty list.
#  * 
#  *    Parameters:
#  *    None
#  * 
#  *    Returns:
#  *    A list of tasks, which may be empty if the file does not exist or cannot 
#  *    be decoded. 
#  * 
#  *    Behavior:
#  *    The function attempts to open the designated JSON file ('tasks.json') in 
#  *    read mode. If successful, it reads the data, deserializes it from JSON 
#  *    format, and returns it as a list. If the file is not found or if a JSON 
#  *    decoding error occurs, it safely returns an empty list.
#  * 
#  *  Exception Handling:
#  *  The load_tasks function specifically handles two exceptions:
#  *  - FileNotFoundError: Triggered if the file 'tasks.json' does not exist; 
#  *    an empty list is returned.
#  *  - json.JSONDecodeError: Triggered if the content of the file is not valid 
#  *    JSON; an empty list is returned.
#  * 
#  * Usage:
#  * This module can be used as part of a larger application for managing 
#  * tasks, allowing users to persist their data across sessions. Users should 
#  * ensure that the data passed to save_tasks is properly formatted to be 
#  * compatible with JSON serialization to avoid runtime errors.
#  * 
#  * Author: [Your Name]
#  * Date: [Current Date]
#  ********************************************************************************/

import json
FILE_NAME = 'tasks.json'


def save_tasks(tasks):
    """def save_tasks(tasks):
    ""\"
    Save a list of tasks to a JSON file.

    This function takes a list of tasks and writes it to a 
    file named 'tasks.json' in JSON format. The list should 
    contain items that can be serialized to JSON.

    Parameters:
    tasks (list): A list of task data to be saved. Each 
                  item in the list must be JSON serializable.

    Returns:
    None

    Usage Example:
    >>> tasks = [{'task': 'Do laundry', 'done': False}, 
    ...          {'task': 'Go grocery shopping', 'done': False}]
    >>> save_tasks(tasks)
    This will create or overwrite the 'tasks.json' file 
    with the provided list of tasks.
    """
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f)


def load_tasks():
    """def load_tasks():
    ""\"
    Load a list of tasks from a JSON file.

    This function attempts to read the tasks from a file 
    named 'tasks.json'. If the file does not exist or cannot 
    be decoded (due to invalid JSON), it returns an empty list.

    Parameters:
    None

    Returns:
    list: A list of tasks loaded from the JSON file. If 
          the file is not found or contains invalid JSON, 
          an empty list is returned.

    Usage Example:
    >>> tasks = load_tasks()
    This will return a list of tasks stored in 'tasks.json'.
    If the file does not exist or has invalid content, 
    an empty list will be returned.
    """
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
