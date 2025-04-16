# Pacman Keyboard Agents Documentation

## Project Name
Pacman Keyboard Agents

## Module Purpose
This module defines keyboard-controlled agents for navigation within the Pacman game environment. It allows users to control characters using specified keys, enabling interactive gameplay. The agents respond to key presses and execute movements while ensuring they adhere to the game's movement rules.

## Author List
- John DeNero (Project Lead)
- Dan Klein (Co-developer)
- Brad Miller (Contributions)
- Nick Hay (Contributions)
- Pieter Abbeel (Contributions)

## Creation/Modification Dates
- Created: 2023-10-01
- Last Modified: 2023-10-01

## Version
1.0.0

## Dependencies
- game (>=1.0.0)
- graphicsUtils (>=1.0.0)

## Public Interface Exports
- `KeyboardAgent`: Class controlling the first player character with predefined keys.
- `KeyboardAgent2`: Class controlling the second player character with alternative keys.

## Internal Implementation Details
The `KeyboardAgent` and `KeyboardAgent2` classes handle user input for character movements within the game. They process key presses, manage legal moves, and maintain the last move state to enhance movement consistency.

## Constant Definitions
- `WEST_KEY`: Key binding for moving west (left).
- `EAST_KEY`: Key binding for moving east (right).
- `NORTH_KEY`: Key binding for moving north (up).
- `SOUTH_KEY`: Key binding for moving south (down).
- `STOP_KEY`: Key binding for stopping movement.

## Class/Function Relationships
- `KeyboardAgent`: Inherits core functionality from the `Agent` class.
- `KeyboardAgent.getAction`: Retrieves user input and calculates the legal move based on the current game state.
- `KeyboardAgent.getMove`: Determines the direction of movement based on pressed keys.

## Class Documentation

### Class KeyboardAgent
An agent controlled by keyboard input.

#### Methods
- `__init__(self, index=0)`: Initializes the agent with default parameters.
- `getAction(self, state)`: Determines the next action based on keyboard input and game state.
- `getMove(self, legal)`: Calculates the move direction based on keys pressed.

##### Parameters
- `index`: An integer representing the agent's index within the game environment (default: 0).

##### Returns
- `str`: Direction of movement as defined in the `Directions` class.

##### Usage Example
```python
agent = KeyboardAgent(0)
next_action = agent.getAction(current_game_state)
```
##### Exception Hierarchy
- May raise errors related to state management or input processing as defined in the parent `Agent` class.

---

### Class KeyboardAgent2
A second agent controlled by the keyboard, with different key mappings.

#### Methods
- `getMove(self, legal)`: Determines movement for the second agent based on specific key bindings.

##### Parameters
- `legal`: A list of legal actions according to the current game state.

##### Returns
- `str`: Direction of movement as defined in the `Directions` class.

##### Usage Example
```python
agent2 = KeyboardAgent2()
next_action = agent2.getAction(current_game_state)
```
##### Exception Hierarchy
- Same as `KeyboardAgent`, with focus on managing input for the second agent.

## Revision History

| Date Modified | Version Delta | Change Description             | Author Initials |
|---------------|---------------|--------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of the module | JD, DK           |