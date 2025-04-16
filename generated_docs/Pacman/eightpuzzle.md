# Eight Puzzle Project

## Module Purpose
The Eight Puzzle module implements the mechanics of the classic 8-puzzle game, which involves sliding pieces on a 3x3 grid to achieve a specified goal state. This module also provides a framework for searching through the state space of puzzle configurations to determine a sequence of moves to reach the goal state.

## Author List
- John DeNero: Lead Developer
- Dan Klein: Contributor
- Brad Miller: Contributor
- Nick Hay: Contributor
- Pieter Abbeel: Contributor

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependencies
- numpy >= 1.18.0
- random >= 2.0

## Public Interface Exports
- `loadEightPuzzle(puzzleNumber)`: Generates and returns an EightPuzzleState instance.
- `createRandomEightPuzzle(moves)`: Creates a random puzzle by applying a series of random moves.

## Internal Implementation Details
- The eight-puzzle mechanics are encapsulated in the `EightPuzzleState` class.
- A search problem framework is provided by the `EightPuzzleSearchProblem` class.
- Legal moves include sliding the blank space up, down, left, or right.

## Constant Definitions
- `EIGHT_PUZZLE_DATA`: Contains predefined configurations for the eight puzzle.

## Class/Function Relationships
1. `EightPuzzleState`: Represents an instance of the eight puzzle.
   - Methods: 
     - `isGoal()`: Checks if the current state is the goal state.
     - `legalMoves()`: Returns a list of legal moves from the current state.
     - `result(move)`: Returns a new state based on the provided move.
2. `EightPuzzleSearchProblem`: Defines a search problem for the eight puzzle domain.
   - Methods:
     - `getStartState()`: Returns the initial puzzle state.
     - `isGoalState(state)`: Checks if the provided state is the goal state.
     - `getSuccessors(state)`: Retrieves successors for the given state.
     - `getCostOfActions(actions)`: Calculates the total cost for a sequence of actions.

## Revision History Table

| Date Modified | Version Delta | Change Description                            | Author Initials |
|---------------|---------------|----------------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of the Eight Puzzle module. | JD, DK, BM, NH, PA |