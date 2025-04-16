# Pacman Layout Module Documentation

## File Header

**Project Name:** Pacman Game

**Module Purpose:**  
The `layout.py` module manages the configuration and representation of the game board for the Pacman game. It interprets layout text to generate the game's walls, food, capsules, and agent positions. It also provides functionality for determining visibility and positions on the grid, including random legal positions and corner retrievals.

**Authors:**  
- John DeNero (Lead Developer)  
- Dan Klein (Developer)  
- Brad Miller (Autograding Implementation)  
- Nick Hay (Autograding Implementation)  
- Pieter Abbeel (Autograding Implementation)  

**Creation/Modification Dates:**  
2023-10-01

**Version:**  
1.0.0

**Dependencies:**  
- util (>= 1.0.0)  
- game (>= 1.0.0)  
- os (>= 1.0.0)  
- random (>= 1.0.0)  
- functools (>= 1.0.0)  

## Public Interface Exports

- `Layout`: Class to represent and manage the game board layout.
- `getLayout(name, back=2)`: Function to retrieve a layout by name.
- `tryToLoad(fullname)`: Function to attempt to load a layout from a specified file.

## Internal Implementation Details

The `Layout` class initializes the game board based on the provided layout text, constructs walls, food, and agents, and computes visibility matrices. The layout is processed character by character, allowing for varied configurations based on given input. Internal caching mechanisms speed up repeated visibility queries, and utility functions facilitate easier data retrieval.

## Constant Definitions

**VISIBILITY_MATRIX_CACHE:**  
A global cache dictionary for storing precomputed visibility matrices to avoid 
recalculation.

## Class and Function Relationships

- `Layout` class relies on functions from `util` for distance calculations and 
`game` for grid manipulations.
- `getLayout` and `tryToLoad` functions interact with the file system to load layout definitions.

## Class `Layout`

### Overview

The `Layout` class encapsulates all the static information about the Pacman game board. It allows for easy management of walls, food, capsules, ghost positions, and Pacman positions.

### Methods

#### `__init__(self, layoutText)`

- **Functionality Overview:**  
Initializes the layout based on the provided text representation, sets dimensions, walls, food, capsules, and agent positions.

- **Parameters:**
  - `layoutText (list of str)`: Lines of text representing the game layout.
  
- **Returns:**  
None.

- **Usage Example:**
```python
layout = Layout(["%%%%%%%","%.....%","%.....%","%%%%%%%"])
```

#### `getNumGhosts(self)`

- **Functionality Overview:**  
Returns the number of ghosts present in the layout.

- **Returns:**  
int: Number of ghosts in the layout.

- **Usage Example:**
```python
num_ghosts = layout.getNumGhosts()
```

#### `initializeVisibilityMatrix(self)`

- **Functionality Overview:**  
Calculates and stores a visibility matrix for the current layout to assist with 
determining visibility from various positions.

- **Returns:**  
None.

#### `isWall(self, pos)`

- **Functionality Overview:**  
Checks if the specified position is a wall.

- **Parameters:**
  - `pos (tuple)`: A tuple (x, y) representing the coordinates to check.

- **Returns:**  
bool: `True` if the position is a wall, otherwise `False`.

- **Usage Example:**
```python
is_wall = layout.isWall((2, 3))
```

#### `getRandomLegalPosition(self)`

- **Functionality Overview:**  
Returns a random legal position on the grid that is not a wall.

- **Returns:**  
tuple: A valid (x, y) position.

- **Usage Example:**
```python
position = layout.getRandomLegalPosition()
```

#### `getRandomCorner(self)`

- **Functionality Overview:**  
Returns a random corner position on the grid, favoring positions near the edges.

- **Returns:**  
tuple: A corner position.

- **Usage Example:**
```python
corner = layout.getRandomCorner()
```

#### `getFurthestCorner(self, pacPos)`

- **Functionality Overview:**  
Determines the farthest corner from the given Pacman position.

- **Parameters:**
  - `pacPos (tuple)`: A tuple (x, y) representing the Pacman position.

- **Returns:**  
tuple: The coordinates of the farthest corner.

- **Usage Example:**
```python
furthest = layout.getFurthestCorner((5, 5))
```

#### `isVisibleFrom(self, ghostPos, pacPos, pacDirection)`

- **Functionality Overview:**  
Checks if a ghost is visible from the Pacman's position in a specified direction.

- **Parameters:**
  - `ghostPos (tuple)`: The position (x, y) of the ghost.
  - `pacPos (tuple)`: The position (x, y) of Pacman.
  - `pacDirection (str)`: The direction in which Pacman is facing.

- **Returns:**  
bool: `True` if the ghost is visible, otherwise `False`.

- **Usage Example:**
```python
visible = layout.isVisibleFrom((3, 3), (2, 2), "NORTH")
```

#### `__str__(self)`

- **Functionality Overview:**  
Returns a string representation of the layout.

- **Returns:**  
str: The layout as a formatted string.

- **Usage Example:**
```python
print(str(layout))
```

#### `deepCopy(self)`

- **Functionality Overview:**  
Creates and returns a deep copy of the current layout instance.

- **Returns:**  
Layout: A new instance of the Layout class with the same properties.

- **Usage Example:**
```python
layout_copy = layout.deepCopy()
```

### Method Information

#### `processLayoutText(self, layoutText)`

- **Functionality Overview:**  
Processes the layout text to populate walls, food, capsules, and agent positions.

- **Parameters:**
  - `layoutText (list of str)`: Lines of text representing the game layout.

- **Returns:**  
None.

- **Usage Example:**
```python
layout.processLayoutText(["%%%", "%P%", "%%%"])
```

#### `processLayoutChar(self, x, y, layoutChar)`

- **Functionality Overview:**  
Processes a single character from the layout text and updates the grid accordingly.

- **Parameters:**
  - `x (int)`: The x-coordinate.
  - `y (int)`: The y-coordinate.
  - `layoutChar (str)`: The character to process.

- **Returns:**  
None.

## Revision History

| Date Modified | Version Delta | Change Description                      | Author Initials |
|---------------|---------------|-----------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of Layout management. | JD                |
| 2023-10-02    | 1.0.1        | Added documentation and enhanced clarity. | JD                |