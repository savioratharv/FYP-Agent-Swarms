# Project Name: Pacman AI Layout Module

## Module Purpose
This module defines the `Layout` class, which manages the static information about the Pacman game board, including the arrangement of walls, food, capsules, and agents (Pacman and ghosts). It provides functionality for detecting wall positions, generating random positions, calculating visibility from agents to ghosts, and managing the layout based on a specified text format. This serves as a critical component for facilitating the game's mechanics and environment.

## Author List
- John DeNero (Lead Developer)
- Dan Klein (Co-developer)
- Brad Miller (Student-side Autograder Developer)
- Nick Hay (Student-side Autograder Developer)
- Pieter Abbeel (Student-side Autograder Developer)

## Creation/Modification Dates
- Creation Date: 2023-01-01
- Modification Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- util (minimum version 1.0.0)
- game (minimum version 1.0.0)

## Public Interface Exports
- `getLayout(name, back=2)`: Loads a layout from the given name or file.
- `tryToLoad(fullname)`: Attempts to load a layout from a specified full path.

## Internal Implementation Details
- The `Layout` class initializes a grid layout from a given text representation and maintains the state of walls, food items, capsules, and agent positions.
- Visibility matrices are managed with caching for optimized access.
- The class supports random position retrieval for legal and corner positions on the grid.

## Constant Definitions
- `VISIBILITY_MATRIX_CACHE`: A global cache to store visibility matrices to improve performance.

## Class/Function Relationships
- `Layout`: The primary class that encapsulates the entire game board's structure and behavior.
- `getLayout`: A function to retrieve layouts by name.
- `tryToLoad`: A helper function to load the layout from the filesystem.

## Revision History

| Date Modified | Version Delta | Change Description                                 | Author Initials |
|---------------|---------------|---------------------------------------------------|-----------------|
| 2023-01-01    | 0.1.0        | Initial creation of the Layout class.            | JD              |
| 2023-10-01    | 1.0.0        | Updated visibility matrix and optimized random position retrieval. | JD              |

## Class: `Layout`

### Overview
The `Layout` class manages the static game board configuration for the Pacman game.

### Methods

#### `__init__(self, layoutText)`
Initializes the layout object with given layout text.

**Parameters:**
- `layoutText` (list of str): A list representing the layout of the game.

**Returns:**
- None

#### `getNumGhosts(self)`
Returns the number of ghost agents in the layout.

**Returns:**
- int: The number of ghost agents.

#### `initializeVisibilityMatrix(self)`
Creates and caches a visibility matrix for the layout.

**Returns:**
- None

#### `isWall(self, pos)`
Checks if a position is a wall.

**Parameters:**
- `pos` (tuple): A tuple representing the (x, y) coordinates.

**Returns:**
- bool: True if the position is a wall, False otherwise.

#### `getRandomLegalPosition(self)`
Gets a random position on the grid that is not a wall.

**Returns:**
- tuple: A tuple representing a random legal (x, y) position.

#### `getRandomCorner(self)`
Gets a random corner position on the grid.

**Returns:**
- tuple: A tuple representing one of the corner positions.

#### `getFurthestCorner(self, pacPos)`
Finds the corner position furthest from a given Pacman position.

**Parameters:**
- `pacPos` (tuple): A tuple representing Pacman's (x, y) position.

**Returns:**
- tuple: The furthest corner from the Pacman's position.

#### `isVisibleFrom(self, ghostPos, pacPos, pacDirection)`
Checks if a ghost is visible from a specific Pacman position and direction.

**Parameters:**
- `ghostPos` (tuple): The ghost's (x, y) position.
- `pacPos` (tuple): The Pacman's (x, y) position.
- `pacDirection` (str): The direction from which visibility is checked.

**Returns:**
- bool: True if the ghost is visible, False otherwise.

#### `__str__(self)`
Returns a string representation of the layout.

**Returns:**
- str: String representation of the layout.

#### `deepCopy(self)`
Generates a deep copy of the layout instance.

**Returns:**
- Layout: A new instance of the Layout class with the same attributes.

#### `processLayoutText(self, layoutText)`
Processes the layout text to establish the walls, food, capsules, and agents.

**Parameters:**
- `layoutText` (list of str): The layout representation.

**Returns:**
- None

#### `processLayoutChar(self, x, y, layoutChar)`
Processes an individual character from the layout text.

**Parameters:**
- `x` (int): The x-coordinate of the character.
- `y` (int): The y-coordinate of the character.
- `layoutChar` (str): The character to process.

**Returns:**
- None

## Function: `getLayout(name, back=2)`

### Overview
Loads a layout based on the specified name.

**Parameters:**
- `name` (str): The name of the layout to load.
- `back` (int): The number of directory levels to search recursively.

**Returns:**
- Layout: Returns a `Layout` object if successful, None otherwise.

### Example
```python
layout = getLayout("testLayout")
if layout:
    print(layout)
```

### Exception Hierarchy
- `FileNotFoundError`: Raised if the specified layout file does not exist.