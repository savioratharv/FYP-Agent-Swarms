# Search Test Classes

## Module Purpose
This module contains classes and functions for testing various search algorithms and heuristics implemented for the Pacman AI project. It provides the infrastructure to define search problems, validate solutions, and compare student submissions against correct implementations.

## Authors
- John DeNero (Primary Developer)
- Dan Klein (Core Contributor)
- Brad Miller (Student Autograding)
- Nick Hay (Student Autograding)
- Pieter Abbeel (Student Autograding)

## Creation/Modification Dates
- Creation Date: 2023-03-01
- Last Modification Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependencies
- Python 3.7+
- layout (>=1.0)
- pacman (>=1.0)
- search (>=1.0)

## Public Interface Exports
- `GraphSearch`
- `GraphSearchTest`
- `PacmanSearchTest`
- `CornerProblemTest`
- `HeuristicTest`
- `HeuristicGrade`
- `ClosestDotTest`
- `CornerHeuristicSanity`
- `CornerHeuristicPacman`

## Internal Implementation Details
The module defines multiple test classes to validate search algorithms in different scenarios. Each test class is designed to handle specific types of search problems and provides methods for validating solutions by comparing student-generated outputs against reference solutions.

## Constant Definitions
None defined at the module level, but constants may be used within individual classes.

## Class/Function Relationships
- `GraphSearchTest` inherits from `testClasses.TestCase` and tests graph search problems using the `GraphSearch` implementation.
- `PacmanSearchTest` inherits from `testClasses.TestCase` to verify search algorithms in the context of Pacman games.
- `CornerProblemTest`, `HeuristicTest`, `HeuristicGrade`, `ClosestDotTest`, `CornerHeuristicSanity`, and `CornerHeuristicPacman` further extend functionality for specific test cases in the game.

## Revision History
| Date Modified | Version Delta | Change Description                              | Author Initials |
|---------------|---------------|-------------------------------------------------|------------------|
| 2023-03-01    | 1.0.0        | Initial module creation and structure setup.  | JD                |
| 2023-10-01    | 1.0.1        | Added comprehensive documentation and comments. | JD                |

## Docstrings

### wrap_solution
```python
def wrap_solution(solution):
```
**Functionality Overview:**  
Formats the solution for cleaner output by wrapping text within a width limit.

**Parameters:**
| Parameter | Type     | Description                          |
|-----------|----------|--------------------------------------|
| solution  | list or str | The solution to format.            |

**Returns:**
| Return Value | Type   | Description                              |
|--------------|--------|------------------------------------------|
| Wrapped solution | str   | A formatted string representation of the solution. |

**Usage Examples:**
```python
print(wrap_solution(['move', 'left', 'move', 'up']))
```

**Exception Hierarchy Documentation:**  
No exceptions are raised.

### followAction
```python
def followAction(state, action, problem):
```
**Functionality Overview:**  
Returns the successor state given the current state and action.

**Parameters:**
| Parameter | Type          | Description                             |
|-----------|---------------|-----------------------------------------|
| state     | any           | The current state of the search problem. |
| action    | any           | The action to execute from the current state. |
| problem   | SearchProblem | The instance of the search problem.    |

**Returns:**
| Return Value | Type     | Description                                      |
|--------------|----------|--------------------------------------------------|
| successor    | any      | The resulting state after the action is executed. |

**Usage Examples:**
```python
next_state = followAction(state, 'move_right', problem)
```

**Exception Hierarchy Documentation:**  
Returns `None` if the action is invalid in the given state.

### followPath
```python
def followPath(path, problem):
```
**Functionality Overview:**  
Follows a series of actions from the starting state and returns the list of visited states.

**Parameters:**
| Parameter | Type          | Description                             |
|-----------|---------------|-----------------------------------------|
| path      | list         | A sequence of actions to follow.        |
| problem   | SearchProblem | The instance of the search problem.     |

**Returns:**
| Return Value | Type   | Description                                     |
|--------------|--------|-------------------------------------------------|
| states       | list   | A list of states visited along the path.      |

**Usage Examples:**
```python
states_visited = followPath(['move', 'left', 'move', 'up'], problem)
```

**Exception Hierarchy Documentation:**  
No exceptions are raised.

### checkSolution
```python
def checkSolution(problem, path):
```
**Functionality Overview:**  
Validates whether the provided path leads to a goal state in the specified problem.

**Parameters:**
| Parameter | Type          | Description                             |
|-----------|---------------|-----------------------------------------|
| problem   | SearchProblem | The instance of the search problem.     |
| path      | list         | A sequence of actions proposed as a solution. |

**Returns:**
| Return Value | Type   | Description                                  |
|--------------|--------|----------------------------------------------|
| valid        | bool   | True if the path reaches a goal state; otherwise False. |

**Usage Examples:**
```python
is_valid = checkSolution(problem, ['move', 'left'])
```

**Exception Hierarchy Documentation:**  
No exceptions are raised.

### GraphSearch
```python
class GraphSearch(SearchProblem):
```
**Functionality Overview:**  
Represents a search problem defined over a graph structure with start and goal states.

**Methods Summary:**
- `getStartState`: Returns the starting state of the graph.
- `isGoalState`: Checks if a given state is a goal state.
- `getSuccessors`: Retrieves the successors of a given state.
- `getCostOfActions`: Evaluates the total cost of a given sequence of actions.
- `getExpandedStates`: Returns the list of states that have been expanded.

**Usage Examples:**
```python
graph = GraphSearch(graph_data)
if graph.isGoalState(current_state):
    print("Reached goal!")
```

**Exception Hierarchy Documentation:**  
Raises exceptions for invalid graph specifications during initialization.