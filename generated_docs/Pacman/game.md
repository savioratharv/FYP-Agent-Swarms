# Game

## Module Purpose
The `game.py` module defines the core classes and logic required to manage the Pacman game, including the implementation of agents, configurations, states, and the game loop. It is responsible for controlling the interaction between agents, displaying the game state, and handling the rules under which the game operates. This module lays the foundation for creating and extending game agents in a dynamic environment.

## Author List
- John DeNero: Lead developer
- Dan Klein: Co-developer
- Brad Miller: Student side development
- Nick Hay: Student side development
- Pieter Abbeel: Student side development

## Creation/Modification Dates
- Creation Date: 2009-03-01
- Modification Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- Python >= 3.6
- Util module

## Public Interface Exports
- `Agent`: Base class for all agents implementing the `getAction` method.
- `Directions`: Class defining movement directions and their relationships.
- `Configuration`: Class representing the position and direction of an agent.
- `AgentState`: Class containing the state of an agent, including configuration.
- `Grid`: Class representing a 2D grid used for the game environment.
- `Game`: Class managing the game flow, agent actions, and state transitions.

## Internal Implementation Details
The internal workings of the `game.py` module are encapsulated within several classes that manage different aspects of the game:

1. **Agent**: This class serves as the base for any agent that interacts with the game, requiring implementation of the `getAction` method.
2. **Directions**: A utility class that contains constants representing directional movement and their relationships (left, right, reverse).
3. **Configuration**: Represents an agent's position and direction in the game grid and provides methods for manipulating this state.
4. **AgentState**: Holds the current and starting configuration for agents, along with their state attributes such as whether they are Pacman or ghosts.
5. **Grid**: Represents the game map as a 2D boolean array, with utility functions for manipulation and representation.
6. **Game**: Manages the game's main control loop, handling agent turns, scoring, and game over conditions.

## Constant Definitions

### Direction Constants
- `NORTH`: 'North'
- `SOUTH`: 'South'
- `EAST`: 'East'
- `WEST`: 'West'
- `STOP`: 'Stop'

### Direction Relationships
- `LEFT`: Direction relationships indicating left turns.
- `RIGHT`: Direction relationships indicating right turns.
- `REVERSE`: Direction relationships indicating reverse turns.

## Class/Function Relationships
- The `Game` class interacts with `Agent` instances to solicit actions during each turn, maintaining the overall game state via `GameStateData`.
- `Actions` provides utility methods for direction manipulation and movement checks, aiding in the interaction between `Configuration`, `Grid`, and agents.
- `Grid` is used to establish the map layout and food status, which impacts the actions available to agents.

## Docstrings
The methods and classes within this module are thoroughly documented following PEP 257, providing functionality overviews, parameter/return value tables, usage examples, and documented exceptions.

### Agent Class
```python
class Agent:
    """
    An agent must define a getAction method, but may also define the
    following methods which will be called if they exist:
    
    def registerInitialState(self, state):  # inspects the starting state
    """
```

### Directions Class
```python
class Directions:
    """
    Defines movement directions and their relationships for the Agents.
    """
```

### Configuration Class
```python
class Configuration:
    """
    Holds the (x,y) coordinate of a character, along with its traveling direction.

    The convention for positions, like a graph, is that (0,0) is the lower left corner, x increases
    horizontally and y increases vertically.
    """
```

### AgentState Class
```python
class AgentState:
    """
    Contains the state of an agent including its configuration and attributes.
    """
```

### Grid Class
```python
class Grid:
    """
    A 2D array representing the game map, with boolean values indicating walls or food.
    """
```

### Game Class
```python
class Game:
    """
    The Game class manages game control flow, processing agent actions and updating state.
    """
```

## Revision History
| Date Modified | Version Delta | Change Description                        | Author Initials |
|---------------|---------------|------------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial release of game module           | JD, DK           |
|               |               | Added core game management functionality |                  |