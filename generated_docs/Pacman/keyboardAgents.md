# Keyboard Agents Module Documentation

## Overview

The `keyboardAgents.py` module defines two classes that implement keyboard-controlled agents for the Pacman game. These agents allow players to control their movement within the game through keyboard inputs, facilitating interaction and gameplay.

## Class: `KeyboardAgent`

### Overview
The `KeyboardAgent` class represents an agent controlled by keyboard inputs. Players can use defined keys to navigate through the game.

### Methods

#### `__init__(self, index=0)`
- **Description**: Initializes the `KeyboardAgent` instance.
- **Parameters**: 
  - `index` (int): An optional index to identify the agent (default is `0`).
- **Attributes**:
  - `lastMove`: Stores the last move performed by the agent.
  - `index`: The index of the agent.
  - `keys`: A list to store currently pressed keys.

#### `getAction(self, state)`
- **Description**: Determines the action for the agent based on the current game state and keyboard input.
- **Parameters**: 
  - `state`: The current game state.
- **Returns**: A direction (action) for the agent to take.
- **Mechanism**:
  1. Retrieves any keys currently pressed and keys that were pressed since the last call using `keys_waiting()` and `keys_pressed()`.
  2. Obtains legal actions from the game state.
  3. Utilizes `getMove(legal)` to determine intended movement based on key inputs.
  4. If the agent is not moving (STOP), attempts to repeat the last move if it is still legal.
  5. If the resultant move is illegal, selects a random legal move.

#### `getMove(self, legal)`
- **Description**: Determines the best move given the current legal actions and the keys pressed.
- **Parameters**: 
  - `legal`: A list of legal actions available to the agent.
- **Returns**: A direction (move) chosen based on player input.
- **Mechanism**:
  1. Initializes move as STOP.
  2. Checks which keys are pressed and returns the corresponding direction if it is legal.

## Class: `KeyboardAgent2`

### Overview
The `KeyboardAgent2` class is a second agent controlled by distinct keyboard inputs, providing flexibility for multi-player scenarios.

### Methods

#### `getMove(self, legal)`
- **Description**: Determines the best move for the second agent, similar to `getMove` in `KeyboardAgent`, but uses different key bindings specific to this agent.
- **Parameters**: 
  - `legal`: A list of legal actions available to the agent.
- **Returns**: A direction (move) chosen based on player input.
- **Mechanism**:
  1. Initializes move as STOP.
  2. Checks for specific keys set for this agent and returns the corresponding direction if it is legal.