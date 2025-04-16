# Keyboard Agents

## Module Purpose
This module defines keyboard-controlled agents for navigating a virtual environment, specifically in the context of the Pacman AI project. It allows user interaction through keyboard inputs, facilitating real-time gameplay adjustments. The module includes two agent classes, `KeyboardAgent` and `KeyboardAgent2`, which cater to different key mappings for user control.

## Author List
- John DeNero (Lead Developer)
- Dan Klein (Co-Developer)
- Brad Miller (Technical Support)
- Nick Hay (Testing & Quality Assurance)
- Pieter Abbeel (Research Advisor)

## Creation/Modification Dates
- Creation Date: 2023-01-15
- Last Modified Date: 2023-10-01

## Version
Version: 1.0.0

## Dependency List
- game (Minimum Version: 1.0.0)
- graphicsUtils (Minimum Version: 1.0.0)

## Public Interface Exports
- `class KeyboardAgent(Agent)`: An agent controlled via keyboard input, allowing movement in four directions and a stop command.
- `class KeyboardAgent2(KeyboardAgent)`: A second variant of the keyboard agent with different key bindings.

## Internal Implementation Details
- `getAction(self, state)`: Determines the current action for the agent based on user inputs and game state.
- `getMove(self, legal)`: Maps the pressed keys to legal movements, considering the movement directions available in the game state.

## Constant Definitions
- `WEST_KEY`: Key for moving west.
- `EAST_KEY`: Key for moving east.
- `NORTH_KEY`: Key for moving north.
- `SOUTH_KEY`: Key for moving south.
- `STOP_KEY`: Key for stopping movement.

## Class/Function Relationships
- `KeyboardAgent` inherits from `Agent`.
- `KeyboardAgent2` inherits from `KeyboardAgent`.
- Uses external functions from the `graphicsUtils` module: `keys_waiting()` and `keys_pressed()`.

## Class and Method Documentation

### class KeyboardAgent(Agent)
This class defines an agent that can be controlled via keyboard inputs, allowing for simple movement in a game.

#### Parameters
- `index` (int): The index of the agent, used within the game.

#### Methods
- `getAction(state)`: Retrieves the next action based on keyboard input and game state.
  - **Parameters**
    - `state`: The current game state.
  - **Returns**
    - `str`: A string representing the action to take.

- `getMove(legal)`: Determines the move based on legal actions and keys pressed.
  - **Parameters**
    - `legal`: A list of legal actions available.
  - **Returns**
    - `str`: The chosen move direction.

#### Example
```python
agent = KeyboardAgent()
action = agent.getAction(current_game_state)
```

### class KeyboardAgent2(KeyboardAgent)
A second implementation of a keyboard-controlled agent with alternate key bindings.

#### Methods
- `getMove(legal)`: Same as in `KeyboardAgent` but with different key mappings.
  - **Parameters**
    - `legal`: A list of legal actions available.
  - **Returns**
    - `str`: The chosen move direction.

#### Example
```python
agent = KeyboardAgent2()
action = agent.getAction(current_game_state)
```

## Exception Hierarchy
- No specific exceptions are raised; however, improper use of the agent may lead to unexpected behavior.

## Revision History

| Date Modified | Version Delta | Change Description                             | Author Initials |
|---------------|---------------|------------------------------------------------|------------------|
| 2023-01-15    | 1.0.0         | Initial creation of the KeyboardAgent module. | JD               |
| 2023-10-01    | 1.0.1         | Added KeyboardAgent2 with different key bindings. | JD               |