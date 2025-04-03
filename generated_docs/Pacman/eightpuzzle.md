# Documentation for `eightpuzzle.py`

## Overview
The `eightpuzzle.py` module implements the mechanics and search strategies for the Eight Puzzle problem. It defines the `EightPuzzleState` class representing the state of the puzzle and the `EightPuzzleSearchProblem` class defining the search problem. The module includes methods for legal moves, state transitions, and searching for solutions.

## Class: `EightPuzzleState`

### `__init__(self, numbers)`
- **Purpose**: Initialize an instance of EightPuzzleState with a specific ordering of numbers.
- **Parameters**: 
  - `numbers`: A list of integers (0-8) representing the puzzle configuration, where 0 denotes the blank space.
- **Key Tasks**: 
  - Reverses the input list to prepare it for 2D representation.
  - Populates the `cells` attribute with a 3x3 grid.
  - Sets the `blankLocation` where the blank space (0) is located.

### `isGoal(self)`
- **Purpose**: Check if the current state is in the goal configuration.
- **Returns**: 
  - `True` if the puzzle is in the goal state, `False` otherwise.

### `legalMoves(self)`
- **Purpose**: Determine the possible legal moves from the current state.
- **Returns**: 
  - A list of strings representing legal moves: `['up', 'down', 'left', 'right']`.

### `result(self, move)`
- **Purpose**: Generate a new EightPuzzleState based on the provided move.
- **Parameters**: 
  - `move`: A string indicating the action ('up', 'down', 'left', 'right').
- **Returns**: 
  - A new `EightPuzzleState` reflecting the state after applying the move.
- **Key Tasks**: 
  - Validates the move.
  - Creates a copy of the current state.
  - Updates the new state to reflect the change.

### `__eq__(self, other)`
- **Purpose**: Overload equality operator to compare two Puzzle states.
- **Parameters**: 
  - `other`: Another instance of `EightPuzzleState`.
- **Returns**: 
  - `True` if both states are identical, `False` otherwise.

### `__hash__(self)`
- **Purpose**: Generate a hash value for the `EightPuzzleState` instance.
- **Returns**: 
  - An integer hash value computed based on the state.

### `__getAsciiString(self)`
- **Purpose**: Generate a string representation of the puzzle for display.
- **Returns**: 
  - A formatted string displaying the 3x3 grid.

### `__str__(self)`
- **Purpose**: Return a string representation of the current puzzle state.
- **Returns**: 
  - A string that utilizes `__getAsciiString()`.

## Class: `EightPuzzleSearchProblem`

### `__init__(self, puzzle)`
- **Purpose**: Initialize an instance of EightPuzzleSearchProblem with a given puzzle.
- **Parameters**: 
  - `puzzle`: An instance of `EightPuzzleState` representing the starting state.

### `getStartState(self)`
- **Purpose**: Retrieve the starting state of the search problem.
- **Returns**: 
  - The initial puzzle state.

### `isGoalState(self, state)`
- **Purpose**: Evaluate whether a given state is the goal state.
- **Parameters**: 
  - `state`: An instance of `EightPuzzleState`.
- **Returns**: 
  - `True` if the state is the goal state; otherwise, `False`.

### `getSuccessors(self, state)`
- **Purpose**: Generate the successors of a given state.
- **Parameters**: 
  - `state`: An instance of `EightPuzzleState`.
- **Returns**: 
  - A list of tuples containing each successor state, the action taken, and the step cost (always 1.0).

### `getCostOfActions(self, actions)`
- **Purpose**: Calculate the total cost of performing a sequence of actions.
- **Parameters**: 
  - `actions`: A list of actions (moves) to perform.
- **Returns**: 
  - Total cost as an integer representing the number of actions.

## Functions

### `loadEightPuzzle(puzzleNumber)`
- **Purpose**: Load a specific puzzle based on a predefined index.
- **Parameters**: 
  - `puzzleNumber`: An index (0-5) corresponding to one of the predefined puzzles.
- **Returns**: 
  - An `EightPuzzleState` object for the specified puzzle.

### `createRandomEightPuzzle(moves=100)`
- **Purpose**: Generate a random puzzle configuration by executing random moves.
- **Parameters**: 
  - `moves`: The number of random moves to apply (default is 100).
- **Returns**: 
  - An instance of `EightPuzzleState` representing a randomized puzzle configuration.

## Main Execution
In the main block, a random puzzle is created, and its solution is sought using breadth-first search. The path of moves is printed, and the state transitions are displayed step-by-step with user interaction.