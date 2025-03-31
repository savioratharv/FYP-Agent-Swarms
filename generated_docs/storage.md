# Documentation for storage.py

## Overview
The `storage.py` module provides functionality for saving and loading tasks in a JSON format. It is a part of a larger software project that manages task-related data, allowing for persistent storage across application sessions.

### Constants
- **FILE_NAME**: A string representing the name of the JSON file where tasks are stored. The default is `"tasks.json"`.

## Functions

### `save_tasks(tasks)`
Saves tasks to a JSON file.

#### Parameters
- **tasks** (list): A list of task objects to be saved to the JSON file. Each task should be serializable to JSON.

#### Description
This function takes a list of tasks as input and writes it to a file specified by `FILE_NAME`. The data is stored in JSON format, ensuring that it can be easily retrieved and understood by other components of the software system.

#### Usage
```python
save_tasks(my_task_list)
```

### `load_tasks()`
Loads tasks from a JSON file.

#### Returns
- **list**: A list of tasks loaded from the JSON file. If the file does not exist or if it contains invalid JSON data, an empty list is returned.

#### Description
This function attempts to read tasks from the JSON file specified by `FILE_NAME`. It handles exceptions that may arise from a missing file or a JSON decoding error, thereby ensuring that the software can continue to operate smoothly in these scenarios by returning an empty list when an error occurs.

#### Usage
```python
tasks = load_tasks()
```