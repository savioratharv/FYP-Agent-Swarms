# Text Display Module

## Project Name
Pacman Text Display

## Module Purpose
The purpose of this module is to provide graphical output for the Pacman game. It includes classes 
to render the game's state either in a graphical display or as text output. The module can 
initialize the display, update it based on game state changes, and conclude the display after the game ends. 
This functionality is essential for providing visual feedback during gameplay for debugging and educational purposes.

## Author List
- John DeNero - Lead Developer
- Dan Klein - Lead Developer
- Brad Miller - Student Side Autograding Development
- Nick Hay - Student Side Autograding Development
- Pieter Abbeel - Student Side Autograding Development

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Modification Date: 2023-10-20

## Version
1.0.0

## Dependency List
- pacman >= 0.1.0

## Public Interface Exports
- `NullGraphics` class
- `PacmanGraphics` class

## Internal Implementation Details
The module defines two primary classes: `NullGraphics` and `PacmanGraphics`. 
`NullGraphics` serves as a placeholder that does not render any interface, while 
`PacmanGraphics` provides functionality to display the current state of the game 
and update it in accordance with game events.

## Constant Definitions
- `DRAW_EVERY` (int): Frequency of updates to the display.
- `SLEEP_TIME` (int): Delay between frames in seconds; can be modified in the 
  constructor of `PacmanGraphics`.
- `DISPLAY_MOVES` (bool): Option to toggle displaying moves of Pacman and ghosts.
- `QUIET` (bool): Suppresses output when set to True.

## Class/Function Relationships
- `NullGraphics`: Designed for situations where graphical output is not required.
- `PacmanGraphics`: Extends the functionality to handle the graphical representation 
  of the Pacman game state, including movement updates and drawing the game state.

### NullGraphics Class

```python
class NullGraphics:
    """
    A class to represent a null display for the Pacman game.

    This class serves as a placeholder that does not render any graphics but can 
    be used to maintain the interface for various functions requiring a display.

    Methods:
    - initialize(state, isBlue=False): Initializes the null display.
    - update(state): Updates the display with the current state.
    - checkNullDisplay(): Checks if the display is a null display.
    - pause(): Pauses execution for the defined sleep time.
    - draw(state): Prints the state as text.
    - updateDistributions(dist): Placeholder for updating probability distributions.
    - finish(): Placeholder method to finalize the display.
    """

    def initialize(self, state, isBlue=False):
        """
        Initializes the null graphics display with the provided game state.

        Parameters:
        - state: The current state of the game.
        - isBlue (bool): Indicates if the display is for a blue agent.
        
        Returns: None
        """

    def update(self, state):
        """
        Updates the state of the null graphics display.

        Parameters:
        - state: The current state of the game.

        Returns: None
        """

    def checkNullDisplay(self):
        """
        Checks if this display is a null display.

        Returns:
        - bool: Always returns True.
        """

    def pause(self):
        """
        Pauses execution for the defined sleep time.

        Returns: None
        """

    def draw(self, state):
        """
        Prints the current game state as text.

        Parameters:
        - state: The current state of the game.

        Returns: None
        """

    def updateDistributions(self, dist):
        """
        Updates the display with probability distributions.

        Parameters:
        - dist: The distribution information to be displayed.

        Returns: None
        """

    def finish(self):
        """
        Finalizes the graphics display.

        Returns: None
        """
```

### PacmanGraphics Class

```python
class PacmanGraphics:
    """
    A class to represent the graphical output for the Pacman game.

    This class provides functionality to render the game state, 
    update it based on player moves, and manage the drawing of 
    the game in a graphical format.

    Methods:
    - __init__(speed=None): Initializes the graphics and sets up delay speed.
    - initialize(state, isBlue=False): Prepares the graphics display with the initial state.
    - update(state): Updates the graphics display based on current game state.
    - pause(): Pauses execution for the defined sleep time.
    - draw(state): Renders the current game state in a textual format.
    - finish(): Finalizes and clears the display.
    """

    def __init__(self, speed=None):
        """
        Initializes the Pacman graphics display and sets the display speed.

        Parameters:
        - speed (int): The desired speed of the display updates in seconds.
        
        Returns: None
        """

    def initialize(self, state, isBlue=False):
        """
        Initializes the graphics display with the provided game state.

        Parameters:
        - state: The current state of the game.
        - isBlue (bool): Indicates if the display is for a blue agent.
        
        Returns: None
        """

    def update(self, state):
        """
        Updates the graphics display according to the game state.

        Parameters:
        - state: The current state of the game.

        Returns: None
        """

    def pause(self):
        """
        Pauses execution for the defined sleep time.

        Returns: None
        """

    def draw(self, state):
        """
        Renders the current game state as text output.

        Parameters:
        - state: The current state of the game.

        Returns: None
        """

    def finish(self):
        """
        Finalizes and clears the graphics display.

        Returns: None
        """
```

## Revision History Table
| Date Modified | Version Delta | Change Description                          | Author Initials |
|---------------|---------------|--------------------------------------------|------------------|
| 2023-10-01    | 1.0.0         | Initial creation of the textDisplay module | JD, DK            |
| 2023-10-20    | 1.0.1         | Added detailed docstrings and comments     | JD                |