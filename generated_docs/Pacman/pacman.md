# Pacman

## Module Purpose
The Pacman module contains the implementation of the classic Pacman game, including strategies for player and ghost interactions. It allows for game control, state management, and interaction between the Pacman and ghost entities, enabling a functional gaming experience. This module serves as the main interface for running the game and managing gameplay rules.

## Author List
- John DeNero: Lead Developer
- Dan Klein: Co-Developer
- Brad Miller: Student-side Autograder
- Nick Hay: Student-side Autograder
- Pieter Abbeel: Student-side Autograder

## Creation/Modification Dates
- Creation Date: 2020-10-01
- Last Modified Date: 2023-10-01

## Version
Version: 1.0.0

## Dependency List
- Python (>= 3.6)
- game (>= 1.0.0)
- util (>= 1.0.0)
- layout (>= 1.0.0)

## Public Interface Exports
- Class: `GameState`
- Class: `ClassicGameRules`
- Class: `PacmanRules`
- Class: `GhostRules`
- Function: `runGames()`
- Function: `replayGame()`
- Function: `readCommand()`
- Function: `loadAgent()`

## Internal Implementation Details
The internal implementation involves several classes and methods that govern the game mechanics, state transitions, and rules based on several interactions between Pacman and the ghosts. The game state interacts with the GameStateData object to track food, scores, agents, and the game layout.

## Constant Definitions
- `SCARED_TIME`: Duration for which ghosts remain scared after consuming a capsule.
- `COLLISION_TOLERANCE`: Maximum distance for a ghost to collide with Pacman.
- `TIME_PENALTY`: Point penalty incurred for idle moves.

## Class/Function Relationships
- The `GameState` class manages the overall state of the game, including food, capsules, and agent configurations.
- The `ClassicGameRules` class encapsulates the game flow logic, determining the start and end conditions.
- The `PacmanRules` class defines the interaction mechanism for Pacman, including movement and food consumption.
- The `GhostRules` class outlines ghost behavior, including legal moves and interactions with Pacman.

## Revision History

| Date Modified | Version Delta | Change Description                | Author Initials |
|---------------|---------------|-----------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial release of the file.     | JD, DK           | 

## Documentation for Classes and Functions

### Class `GameState`
The `GameState` class specifies the full game state, including agents, food, and scores. It provides methods for accessing state data and generating successor states.

#### Methods Overview
- `__init__(self, prevState=None)`: Initializes a game state from a previous state or creates a new one.
- `generateSuccessor(self, agentIndex, action)`: Generates a new state by applying the specified action of the specified agent.
  
#### Parameter/Return Value Table
| Parameter     | Type       | Description                                |
|---------------|------------|--------------------------------------------|
| prevState     | `GameState`| Previous game state for initialization.    |
| agentIndex    | `int`     | Index of the agent whose action to apply.  |
| action        | `str`     | The action to apply for generating a state. |

### Class `ClassicGameRules`
The `ClassicGameRules` class encapsulates the game rules and process flow including win/lose conditions.

#### Methods Overview
- `newGame(self, layout, pacmanAgent, ghostAgents, display, quiet=False, catchExceptions=False)`: Initializes a new game state based on the provided parameters.

#### Parameter/Return Value Table
| Parameter            | Type       | Description                                |
|----------------------|------------|--------------------------------------------|
| layout               | `Layout`   | The game layout to be used.                |
| pacmanAgent          | `Agent`    | The agent object managing Pacman.          |
| ghostAgents          | `List[Agent]` | List of ghost agent objects.            |
| display              | `Display`  | The display object for the game.           |
| quiet                | `bool`     | If true, skips outputs and displays.       |
| catchExceptions      | `bool`     | If true, enables exception handling.       |

### Class `PacmanRules`
The `PacmanRules` class manages the actions and interactions specific to the Pacman character.

#### Methods Overview
- `getLegalActions(state)`: Returns a list of legal actions for Pacman.
- `applyAction(state, action)`: Updates the state based on the action taken by Pacman.

### Class `GhostRules`
The `GhostRules` class outlines the behavior and rules governing ghost actions.

#### Methods Overview
- `getLegalActions(state, ghostIndex)`: Returns legal actions for a specified ghost.
- `applyAction(state, action, ghostIndex)`: Applies the specified action for the ghost, updating the state accordingly.

### Utility Functions
#### Function `manhattanDistance`
Calculates the Manhattan distance between two points in a 2D grid.

- **Parameter**: 
  - xy1: Tuple of coordinates (x1, y1).
  - xy2: Tuple of coordinates (x2, y2).
  
- **Returns**: 
  - int: The Manhattan distance between the two points.

#### Function `nearestPoint`
Finds the nearest grid point to a given position by rounding the coordinates.

- **Parameter**: 
  - pos: Tuple of continuous coordinates (x, y).
  
- **Returns**: 
  - Tuple: Nearest grid coordinates (rounded_x, rounded_y).