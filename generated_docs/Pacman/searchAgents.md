# Pacman Search Agents Documentation

## Overview
This module contains implementations of various agents for the Pacman game, focusing on different search strategies to navigate through the game environment efficiently. The code includes definitions for agents that can solve pathfinding problems, locate food, or visit corners of the maze using search algorithms.

### Classes

#### GoWestAgent
- **Purpose**: An agent that continuously moves west until it can't.
- **Methods**:
  - `getAction(state)`: Returns the action to move west if possible, otherwise stops.

#### SearchAgent
- **Purpose**: A general search agent that utilizes a specified search algorithm to find a path to a defined goal.
- **Methods**:
  - `__init__(fn, prob, heuristic)`: Initializes the agent with specified function, problem type, and heuristic.
  - `registerInitialState(state)`: Computes the path to the goal state during the first encounter with the game state and stores it for future actions.
  - `getAction(state)`: Retrieves the next action from the precomputed path or stops if there are no actions left.

#### PositionSearchProblem
- **Purpose**: Models a search problem focused on reaching a specific position in the Pacman grid.
- **Methods**:
  - `__init__(gameState, costFn, goal, start, warn, visualize)`: Initializes the problem's state, walls, start, and goal.
  - `getStartState()`: Returns the starting state of the problem.
  - `isGoalState(state)`: Checks if the given state is the goal state.
  - `getSuccessors(state)`: Returns successor states, actions required, and their costs.
  - `getCostOfActions(actions)`: Computes the total cost of a sequence of actions.

#### StayEastSearchAgent
- **Purpose**: An agent that minimizes cost for being in the eastern part of the board using a specific cost function.
- **Methods**:
  - `__init__()`: Initializes the search function and cost function.

#### StayWestSearchAgent
- **Purpose**: Similar to StayEastSearchAgent but penalizes positions in the east.
- **Methods**:
  - `__init__()`: Initializes the search function and cost function.

#### CornersProblem
- **Purpose**: A search problem to find paths that visit all corners of the maze.
- **Methods**:
  - `__init__(startingGameState)`: Initializes the corners problem with starting position and corner locations.
  - `getStartState()`: Returns the starting state.
  - `isGoalState(state)`: Determines if all corners have been visited.
  - `getSuccessors(state)`: Generates successors based on legal movements.
  - `getCostOfActions(actions)`: Returns the cost of a sequence of actions.

#### AStarCornersAgent
- **Purpose**: Implements an agent for solving the corners problem using the A* search algorithm with a heuristic.
- **Methods**:
  - `__init__()`: Initializes the search function and problem type.

#### FoodSearchProblem
- **Purpose**: A search problem to collect food items in the maze.
- **Methods**:
  - `__init__(startingGameState)`: Initializes the food collection problem parameters.
  - `getStartState()`: Returns the starting state.
  - `isGoalState(state)`: Checks if all food has been collected.
  - `getSuccessors(state)`: Returns possible successor states based on actions.
  - `getCostOfActions(actions)`: Computes the cost of moving through specified actions.

#### AStarFoodSearchAgent
- **Purpose**: Uses A* search to find a path for collecting food.
- **Methods**:
  - `__init__()`: Sets the search function for food collection.

### Functions

#### foodHeuristic(state, problem)
- **Purpose**: Provides a heuristic for the FoodSearchProblem.
- **Parameters**:
  - `state`: Current state of the search.
  - `problem`: Instance of the FoodSearchProblem.
- **Returns**: A heuristic value estimating the cost to reach the goal.

#### mazeDistance(point1, point2, gameState)
- **Purpose**: Calculates the maze distance between two points in the game state.
- **Parameters**:
  - `point1`: First point coordinates.
  - `point2`: Second point coordinates.
  - `gameState`: Current game state used to determine walls.
- **Returns**: The number of moves required to reach from point1 to point2 without hitting walls.