# Pacman textDisplay.py Documentation

## Overview
The `textDisplay.py` file is part of the Pacman AI projects developed at UC Berkeley. It handles the graphical display of the game state, either through a null graphics implementation that outputs text or a more advanced graphical method (PacmanGraphics). It supports the visualization of game states, demonstrating the positions of Pacman and ghosts, along with the scores.

## Classes

### NullGraphics
A class that provides a no-operation (null) graphics implementation. This is useful for situations where graphical output is unnecessary.

#### Methods
- **initialize(self, state, isBlue=False)**  
  Initializes the display. No operation is performed since this is a null graphic implementation.

- **update(self, state)**  
  A placeholder method that does not alter any state since there is no graphical representation.

- **checkNullDisplay(self)**  
  Returns `True`, indicating that this is a null display class.

- **pause(self)**  
  Introduces a delay in execution, based on `SLEEP_TIME`.

- **draw(self, state)**  
  Outputs the string representation of the game state to the console.

- **updateDistributions(self, dist)**  
  A placeholder method that does nothing with distributions; included for interface completeness.

- **finish(self)**  
  A placeholder method that does not perform any action upon finishing.

### PacmanGraphics
A class responsible for rendering the game state in a more interactive graphical representation.

#### Methods
- **__init__(self, speed=None)**  
  Initializes the graphic display with an optional speed parameter to set the `SLEEP_TIME` for animation pacing.

- **initialize(self, state, isBlue=False)**  
  Prepares the graphical display for the current state. Calls `draw` to render the initial state and pauses for the specified duration.

- **update(self, state)**  
  Updates the display based on the current state. It manages the turn sequence and potentially outputs information regarding player moves and scores every few turns. It calls `draw` when conditions are met.

- **pause(self)**  
  Introduces a delay in execution based on the configured `SLEEP_TIME`.

- **draw(self, state)**  
  Outputs the string representation of the game state to the console, visually updating the state of the game.

- **finish(self)**  
  A placeholder method that does not perform any action upon completion of the game.

## Constants
- **DRAW_EVERY**  
  A constant that specifies how often to draw the state (every 1 turn by default).

- **SLEEP_TIME**  
  Time interval (in seconds) that the program will pause during updates to control the speed of the display.

- **DISPLAY_MOVES**  
  A boolean flag that, when set to `True`, prints the details of the moves made by Pacman and the positions of ghosts.

- **QUIET**  
  A boolean flag that suppresses output if set to `True`.