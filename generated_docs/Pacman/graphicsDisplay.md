# Pacman Graphics Display

## Module Purpose
This module provides a graphical interface for the Pacman game, enabling visual representation 
of the grid, agents, and their interactions. It supports elements such as walls, food, capsules, 
and both Pacman and ghost animations. The graphics are designed to enhance gameplay by providing 
an intuitive and engaging visual output.

## Authors
- John DeNero (Lead Developer)
- Dan Klein (Graphics Designer)
- Brad Miller (Student Autograder Developer)
- Nick Hay (Student Autograder Developer)
- Pieter Abbeel (Student Autograder Developer)

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modification Date: 2023-10-10

## Version
Version: 1.0.0

## Dependencies
- graphicsUtils >= 1.0
- game >= 1.0

## Public Interface Exports
- `class InfoPane`
- `class PacmanGraphics`
- `class FirstPersonPacmanGraphics`
- Functions for drawing elements like walls, food, capsules, and agents.

## Internal Implementation Details
This module consists of classes and functions that handle the graphical output of 
the Pacman game. Key implementation aspects include:
- The `InfoPane` class for displaying game information such as score and ghost distances.
- The `PacmanGraphics` and `FirstPersonPacmanGraphics` classes that manage the drawing 
of agents and game objects, including movement and animations.
- Drawing utilities that translate game coordinates into screen coordinates.

## Constant Definitions
- `DEFAULT_GRID_SIZE`: Default size for each grid square.
- `INFO_PANE_HEIGHT`: Height of the information display area.
- `BACKGROUND_COLOR`: Color used for the background.
- `WALL_COLOR`: Color used for the walls.
- `FOOD_COLOR`: Color used for food items.
- `PACMAN_COLOR`: Color of Pacman.
- `CAPSULE_COLOR`: Color of power capsules.
- `SCARED_COLOR`: Color representing scared ghosts.
  
## Class/Function Relationships
- `InfoPane` manages the display of the game score and distance to ghosts.
- `PacmanGraphics` is responsible for rendering the various game objects and their movements.
- `FirstPersonPacmanGraphics` extends `PacmanGraphics` for a first-person view.

## Docstrings

### InfoPane Class
```python
class InfoPane:
    """
    Displays the game's information pane.

    Parameters
    ----------
    layout : Layout
        The layout of the game.
    gridSize : float
        The size of each grid square.

    Methods
    -------
    toScreen(pos, y=None) -> Tuple[float, float]
        Translates a point to screen coordinates.

    drawPane() -> None
        Draws the initial information pane.

    updateScore(score) -> None
        Updates the displayed score.

    updateGhostDistances(distances) -> None
        Updates distance information to ghosts.
    """
```

### PacmanGraphics Class
```python
class PacmanGraphics:
    """
    Handles the drawing and visualization for Pacman and the game grid.

    Parameters
    ----------
    zoom : float, optional
        Zoom factor for the graphics.
    frameTime : float, optional
        Time delay for frame animation.
    capture : bool, optional
        Flag to indicate capture mode.

    Methods
    -------
    initialize(state, isBlue=False) -> None
        Initializes the graphics with the game state.
    
    drawStaticObjects(state) -> None
        Draws static objects such as walls and food.
    
    drawAgentObjects(state) -> None
        Draws agent objects (Pacman and ghosts).
    
    update(newState) -> None
        Updates the graphics based on the new game state.
    
    removeFood(cell) -> None
        Removes food from the specified cell.
    
    removeCapsule(cell) -> None
        Removes a capsule from the specified cell.
    """
```

### FirstPersonPacmanGraphics Class
```python
class FirstPersonPacmanGraphics(PacmanGraphics):
    """
    Extends PacmanGraphics for first-person visuals.

    Parameters
    ----------
    zoom : float, optional
        Zoom factor for the graphics.
    showGhosts : bool, optional
        Flag to show ghosts.
    capture : bool, optional
        Flag to indicate capture mode.

    Methods
    -------
    initialize(state, isBlue=False) -> None
        Initializes the graphics with the game state for first-person view.
    
    lookAhead(config, state) -> None
        Handles ghost drawing based on visibility.
    """
```

## Revision History
| Date Modified | Version Delta | Change Description                             | Author Initials |
|---------------|---------------|-----------------------------------------------|-------------------|
| 2023-10-01    | 1.0.0         | Initial creation of graphics display module. | JDN, DK           |
| 2023-10-10    | 1.0.1         | Added first-person graphics feature.          | JDN, DK           |