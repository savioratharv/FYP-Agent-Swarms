# Game.py Documentation

## Classes

### Agent
The base class for agents within the game. An agent must implement the `getAction` method to define its behavior in response to the current game state.

- **Methods**:
  - `__init__(index=0)`: Initializes an agent with a specified index.
  - `getAction(state)`: Must be implemented by subclasses to return an action based on the given game state.

---

### Directions
A utility class that defines movement directions and their corresponding relationships (left, right, reverse).

- **Constants**:
  - `NORTH`, `SOUTH`, `EAST`, `WEST`, `STOP`: Strings representing directions.
  
- **Dictionaries**:
  - `LEFT`: Maps each direction to its left direction.
  - `RIGHT`: Maps each direction to its right direction.
  - `REVERSE`: Maps each direction to its opposite direction.

---

### Configuration
Represents an agent's position and direction on the game board. 

- **Methods**:
  - `__init__(pos, direction)`: Initializes a configuration with a position and direction.
  - `getPosition()`: Returns the current (x, y) coordinates.
  - `getDirection()`: Returns the current direction.
  - `isInteger()`: Checks if the coordinates are both integers.
  - `__eq__(other)`: Compares two configurations.
  - `__hash__()`: Generates a hash for the configuration.
  - `__str__()`: Returns a string representation of the configuration.
  - `generateSuccessor(vector)`: Creates a new configuration by moving in the specified vector direction.

---

### AgentState
Holds the state information for an agent, including its configuration and status (such as if it's Pacman).

- **Methods**:
  - `__init__(startConfiguration, isPacman)`: Initializes the agent's state.
  - `__str__()`: Provides a string representation of the agent state.
  - `__eq__(other)`: Compares two agent states.
  - `__hash__()`: Generates a hash for the agent state.
  - `copy()`: Creates a duplicate of the agent state.
  - `getPosition()`: Returns the agent's current position.
  - `getDirection()`: Returns the agent's current direction.

---

### Grid
A two-dimensional array representing the game board. It manages the state of various cells (empty, food, walls).

- **Methods**:
  - `__init__(width, height, initialValue=False, bitRepresentation=None)`: Initializes the grid.
  - `__getitem__(i)`: Retrieves the data for the specified position.
  - `__setitem__(key, item)`: Sets the data for the specified position.
  - `__str__()`: Constructs a visual representation of the grid.
  - `__eq__(other)`: Compares two grid states.
  - `__hash__()`: Generates a hash for the grid.
  - `copy()`: Returns a shallow copy of the grid.
  - `deepCopy()`: Returns a deep copy of the grid.
  - `shallowCopy()`: Returns a shallow copy of the grid.
  - `count(item=True)`: Counts the number of cells with a specified value.
  - `asList(key=True)`: Returns a list of positions that match a specified value.
  - `packBits()`: Generates an efficient representation of the grid using bit-packing.
  - `_cellIndexToPosition(index)`: Converts a linear index to (x, y) coordinates.
  - `_unpackBits(bits)`: Fills the grid with data from a bit-level representation.
  - `_unpackInt(packed, size)`: Unpacks bits to boolean values.

---

### Actions
A utility class that provides methods for action manipulation in the game.

- **Methods**:
  - `reverseDirection(action)`: Returns the opposite direction of the given action.
  - `vectorToDirection(vector)`: Converts a movement vector to a direction.
  - `directionToVector(direction, speed=1.0)`: Converts a direction to a movement vector.
  - `getPossibleActions(config, walls)`: Returns a list of legal actions available to an agent at a given configuration.
  - `getLegalNeighbors(position, walls)`: Returns valid neighboring positions based on walls.
  - `getSuccessor(position, action)`: Computes the next position based on the current position and action taken.

---

### GameStateData
Holds the current state of the game, including the positions of agents, food, the score, and other gameplay data.

- **Methods**:
  - `__init__(prevState=None)`: Initializes GameStateData by copying from a predecessor state if provided.
  - `deepCopy()`: Creates a deep copy of the current state.
  - `copyAgentStates(agentStates)`: Copies the agent states for the current game state.
  - `__eq__(other)`: Compares two game states.
  - `__hash__()`: Generates a hash for the game state.
  - `__str__()`: Returns a string representation of the game state.
  - `initialize(layout, numGhostAgents)`: Initializes the game state from a given layout and the number of ghost agents.

---

### Game
The main control class that orchestrates the flow of the game, invoking agent actions and managing game states.

- **Methods**:
  - `__init__(agents, display, rules, startingIndex=0, muteAgents=False, catchExceptions=False)`: Initializes the game with specified parameters.
  - `getProgress()`: Returns the progress of the game, indicating completion.
  - `_agentCrash(agentIndex, quiet=False)`: Handles the situation when an agent encounters a crash.
  - `run()`: The main loop for game execution, handling agent actions, state updates, and game display.

--- 

## Dependencies
The `Counter` class, defined elsewhere, aids in counting occurrences and is utilized for tracking event frequencies within the agents in the game environment.