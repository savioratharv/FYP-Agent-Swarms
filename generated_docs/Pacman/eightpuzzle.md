# Eight Puzzle

## Module Purpose
This module implements the mechanics of the Eight Puzzle, which consists of a 3x3 grid with eight numbered tiles and one empty space. Its primary goal is to facilitate search problem representation, allowing for solving the puzzle through various algorithms. The code defines an `EightPuzzleState` class and an associated `EightPuzzleSearchProblem` class that utilizes a search method to transition between states in pursuit of the goal configuration.

## Author List
- John DeNero - Lead Developer
- Dan Klein - Project Manager
- Brad Miller - Student Side Autograder Developer
- Nick Hay - Student Side Autograder Developer
- Pieter Abbeel - Autograder Contributor

## Creation/Modification Dates
- Creation Date: 2023-01-15
- Modification Date: 2023-10-25

## Version
- Version: 1.0.0

## Dependency List
- search: >=1.0.0

## Public Interface Exports
- `EightPuzzleState`: Class representing an individual state of the Eight Puzzle.
- `EightPuzzleSearchProblem`: Class for modeling the Eight Puzzle as a search problem.
- `loadEightPuzzle(puzzleNumber)`: Function to load a pre-defined Eight Puzzle state.
- `createRandomEightPuzzle(moves=100)`: Function to create a random Eight Puzzle through a series of legal moves.

## Internal Implementation Details
This module defines two principal classes: `EightPuzzleState`, which encapsulates the state and behavior of the Eight Puzzle, and `EightPuzzleSearchProblem`, which integrates state management with search algorithms. The Eight Puzzle operates on a basic state mechanism where actions are defined as moving the blank space in the grid, with the goal of reaching a correct configuration. 

## Constant Definitions
- `EIGHT_PUZZLE_DATA`: A list of predefined puzzle configurations.

## Class/Function Relationships
- `EightPuzzleState`: Manages the puzzle state, including its representation and the legal moves possible.
- `EightPuzzleSearchProblem`: Extends `search.SearchProblem` to implement required methods for state evaluation and successor generation.
- `loadEightPuzzle`: Utilizes `EIGHT_PUZZLE_DATA` to instantiate `EightPuzzleState` objects from predefined configurations.
- `createRandomEightPuzzle`: Generates an `EightPuzzleState` object and applies random legal moves based on initial solved puzzle. 

## Revision History
| Date Modified | Version Delta | Change Description                       | Author Initials |
|---------------|---------------|-----------------------------------------|------------------|
| 2023-01-15    | 1.0.0        | Initial creation of Eight Puzzle module | JD, DK           |
| 2023-10-25    | 1.0.1        | Code refactoring and comments added    | JD               |

## Docstrings Following PEP 257

### `EightPuzzleState.__init__`
```python
def __init__(self, numbers):
    """
    Constructs a new eight puzzle from an ordering of numbers.

    Parameters:
    numbers: list[int]
        A list of integers from 0 to 8 representing an instance of
        the eight puzzle, where 0 indicates the blank space.

    Returns:
    None

    Examples:
    >>> EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8])
    >>>
       -------------
       | 1 |   | 2 |
       -------------
       | 3 | 4 | 5 |
       -------------
       | 6 | 7 | 8 |
       -------------
    """
```

### `EightPuzzleState.isGoal`
```python
def isGoal(self):
    """
    Checks to see if the puzzle is in its goal state.

    Parameters:
    None

    Returns:
    bool
        True if the current state is the goal state, False otherwise.

    Examples:
    >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).isGoal()
    True
    >>> EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).isGoal()
    False
    """
```

### `EightPuzzleState.legalMoves`
```python
def legalMoves(self):
    """
    Returns a list of legal moves from the current state.

    Moves are encoded as strings: 'up', 'down', 'left', and 'right'.

    Parameters:
    None

    Returns:
    list[str]
        A list of legal moves available from the current state.

    Examples:
    >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).legalMoves()
    ['down', 'right']
    """
```

### `EightPuzzleState.result`
```python
def result(self, move):
    """
    Returns a new eightPuzzle updated based on the provided move.

    The method does not alter the current object's state.

    Parameters:
    move: str
        A valid move string as returned from legalMoves.

    Returns:
    EightPuzzleState
        A new instance of EightPuzzleState reflecting the result of the move.

    Raises:
    Exception
        If the move is illegal.

    Examples:
    >>> state = EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8])
    >>> new_state = state.result('left')
    >>> new_state == EightPuzzleState([1, 2, 0, 3, 4, 5, 6, 7, 8])
    True
    """
```

### `EightPuzzleSearchProblem.__init__`
```python
def __init__(self, puzzle):
    """
    Initializes a new EightPuzzleSearchProblem.

    Parameters:
    puzzle: EightPuzzleState
        An instance of EightPuzzleState representing the initial state.

    Returns:
    None
    """
```

### `EightPuzzleSearchProblem.getStartState`
```python
def getStartState(self):
    """
    Returns the starting state of the search problem.

    Parameters:
    None

    Returns:
    EightPuzzleState
        The initial state of the Eight Puzzle.
    """
```

### `EightPuzzleSearchProblem.isGoalState`
```python
def isGoalState(self, state):
    """
    Checks if the given state is a goal state.

    Parameters:
    state: EightPuzzleState
        The state to be checked for its goal condition.

    Returns:
    bool
        True if the state is a goal state, False otherwise.
    """
```

### `EightPuzzleSearchProblem.getSuccessors`
```python
def getSuccessors(self, state):
    """
    Generates successors of the given state.

    Parameters:
    state: EightPuzzleState
        The current state from which successors are derived.

    Returns:
    list[tuple]
        A list of tuples containing the successor state, action taken,
        and step cost.

    Examples:
    >>> problem = EightPuzzleSearchProblem(EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]))
    >>> problem.getSuccessors(EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]))
    [(...), (...)] # Examples of the resulting successor states.
    """
```

### `EightPuzzleSearchProblem.getCostOfActions`
```python
def getCostOfActions(self, actions):
    """
    Computes the total cost of a given sequence of actions.

    Parameters:
    actions: list[str]
        A list of actions representing the moves taken.

    Returns:
    int
        The total cost associated with the sequence of actions.

    Examples:
    >>> problem.getCostOfActions(['up', 'down'])
    2
    """
```