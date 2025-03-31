# utils.py Documentation

## Overview
This file contains utility functions that support task management within the application. As part of a larger software project, these utilities facilitate user interactions with task lists, allowing for efficient display and organization of tasks.

## Functions

### `display_tasks(tasks)`

#### Purpose
Displays a list of tasks in a user-friendly format.

#### Parameters
- `tasks` (list): A list of tasks to be displayed. Each task is expected to be a string.

#### Functionality
- Prints a header "Your Tasks:" to indicate the start of the task list.
- Iterates over the provided tasks.
- For each task, it prints the task index (starting from 1) followed by the task itself.

#### Example
If `tasks` is `["Task 1", "Task 2", "Task 3"]`, the output will be:
```
Your Tasks:
1. Task 1
2. Task 2
3. Task 3
```