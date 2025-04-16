# Pacman Game Module Documentation

## File Header

**Project Name:** Pacman AI

**Module Purpose:**  
This module provides the essential components needed to implement and manage a game of Pacman. It defines agents, their configurations, the game state, actions, and the game control flow. The structured design supports easy modification and expansion for various gameplay scenarios and strategies for both Pacman and ghost agents.

**Author List:**  
- John DeNero - Project Lead  
- Dan Klein - Project Architect  
- Brad Miller - Student Developer  
- Nick Hay - Student Developer  
- Pieter Abbeel - Student Developer  

**Creation/Modification Dates:**  
- Created: 2020-01-01  
- Modified: 2023-10-01  

**Version:**  
1.1.0  

**Dependencies:**  
- Python 3.7.0 or higher  
- `util` module (version 1.0 or higher)

## Public Interface Exports
- Classes:
  - `Agent`
  - `Directions`
  - `Configuration`
  - `AgentState`
  - `Grid`
  - `GameStateData`
  - `Game`
  
## Internal Implementation Details
The module implements various classes responsible for managing agents (Pacman and ghosts), their configurations, the grid for the game environment, and the overall game state. Each class provides methods for manipulating and accessing state information such as positions, directions, and actions. 

## Constant Definitions
- `CELLS_PER_INT`: Constant defining the number of cells represented in a single integer for efficient storage in the `Grid` class.
- Directions:
  - `Directions.NORTH`
  - `Directions.SOUTH`
  - `Directions.EAST`
  - `Directions.WEST`
  - `Directions.STOP`

## Class/Function Relationships
- `Agent`: Base class for all agents in the game.
- `Grid`: Represents the 2D game area and manages food, walls, and other entities.
- `Game`: Controls the game loops, taking actions from agents and updating the game state accordingly.

## Docstrings

### Agent Class
```python
class Agent:
    """ 
    Represents an agent in the game, which can be either Pacman or a ghost.

    Attributes:
    - index: The identifier index of the agent.

    Methods:
    - getAction(state): Abstract method to determine the action given the current game state.
    """

    def __init__(self, index=0):
        """
        Initializes an agent with a specific index.

        Parameters:
        - index: int, optional, default is 0. The index of the agent.

        Returns:
        None
        """
```

### Configuration Class
```python
class Configuration:
    """
    Holds the (x,y) coordinate of a character along with its traveling direction.

    Attributes:
    - pos: Tuple[int, int] representing x and y coordinates.
    - direction: The current direction of movement.

    Methods:
    - getPosition(): Returns the current position.
    - getDirection(): Returns the current direction.
    - generateSuccessor(vector): Generates a new configuration based on the action vector.
    """

    def __init__(self, pos, direction):
        """
        Initializes the configuration with specific position and direction.

        Parameters:
        - pos: Tuple[int, int]. The initial coordinates of the agent.
        - direction: str. The initial direction of the agent.

        Returns:
        None
        """
```

## Exception Hierarchy Documentation
- `Exception`: Base class for all exceptions.
  - `TimeoutFunctionException`: Raised when a function exceeds its allowed execution time.

## Revision History
| Date Modified | Version Delta | Change Description                      | Author Initials |
|---------------|---------------|----------------------------------------|------------------|
| 2023-10-01    | 1.1.0        | Updated methods for agent handling and improved error management. | JD              |
| 2023-01-15    | 1.0.0        | Initial creation of the game module.  | JD, DK           |