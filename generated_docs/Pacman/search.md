# Pacman Search Module

## Purpose
The `search.py` module provides implementations of various search algorithms that can be utilized by Pacman agents to navigate through search problems. These algorithms include depth-first search, breadth-first search, uniform cost search, and A* search, supporting pathfinding tasks in grid-based maze environments. This module serves as the core search engine, facilitating the decision-making process of agents in the Pacman game.

## Author List
- John DeNero - Primary Developer
- Dan Klein - Core Contributor
- Brad Miller - Student Side Autograding
- Nick Hay - Student Side Autograding
- Pieter Abbeel - Student Side Autograding

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modification Date: 2023-10-20

## Version
Version: 1.0.0

## Dependencies
- util: >=1.0

## Public Interface Exports
- `bfs`: Function for breadth-first search.
- `dfs`: Function for depth-first search.
- `ucs`: Function for uniform cost search.
- `astar`: Function for A* search.

## Internal Implementation Details
The module implements multiple search algorithms as functions that all accept a `SearchProblem` instance, which outlines the structure of the search problem. Each algorithm maintains its state through open and visited lists and explores successor states until a goal state is reached. 

## Constant Definitions
- `nullHeuristic`: Default heuristic function for A* search.

## Class/Function Relationships
- `SearchProblem`: Abstract class defining the interface for search problems.
- `tinyMazeSearch`: Returns a sequence of actions to solve the tiny maze.
- `depthFirstSearch`: Implements depth-first search algorithm.
- `breadthFirstSearch`: Implements breadth-first search algorithm.
- `uniformCostSearch`: Implements uniform cost search algorithm.
- `aStarSearch`: Implements A* search algorithm with an optional heuristic.

## Docstrings

### `depthFirstSearch(problem)`
Search the deepest nodes in the search tree first.

**Parameters:**
- `problem`: An instance of `SearchProblem` representing the search state.

**Returns:**
- A list of actions that lead to the goal state.

**Examples:**
```python
result = depthFirstSearch(my_search_problem)
```

### `breadthFirstSearch(problem)`
Search the shallowest nodes in the search tree first.

**Parameters:**
- `problem`: An instance of `SearchProblem` representing the search state.

**Returns:**
- A list of actions that lead to the goal state.

**Examples:**
```python
result = breadthFirstSearch(my_search_problem)
```

### `uniformCostSearch(problem)`
Search the node of least total cost first.

**Parameters:**
- `problem`: An instance of `SearchProblem` representing the search state.

**Returns:**
- A list of actions that lead to the goal state.

**Examples:**
```python
result = uniformCostSearch(my_search_problem)
```

### `nullHeuristic(state, problem=None)`
A heuristic function that estimates the cost from the current state to the nearest goal.

**Parameters:**
- `state`: The current search state.
- `problem`: An optional `SearchProblem` instance.

**Returns:**
- An integer heuristic value (0 in this trivial case).

### `aStarSearch(problem, heuristic=nullHeuristic)`
Search the node that has the lowest combined cost and heuristic first.

**Parameters:**
- `problem`: An instance of `SearchProblem` representing the search state.
- `heuristic`: Optional heuristic function (default is nullHeuristic).

**Returns:**
- A list of actions that lead to the goal state.

## Revision History Table

| Date Modified | Version Delta | Change Description                      | Author Initials |
|---------------|---------------|----------------------------------------|------------------|
| 2023-10-01    | 1.0.0         | Initial creation of the search module. | JD               |
| 2023-10-20    | 1.0.0         | Added implementation for search algorithms. | JD               |