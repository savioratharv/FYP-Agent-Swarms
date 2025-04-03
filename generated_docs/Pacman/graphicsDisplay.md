# Pacman Graphics Display Module

## Overview
The `graphicsDisplay.py` file contains the implementation for rendering visuals in a Pacman game, handling the display of agents, walls, food, capsules, and game information. It integrates with a tkinter-based graphical utility to facilitate graphical representation of game states.

## Classes

### 1. `InfoPane`
This class is responsible for creating and managing the information display pane, showing score and ghost distances.

#### Methods:
- **`__init__(self, layout, gridSize)`**
  - Initializes the info pane with layout dimensions and grid size.

- **`toScreen(self, pos, y=None)`**
  - Converts a point relative to the info pane into screen coordinates.

- **`drawPane(self)`**
  - Draws the initial scoreboard.

- **`initializeGhostDistances(self, distances)`**
  - Initializes ghost distance displays based on the provided distances.

- **`updateScore(self, score)`**
  - Updates the score display.

- **`setTeam(self, isBlue)`**
  - Sets the team display (Red or Blue).

- **`updateGhostDistances(self, distances)`**
  - Updates the displayed ghost distances.

- **`drawGhost(self)`**
  - Placeholder for drawing ghost representations.

- **`drawPacman(self)`**
  - Placeholder for drawing Pacman representations.

- **`drawWarning(self)`**
  - Placeholder for drawing warning messages.

- **`clearIcon(self)`**
  - Placeholder for clearing graphical icons.

- **`updateMessage(self, message)`**
  - Placeholder for updating messages on screen.

- **`clearMessage(self)`**
  - Placeholder for clearing messages from the display.


### 2. `PacmanGraphics`
This class manages the rendering of the Pacman game graphics including the game state, agents (Pacman and ghosts), and game objects.

#### Methods:
- **`__init__(self, zoom=1.0, frameTime=0.0, capture=False)`**
  - Initializes graphics settings such as zoom level and frame time.

- **`checkNullDisplay(self)`**
  - Checks if the display has been initialized.

- **`initialize(self, state, isBlue=False)`**
  - Initializes graphical display for the current game state.

- **`startGraphics(self, state)`**
  - Sets up the graphical window and layout for rendering.

- **`drawDistributions(self, state)`**
  - Draws a grid representation of belief distributions.

- **`drawStaticObjects(self, state)`**
  - Renders walls, food, and capsules in the game.

- **`drawAgentObjects(self, state)`**
  - Draws agents (Pacman and ghosts) in the game.

- **`swapImages(self, agentIndex, newState)`**
  - Swaps the graphical representation of agents when states change.

- **`update(self, newState)`**
  - Updates the display to reflect the new game state.

- **`make_window(self, width, height)`**
  - Creates the graphical window with specified dimensions.

- **`drawPacman(self, pacman, index)`**
  - Draws the Pacman character on the screen.

- **`getEndpoints(self, direction, position=(0,0))`**
  - Calculates endpoint angles for the Pacman graphic based on direction.

- **`movePacman(self, position, direction, image)`**
  - Moves the Pacman graphic to a new position on the screen.

- **`animatePacman(self, pacman, prevPacman, image)`**
  - Animates the Pacman movement based on its previous state.

- **`getGhostColor(self, ghost, ghostIndex)`**
  - Determines the color of a ghost based on its state.

- **`drawGhost(self, ghost, agentIndex)`**
  - Draws ghost characters on the screen.

- **`moveEyes(self, pos, dir, eyes)`**
  - Moves the ghost's eyes to simulate looking around.

- **`moveGhost(self, ghost, ghostIndex, prevGhost, ghostImageParts)`**
  - Moves the ghost graphic to its new position and updates its look.

- **`getPosition(self, agentState)`**
  - Retrieves the position of an agent from its state.

- **`getDirection(self, agentState)`**
  - Retrieves the current direction of an agent.

- **`finish(self)`**
  - Ends graphical representation by closing the window and clearing resources.

- **`to_screen(self, point)`**
  - Converts a game coordinate to screen coordinates.

- **`drawWalls(self, wallMatrix)`**
  - Renders the game's walls based on the wall matrix.

- **`drawFood(self, foodMatrix)`**
  - Draws food items on the screen.

- **`drawCapsules(self, capsules)`**
  - Renders capsules on the screen.

- **`removeFood(self, cell, foodImages)`**
  - Removes food items from the display.

- **`removeCapsule(self, cell, capsuleImages)`**
  - Removes capsules from the display.

- **`drawExpandedCells(self, cells)`**
  - Draws an overlay of expanded grid positions for search agents.

- **`clearExpandedCells(self)`**
  - Clears the display of expanded cells.

- **`updateDistributions(self, distributions)`**
  - Updates the display to show agents' belief distributions.

### 3. `FirstPersonPacmanGraphics`
A specialized version of `PacmanGraphics` that provides a first-person view.

#### Methods:
- **`__init__(self, zoom=1.0, showGhosts=True, capture=False, frameTime=0)`**
  - Initializes first-person graphics settings.

- **`initialize(self, state, isBlue=False)`**
  - Initializes the display for a first-person perspective.

- **`lookAhead(self, config, state)`**
  - Prepares the display for the next visual frame based on agent's direction.

- **`getGhostColor(self, ghost, ghostIndex)`**
  - Retrieves ghost color for display.

- **`getPosition(self, ghostState)`**
  - Retrieves the position of a ghost considering visibility settings.

## Functions

### 1. `add(x, y)`
- **Input Parameters**: 
  - `x`: Tuple indicating the first point.
  - `y`: Tuple indicating the second point.
- **Output Parameters**: 
  - A new tuple representing the sum of the two points.
- **Role**: Adds two coordinate tuples together.

### 2. `saveFrame()`
- **Input Parameters**: 
  - None.
- **Output Parameters**: 
  - None.
- **Role**: Saves the current graphical output as a PostScript file for later use.

## Constants
- `DEFAULT_GRID_SIZE`: Default size for the game grid.
- `INFO_PANE_HEIGHT`: Height of the information pane.
- `BACKGROUND_COLOR`: RGB color for the background.
- `WALL_COLOR`: Color for walls.
- `FOOD_COLOR`: Color for food items.
- `CAPSULE_COLOR`: Color for capsules.
- Various colors and sizes formatted for graphical representations.

## Summary
This file creates a graphical interface for the Pacman game, encapsulating the logic for rendering game elements and updating their display based on the current game states. It interacts with an external graphics utility to leverage Tkinter's capabilities for dynamic and interactive graphics.