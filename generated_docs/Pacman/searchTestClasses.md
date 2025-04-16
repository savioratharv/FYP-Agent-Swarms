# Pacman Search Test Classes

## Module Purpose
This module provides a framework for testing various search algorithms and heuristics 
within the context of the Pacman game. It defines different test cases for assessing the 
performance of search algorithms on specified graph layouts, ensuring they adhere to 
desired parameters and solution characteristics. The module also includes utilities for 
evaluation and grading based on problem specifications.

## Author List
- John DeNero (Lead Developer)
- Dan Klein (Algorithm Expert)
- Brad Miller (Testing & Grading)
- Nick Hay (Documentation & Maintenance)
- Pieter Abbeel (Integration Specialist)

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- Python 3.8+
- `layout` >= 1.0
- `pacman` >= 1.0
- `search` >= 1.0
- `textwrap` >= 1.0
- `re` >= 1.0

## Public Interface Exports
- `GraphSearch`: Class representing a search problem on a graph.
- `GraphSearchTest`: Class for testing graph search implementations.
- `PacmanSearchTest`: Class for testing Pacman search algorithms.
- `CornerProblemTest`: Class for testing the corner problem in Pacman.
- `HeuristicTest`: Class for testing heuristic functions.
- `ClosestDotTest`: Class for finding the closest dot in Pacman.
- `CornerHeuristicSanity`: Test case for checking corner heuristic properties.
- `CornerHeuristicPacman`: Test case for evaluating corner heuristic performance.

## Internal Implementation Details
The module contains several classes that handle different aspects of search 
algorithm testing. It imports required modules for layout and search problem 
definitions. Helper functions support core functionalities including solution 
validation, action following, path generation, and cost calculation.

### Class/Function Relationships
- `GraphSearch`: Uses methods from the `SearchProblem` to define search problems and methods to evaluate search outcomes.
- `GraphSearchTest`: Interacts with `GraphSearch` and encapsulates the logic for validating search outcomes against expected results.
- `PacmanSearchTest`: Works with `Pacman` game states and integrates with testing heuristics.
- `CornerProblemTest`: Implements searching for corners via the `CornersProblem` definition.
- Utility functions such as `followAction`, `checkSolution`, and `wrap_solution` assist in validating search results and wrapping solutions for output.

## Constant Definitions
- None defined explicitly in this module.

## Function Documentation

### `wrap_solution(solution)`
Wraps the provided solution in a string format suitable for display.

#### Parameters
- `solution`: A list or string that represents the solution to be wrapped.

#### Returns
- A formatted string of the solution.

### `followAction(state, action, problem)`
Follows a given action from a specified state within the problem context.

#### Parameters
- `state`: The current state in the search problem.
- `action`: The action to be taken from the current state.
- `problem`: The search problem instance.

#### Returns
- The resulting state after the action is applied, or `None` if invalid.

### `followPath(path, problem)`
Generates a list of states visited along a specified path within a problem.

#### Parameters
- `path`: A list of actions taken.
- `problem`: The search problem instance.

#### Returns
- A list of states visited.

### `checkSolution(problem, path)`
Validates whether the proposed path is a solution to the given problem.

#### Parameters
- `problem`: The search problem instance.
- `path`: A list of actions constituting a proposed solution.

#### Returns
- A boolean indicating whether the path is a valid solution.

## Revision History

| Date Modified | Version Delta | Change Description                 | Author Initials |
|---------------|---------------|-------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of the module.    | JD                |
| 2023-10-01    | 1.0.0        | Refactored tests for search algorithms. | DK                |
| 2023-10-01    | 1.0.0        | Added detailed docstrings and comments. | BM                |