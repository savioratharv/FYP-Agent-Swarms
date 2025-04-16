# TextDisplay Module

## Module Purpose
The `textDisplay.py` module is designed to provide a text-based display for the Pacman game, allowing users to visualize the game's state through console output. It defines classes for graphical representation, including a null graphics class for situations when visual output is not required. The module manages the rendering of game states and updates based on the player's actions and game events.

## Author List
- John DeNero: Principal Developer
- Dan Klein: Core Developer
- Brad Miller: Autograding Implementation
- Nick Hay: Autograding Support
- Pieter Abbeel: Autograding Support

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- pacman (version >= 0.1.0)

## Public Interface Exports
- `NullGraphics`
- `PacmanGraphics`

## Internal Implementation Details
- The module provides two classes, `NullGraphics` and `PacmanGraphics`, to handle rendering in different contexts. `NullGraphics` offers a placeholder for graphics when no output is desired, while `PacmanGraphics` offers functionality for rendering game state updates.
- The module utilizes timing functions to control the refresh rate of the display.

## Constant Definitions
- `DRAW_EVERY`: Controls the frequency of drawing updates.
- `SLEEP_TIME`: Time in seconds to pause between updates.
- `DISPLAY_MOVES`: Boolean to toggle displaying moves in the console.
- `QUIET`: Boolean to suppress output.

## Class/Function Relationships
- The `PacmanGraphics` class interacts with the `state` object to obtain the current game state used for drawing.
- The `NullGraphics` class serves as a baseline for scenarios where no graphics are needed.

## Class: NullGraphics
### Overview
Provides a placeholder graphics implementation that suppresses rendering but retains method signatures for compatibility.

### Methods
- `initialize(state, isBlue=False)`: Initializes graphic settings.
- `update(state)`: Updates the current state.
- `checkNullDisplay()`: Returns true if the display is a null graphics.
- `pause()`: Pauses execution for a defined period.
- `draw(state)`: Outputs the current state to the console.
- `updateDistributions(dist)`: No operation.
- `finish()`: Finalizes any required processes.

### Usage
```python
null_graphics = NullGraphics()
null_graphics.initialize(game_state)
null_graphics.draw(game_state)
```

## Class: PacmanGraphics
### Overview
Manages the rendering of Pacman game states and accumulates scoring and game turn data.

### Methods
- `__init__(speed=None)`: Initializes a graphical display with an optional speed parameter.
- `initialize(state, isBlue=False)`: Prepares the display for the game state.
- `update(state)`: Updates the graphics and prints game state based on turn and moves.
- `pause()`: Controls the speed of the display by pausing.
- `draw(state)`: Renders the current game state to the console.
- `finish()`: Performs cleanup operations.

### Usage
```python
pacman_graphics = PacmanGraphics(speed=0.5)
pacman_graphics.initialize(game_state)
pacman_graphics.update(game_state)
```

## Revision History
| Date Modified | Version Delta | Change Description                          | Author Initials |
|---------------|---------------|--------------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial version created.                   | JD, DK           |