# Pacman Graphics Display

## Module Purpose
This module provides the graphical interface for the Pacman game environment, allowing 
for the visualization of game elements such as the player (Pacman), ghosts, food, and walls. 
It handles rendering updates, animations, and displays the score and other game-related 
information in real time.

## Author List
- John DeNero: Lead Developer
- Dan Klein: Graphics Implementation
- Brad Miller: Student Autograding
- Nick Hay: Student Autograding
- Pieter Abbeel: Student Autograding

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified Date: 2023-10-20

## Version
- Version: 1.0.0

## Dependency List
- graphicsUtils >= 1.0.0
- game >= 1.0.0
- math >= 1.0.0
- time >= 1.0.0

## Public Interface Exports
- `class InfoPane`
- `class PacmanGraphics`
- `class FirstPersonPacmanGraphics`
- `def saveFrame()`

## Internal Implementation Details
The primary functionality involves initializing and updating a graphical window 
to visualize the game state. The module includes classes for managing various 
graphics aspects and rendering elements like walls, food, and agents dynamically.

## Constant Definitions
- `DEFAULT_GRID_SIZE = 30.0`
- `INFO_PANE_HEIGHT = 35`
- `BACKGROUND_COLOR = formatColor(0,0,0)`
- `WALL_COLOR = formatColor(0,0/255.0, 51.0/255.0, 255.0/255.0)`
- `PACMAN_COLOR = formatColor(255.0/255.0,255.0/255.0,61.0/255)`

## Class/Function Relationships
- `InfoPane` is responsible for displaying scores and ghost distances.
- `PacmanGraphics` handles the rendering of Pacman and ghosts including their 
animations and interactions.
- `FirstPersonPacmanGraphics` extends `PacmanGraphics` to provide a first-person 
view of the game.
- `saveFrame()` saves the graphical output as a postscript file.

## Docstrings

### InfoPane
```python
class InfoPane:
    """
    Manages the display of the information pane, which includes 
    score and ghost distance information.

    Parameters:
    layout: The game layout object for the current layout.
    gridSize: The size of each cell in pixels.

    Methods:
    - toScreen(pos, y=None): Translates grid positions to screen coordinates.
    - drawPane(): Initializes and draws the information pane.
    - updateScore(score): Updates the score display.
    - updateGhostDistances(distances): Updates the distances of ghosts.
    """
```

### PacmanGraphics
```python
class PacmanGraphics:
    """
    Manages the graphical display for the Pacman game.

    Parameters:
    zoom: Scale factor for the graphics.
    frameTime: Time per frame for animation.
    capture: Boolean flag for capturing mode.

    Methods:
    - initialize(state, isBlue=False): Initializes the display with the current game state.
    - drawPacman(pacman, index): Draws Pacman at the specified index.
    - drawGhost(ghost, agentIndex): Draws a ghost at the specified index.
    - update(newState): Updates the display based on the new game state.
    """
```

### FirstPersonPacmanGraphics
```python
class FirstPersonPacmanGraphics(PacmanGraphics):
    """
    Provides a first-person perspective of the Pacman game.

    Parameters:
    zoom: Scale factor for the graphics.
    showGhosts: Boolean flag to toggle ghost visibility.
    capture: Boolean flag for capturing mode.
    frameTime: Time per frame for animation.

    Methods:
    - lookAhead(config, state): Previews the view based on the current configuration.
    """
```

### saveFrame
```python
def saveFrame():
    """
    Saves the current graphical output as a postscript file.

    Returns:
    None: This function does not return a value. The frame is saved to the 
    specified output directory.

    Example:
    >>> saveFrame()
    This saves the current graphics state to a postscript file.
    """
```

## Revision History
| Date Modified | Version Delta | Change Description                       | Author |
|---------------|---------------|-----------------------------------------|--------|
| 2023-10-20    | 1.0.0        | Initial creation of graphical display. | JD     |
| 2023-10-01    | 0.1.0        | Basic setup and class structure defined.| DK     |