# Layout Module Documentation

## Overview
The `Layout` class manages the static information about the game board in the Pacman AI project. It handles the processing of the layout, including walls, food, capsules, ghosts, and Pacman's position. The class also maintains various utility functions for interacting with the game layout.

## Class: `Layout`

### `__init__(self, layoutText)`
Initializes a `Layout` object based on the provided layout text.

- **Parameters**:
  - `layoutText`: A list of strings representing the layout of the game board.

- **Key Attributes**:
  - `width`: Width of the layout.
  - `height`: Height of the layout.
  - `walls`: A 2D grid indicating the presence of walls.
  - `food`: A 2D grid indicating the presence of food.
  - `capsules`: A list of capsule positions.
  - `agentPositions`: A list of positions for both Pacman and ghosts.
  - `numGhosts`: Number of ghosts present on the board.
  - `layoutText`: The original layout text.
  - `totalFood`: Total number of food items present.

### `getNumGhosts(self)`
Returns the number of ghosts present in the layout.

- **Returns**: 
  - An integer representing the number of ghosts.

### `initializeVisibilityMatrix(self)`
Constructs and caches the visibility matrix if it has not been cached already.

- **Context**:
  - Uses the `view` of each cell to determine which other cells (ghost positions) are visible from a given cell and direction.
  - Caches the matrix for reuse, improving performance by avoiding recalculating visibility for the same layout.

### `isWall(self, pos)`
Checks if a specific position is a wall.

- **Parameters**:
  - `pos`: A tuple representing the (x, y) coordinates of the position.

- **Returns**: 
  - `True` if the position is a wall; otherwise `False`.

### `getRandomLegalPosition(self)`
Gets a random position on the board that is not a wall.

- **Returns**: 
  - A tuple representing the (x, y) coordinates of a random legal position.

### `getRandomCorner(self)`
Returns a random corner position on the board.

- **Returns**: 
  - A tuple representing the coordinates of a random corner.

### `getFurthestCorner(self, pacPos)`
Finds and returns the corner position that is furthest from Pacman's current position.

- **Parameters**:
  - `pacPos`: A tuple representing the (x, y) coordinates of Pacman's position.

- **Returns**: 
  - A tuple representing the coordinates of the furthest corner.

### `isVisibleFrom(self, ghostPos, pacPos, pacDirection)`
Determines if a ghost is visible from Pacman's position and direction.

- **Parameters**:
  - `ghostPos`: A tuple representing the (x, y) coordinates of the ghost.
  - `pacPos`: A tuple representing the (x, y) coordinates of Pacman.
  - `pacDirection`: The current direction of Pacman.

- **Returns**: 
  - `True` if the ghost is visible; otherwise `False`.

### `__str__(self)`
Returns a string representation of the layout.

- **Returns**: 
  - A string of the layout text, with each line separated by a newline character.

### `deepCopy(self)`
Creates a deep copy of the current layout.

- **Returns**: 
  - A new `Layout` instance that is a copy of the current layout.

### `processLayoutText(self, layoutText)`
Processes the layout text to populate walls, food, capsules, and agent positions.

- **Parameters**:
  - `layoutText`: A list of strings representing the layout of the game board.

### `processLayoutChar(self, x, y, layoutChar)`
Processes a character from the layout text to update the game board properties.

- **Parameters**:
  - `x`: The x-coordinate on the board.
  - `y`: The y-coordinate on the board.
  - `layoutChar`: The character representing a specific element in the layout.

## Functions

### `getLayout(name, back=2)`
Loads a layout by name from the file system. 

- **Parameters**:
  - `name`: Name of the layout to load.
  - `back`: A counter to go back in the directory if not found.

- **Returns**: 
  - A `Layout` instance or `None` if the layout could not be found.

### `tryToLoad(fullname)`
Attempts to load a layout from the given full file path.

- **Parameters**:
  - `fullname`: The full path to the layout file.

- **Returns**: 
  - A `Layout` instance if successfully loaded; `None` otherwise.