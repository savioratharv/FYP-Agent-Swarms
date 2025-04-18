# /********************************************************************************
#  * Filename: storage.py
#  * 
#  * File Description:
#  * This module facilitates persistent storage of task data through JSON serialization.
#  * It provides mechanisms to save a collection of tasks to a JSON file and to retrieve
#  * tasks from that file. The module ensures robustness against common I/O and data
#  * decoding errors by implementing appropriate exception handling. Following IEEE 1016 
#  * standards and GNU coding conventions, the code emphasizes clarity, consistency, 
#  * and readability.
#  * 
#  * Functions:
#  * 
#  * 1. save_tasks(tasks)
#  *    Purpose:
#  *       Serializes a list of task objects and writes them into a JSON-formatted file named 'tasks.json'.
#  *    Parameters:
#  *       tasks (list): A collection of task objects, each of which must be compatible with JSON serialization.
#  *    Returns:
#  *       None
#  *    Behavior:
#  *       Opens the designated file in write mode, serializes the input list into JSON, and writes
#  *       the data. Overwrites existing content without explicit backup. Assumes provided data is
#  *       properly formatted and serializable.
#  *    Usage:
#  *       Invoke this function with a list of task representations to update persistent storage.
#  * 
#  * 2. load_tasks()
#  *    Purpose:
#  *       Reads and deserializes task data from the JSON file named 'tasks.json'.
#  *    Returns:
#  *       list: The list of tasks retrieved from storage. If the file is missing or contains
#  *             invalid data, an empty list is returned.
#  *    Behavior:
#  *       Attempts to open the designated file in read mode. If successful, deserializes JSON content.
#  *       If the file does not exist or contains invalid JSON, returns an empty list to prevent crashes.
#  *    Usage:
#  *       Call this function at application startup or when loading task data to restore user tasks.
#  * 
#  * Exception Handling:
#  * - load_tasks() captures and manages FileNotFoundError to handle missing storage file gracefully.
#  * - Also captures JSONDecodeError to handle invalid or malformed JSON content without crashing.
#  * 
#  * Implementation Details:
#  * - Uses a constant FILE_NAME to define the JSON data file location ('tasks.json').
#  * - Employs context managers for safe file operations, ensuring resources are properly released.
#  * - Ensures that functions do not modify external state and operate predictably.
#  * 
#  * Usage Context:
#  * This module is intended for integration within task management applications requiring
#  * data persistence. Users should ensure that task data passed to save_tasks() conforms to
#  * JSON serializable structures, such as dictionaries or lists of primitives.
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
