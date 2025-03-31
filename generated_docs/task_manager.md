# Task Manager Documentation

## Overview
The `TaskManager` class is responsible for managing tasks within a TODO application. It interacts with task data by adding, removing, and listing tasks, while utilizing external functions for loading and saving tasks.

### Class: `TaskManager`
#### Description
The `TaskManager` class encapsulates the functionality for task management in a TODO app, allowing users to add, remove, and display tasks. It initializes itself with stored tasks upon instantiation.

#### Methods

##### `__init__(self)`
- **Purpose**: Initializes the `TaskManager` instance and loads previously saved tasks.
- **Functionality**:
  - Calls the `load_tasks()` function to fetch existing tasks for the session.
  
##### `add_task(self, task)`
- **Purpose**: Adds a new task to the tasks list.
- **Parameters**:
  - `task` (str): The task to be added to the list.
- **Functionality**:
  - Appends the new task to the internal list of tasks.
  - Calls `save_tasks(self.tasks)` to update the stored tasks.
  - Prints a confirmation message indicating that the task has been added.

##### `remove_task(self, task)`
- **Purpose**: Removes an existing task from the tasks list.
- **Parameters**:
  - `task` (str): The task to be removed.
- **Functionality**:
  - Checks if the task exists in the internal list.
    - If found, removes the task and calls `save_tasks(self.tasks)` to update the storage.
    - Prints a confirmation message; if not found, prints a "Task not found" message.

##### `list_tasks(self)`
- **Purpose**: Displays all current tasks.
- **Functionality**:
  - Checks if there are any tasks available.
    - If tasks exist, calls `display_tasks(self.tasks)` to show them.
    - If no tasks are available, prints a message indicating that there are no tasks.

### External Dependencies
- **Helper Functions**:
  - `load_tasks()`: Loads tasks from a JSON file into a list. (See detailed documentation)
  - `save_tasks(tasks)`: Saves the current list of tasks to a JSON file. (See detailed documentation)
  - `display_tasks(tasks)`: Displays the list of tasks in a formatted manner. (See detailed documentation)