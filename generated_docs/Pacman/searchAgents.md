# Pacman Search Agents Documentation

## Project Information
- **Project Name:** Pacman AI
- **Module Purpose:** This module implements various agents for controlling Pacman within a grid-based environment. It allows the utilization of search algorithms to navigate and solve pathfinding problems, including reaching goals, visiting specific locations, and collecting food. The agents leverage different search strategies, such as depth-first search and A* search, to find optimal paths based on the specified problem types.
- **Authors:** 
  - John DeNero - Developer
  - Dan Klein - Developer
  - Brad Miller - Tester
  - Nick Hay - Tester
  - Pieter Abbeel - Tester
- **Creation Date:** 2023-01-15
- **Modification Date:** 2023-10-10
- **Version:** 1.0.0
- **Dependencies:**
  - Python 3.7+
  - game.py (custom module)
  
## Public Interface Exports
- Classes:
  - `GoWestAgent`
  - `SearchAgent`
  - `PositionSearchProblem`
  - `StayEastSearchAgent`
  - `StayWestSearchAgent`
  - `CornersProblem`
  - `AStarCornersAgent`
  - `FoodSearchProblem`
  - `AStarFoodSearchAgent`
  - `ClosestDotSearchAgent`
  - `AnyFoodSearchProblem`
- Functions:
  - `manhattanHeuristic`
  - `euclideanHeuristic`
  - `cornersHeuristic`
  - `foodHeuristic`
  - `mazeDistance`

## Internal Implementation Details
- The `SearchAgent` class operates as a base agent for various search problem instances using specified search functions and heuristics.
- The `PositionSearchProblem` serves as a template for problems involving navigation to a specific point on the grid.
- `CornersProblem` is specifically designed for finding paths through all four corners of the grid.
- `FoodSearchProblem` models the challenge of navigating to collect all food items within the environment.
- Heuristic functions, such as `manhattanHeuristic` and `euclideanHeuristic`, aid in guiding search algorithms efficiently.

## Constant Definitions
- `Directions`: Enum-like structure defining valid movement directions for the agent (NORTH, SOUTH, EAST, WEST).
  
## Class/Function Relationships
- `SearchAgent` -> Utilizes functions from `search.py` to find a path to goals based on the type of problem defined.
- `CornersProblem` -> Extends `SearchProblem`, uniquely defining a state space for reaching corners in the grid.
- `AStarFoodSearchAgent` -> Inherits from `SearchAgent` and uses A* search with a custom heuristic for navigating to food.

## Revision History
| Date Modified | Version Delta | Change Description                                    | Author Initials |
|---------------|---------------|------------------------------------------------------|------------------|
| 2023-01-15    | 1.0.0         | Initial version implementation                        | JD                |
| 2023-10-10    | 1.0.1         | Added heuristic functions and refined search agents   | JD                |

## Docstrings for Key Functions

### GoWestAgent.getAction
**Functionality Overview:** Returns the action to move West if possible, otherwise stops.

**Parameters:** 
- `state` (GameState): The current state of the game.

**Returns:**
- `str`: Direction to move (WEST or STOP).

**Usage Example:**
```python
agent = GoWestAgent()
action = agent.getAction(currentGameState)
```

### SearchAgent.registerInitialState
**Functionality Overview:** Initializes the agent with the path to the goal using a specified search function.

**Parameters:**
- `state` (GameState): The initial state of the game.

**Returns:** None.

### CornersProblem.isGoalState
**Functionality Overview:** Checks if all corners have been visited.

**Parameters:**
- `state` (tuple): Contains current position and corners' visited status.

**Returns:** 
- `bool`: True if all corners are visited, otherwise False.

### foodHeuristic
**Functionality Overview:** Computes a heuristic for the FoodSearchProblem, estimating the shortest distance to uncollected food.

**Parameters:**
- `state` (tuple): Contains Pacman's position and the food grid.
- `problem` (FoodSearchProblem): The problem instance.

**Returns:** 
- `int`: Estimated distance or cost to collect remaining food.

**Usage Example:**
```python
heuristic_value = foodHeuristic(currentState, foodProblem)
```

### mazeDistance
**Functionality Overview:** Calculates the maze (grid-based) distance between two points using BFS.

**Parameters:**
- `point1` (tuple): First coordinate (x1, y1).
- `point2` (tuple): Second coordinate (x2, y2).
- `gameState` (GameState): The game state context.

**Returns:** 
- `int`: The maze distance between the two points.

### Exception Hierarchy
- `AttributeError`: Raised when an unspecified search function or problem type is requested.
- `Exception`: General error raised for illegal moves or search function issues.