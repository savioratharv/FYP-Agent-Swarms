# Search.py Documentation

## Project Name
Pacman AI Search

## Module Purpose
This module implements various search algorithms that are used by Pacman agents to navigate through mazes. The algorithms included are Depth First Search (DFS), Breadth First Search (BFS), Uniform Cost Search (UCS), and A* Search, each of which provides a distinct strategy for exploring possible paths and determining the optimal route to a goal state.

## Author List
- John DeNero: Core Developer
- Dan Klein: Core Developer
- Brad Miller: Student Autograder Contributor
- Nick Hay: Student Autograder Contributor
- Pieter Abbeel: Student Autograder Contributor

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modification Date: 2023-10-15

## Version
1.0.0

## Dependency List
- Python 3.7+
- util (>=1.0.0)
- game (>=1.0.0)

---

## Public Interface Exports
- `tinyMazeSearch(problem)`
- `depthFirstSearch(problem)`
- `breadthFirstSearch(problem)`
- `uniformCostSearch(problem)`
- `aStarSearch(problem, heuristic=nullHeuristic)`

---

## Internal Implementation Details
- The search algorithms utilize various data structures such as stacks, queues, and priority queues to manage the exploration of potential paths.
- Each algorithm maintains a list of visited nodes to avoid cycles and redundant explorations.
- Successor nodes are generated from the current node based on available actions and costs.

---

## Constant Definitions
- No constant values are defined in this module.

---

## Class/Function Relationships
- `SearchProblem`: An abstract class that outlines the structure of a search problem.
- `tinyMazeSearch`: A function that returns moves to solve the tinyMaze specifically.
- `depthFirstSearch`, `breadthFirstSearch`, `uniformCostSearch`, `aStarSearch`: Functions that implement various search strategies as defined in search algorithms.

---

## Function Documentation

### tinyMazeSearch
```python
def tinyMazeSearch(problem):
```
- **Functionality Overview:** Returns a sequence of moves that solves the tinyMaze. 
- **Parameters:**
    - `problem`: A `SearchProblem` instance.
- **Returns:** A list of actions to reach the goal in the tinyMaze.
- **Usage Example:**
    ```python
    >>> tinyMazeSearch(some_problem)
    ['S', 'S', 'W', 'S', 'W', 'W', 'S', 'W']
    ```
- **Exception Hierarchy:** N/A

---

### depthFirstSearch
```python
def depthFirstSearch(problem):
```
- **Functionality Overview:** Uses the depth-first search algorithm to find a path to the goal state.
- **Parameters:**
    - `problem`: A `SearchProblem` instance.
- **Returns:** A list of actions leading to the goal state, or an empty list if no path is found.
- **Usage Example:**
    ```python
    >>> depthFirstSearch(some_problem)
    ['South', 'South', 'West', 'South']
    ```
- **Exception Hierarchy:** If the problem is not defined properly, a `NotImplementedError` may occur.

---

### breadthFirstSearch
```python
def breadthFirstSearch(problem):
```
- **Functionality Overview:** Employs the breadth-first search strategy to explore the shallowest nodes first.
- **Parameters:**
    - `problem`: A `SearchProblem` instance.
- **Returns:** A list of actions to reach the goal state.
- **Usage Example:**
    ```python
    >>> breadthFirstSearch(some_problem)
    ['North', 'North', 'East']
    ```
- **Exception Hierarchy:** If the problem is not defined, a `NotImplementedError` may occur.

---

### uniformCostSearch
```python
def uniformCostSearch(problem):
```
- **Functionality Overview:** Searches the node of least total cost first.
- **Parameters:**
    - `problem`: A `SearchProblem` instance.
- **Returns:** A list of actions that leads to the optimal goal state based on costs.
- **Usage Example:**
    ```python
    >>> uniformCostSearch(some_problem)
    ['East', 'East', 'South']
    ```
- **Exception Hierarchy:** If the problem is not set appropriately, a `NotImplementedError` may arise.

---

### aStarSearch
```python
def aStarSearch(problem, heuristic=nullHeuristic):
```
- **Functionality Overview:** Combines the cost and heuristic to find the optimal path to the goal.
- **Parameters:**
    - `problem`: A `SearchProblem` instance.
    - `heuristic`: A function that estimates the distance to the nearest goal.
- **Returns:** A list of actions leading to the goal state based on the combined cost and heuristic.
- **Usage Example:**
    ```python
    >>> aStarSearch(some_problem, heuristic)
    ['West', 'West', 'North']
    ```
- **Exception Hierarchy:** A poorly defined problem can lead to a `NotImplementedError`.

---

## Revision History

| Date Modified   | Version Delta | Change Description                                | Author Initials |
|------------------|---------------|---------------------------------------------------|------------------|
| 2023-10-01       | 1.0.0         | Initial creation of search algorithms module.     | JD, DK           |
| 2023-10-15       | 1.0.1         | Updated documentation and fixed minor bugs.       | JD               |