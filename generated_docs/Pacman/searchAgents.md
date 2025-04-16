# Pacman Search Agents

## Module Purpose
This module contains various agents that can control the behavior of Pacman in a grid-based game environment. These agents utilize different search algorithms to navigate the maze and achieve specific goals, including reaching a designated point, visiting corners, and collecting food. The search strategies implemented include depth-first search, breadth-first search, and A* search. The agents can be customized through parameters passed during initialization.

## Author List
- John DeNero: Lead Developer, Algorithm Design
- Dan Klein: Co-Developer, API Design
- Brad Miller: Testing and Documentation
- Pieter Abbeel: Systems Architect

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modification Date: 2023-10-15

## Version
- Version: 1.0.0

## Dependencies
- Python 3.7+
- `game` module (minimum version unspecified)
- `search` module (minimum version unspecified)
- `util` module (minimum version unspecified)

## Public Interface Exports
- `GoWestAgent`: Agent that moves west until it can't.
- `SearchAgent`: General search agent allowing customizable search strategies.
- `CornersProblem`: Defines a search problem for visiting all four corners.
- `AStarCornersAgent`: Agent that solves the CornersProblem using A* search.
- `FoodSearchProblem`: Defines a search problem for collecting all food.
- `AStarFoodSearchAgent`: Agent that solves the FoodSearchProblem using A* search.

## Internal Implementation Details
- Agents implement various search strategies and problem definitions.
- The `SearchAgent` orchestrates the search by using specified search functions and problems.
- Each search problem maintains its own state, goal states, and adjacency through successor functions.

## Constant Definitions
- `Directions`: Constants representing possible movement directions.
- `Directions.NORTH`, `Directions.SOUTH`, `Directions.EAST`, `Directions.WEST`: Directional constants.

## Class/Function Relationships
- `SearchAgent` serves as a base class for agents that require a search algorithm.
- `PositionSearchProblem` is a base class for position-related searching tasks.
- `CornersProblem` and `FoodSearchProblem` inherit from `PositionSearchProblem`, defining distinct goals.

## Docstring Overview

### GoWestAgent

```python
class GoWestAgent(Agent):
    """
    An agent that goes West until it can't.

    Parameters:
    state (GameState): The current game state.

    Returns:
    Directions: Direction to move (West or Stop).
    """
```

### SearchAgent

```python
class SearchAgent(Agent):
    """
    General search agent that finds a path using a search algorithm.

    Parameters:
    fn (str): Name of the search function to use.
    prob (str): Type of search problem.
    heuristic (str): Heuristic function to use.

    Returns:
    None

    Usage Example:
    agent = SearchAgent(fn='depthFirstSearch', prob='PositionSearchProblem', heuristic='nullHeuristic')
    """

    def registerInitialState(self, state):
        """
        Receives the initial game state and computes the path to the goal.

        Parameters:
        state (GameState): Initial game state for pathfinding.
        
        Returns:
        None
        """
```

### CornersProblem

```python
class CornersProblem(search.SearchProblem):
    """
    A problem defined for visiting all four corners.

    Parameters:
    startingGameState (GameState): Initial game state to initialize problem.

    Returns:
    None
    """
    
    def isGoalState(self, state):
        """ 
        Determines if all corners have been visited.

        Parameters:
        state: Current state of the problem.
        
        Returns:
        bool: True if goal state reached, otherwise False.
        """
```

### foodHeuristic

```python
def foodHeuristic(state, problem):
    """
    Heuristic for the FoodSearchProblem.

    Parameters:
    state (tuple): Current state (Pacman position and food grid).
    problem (FoodSearchProblem): Instance of the food search problem.
    
    Returns:
    int: Heuristic value estimating cost to reach goal.
    """
```

## Revision History

| Date Modified | Version Delta | Change Description                                       | Author Initials |
|---------------|---------------|---------------------------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of module and core functionalities.    | JD, DK            |
| 2023-10-15    | 1.1.0        | Added heuristic functions and additional agents.         | BM, PA            |