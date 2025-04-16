# Pacman Agents

## Module Purpose
This module implements agents for the Pacman game, including a `LeftTurnAgent` that turns left at every opportunity and a `GreedyAgent` that selects actions based on a scoring evaluation function. It integrates with the underlying game infrastructure and provides functionality to evaluate and make decisions in a game state.

## Author List
- John DeNero - Lead Developer
- Dan Klein - Core Contributor
- Brad Miller - Student Side Autograding
- Nick Hay - Student Side Autograding
- Pieter Abbeel - Student Side Autograding

## Creation/Modification Dates
- Creation Date: 2023-01-01
- Last Modified Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- pacman >= 1.0.0
- game >= 1.0.0
- util >= 1.0.0
- random >= 1.0.0

## Public Interface Exports
- `LeftTurnAgent`: An agent that takes left turns whenever possible.
- `GreedyAgent`: An agent that selects actions based on a scoring mechanism.
- `scoreEvaluation`: A function that scores the game state based on the current score.

## Internal Implementation Details
- The `LeftTurnAgent` relies on direction constants defined in the `Directions` module to dictate movement behavior.
- The `GreedyAgent` makes use of an evaluation function to assess the desirability of potential successor states in the game.
- The `scoreEvaluation` function provides a basic scoring measure by returning the current score from the game state.

## Constant Definitions
- Direction constants from `Directions`: `NORTH`, `SOUTH`, `EAST`, `WEST`, `STOP`, `LEFT`, `RIGHT`.

## Class/Function Relationships
- `LeftTurnAgent`: Inherits from `game.Agent`.
- `GreedyAgent`: Inherits from `game.Agent` and employs an evaluation function for decision making.
- `scoreEvaluation`: Used by the `GreedyAgent` for evaluating game states.

### Class Definitions

#### `LeftTurnAgent`
- **Description**: An agent that turns left at every opportunity.
  
##### Methods
- `getAction(state)`: 
  - **Overview**: Determines the next action based on the current direction and allowed movements.
  - **Parameters**:
    - `state`: The current game state (instance of `GameState`).
  - **Returns**: A direction constant indicating the next action.
  - **Usage Example**: 
    ```python
    agent = LeftTurnAgent()
    next_action = agent.getAction(current_state)
    ```
  - **Exceptions**: Returns `STOP` if no movements are available.

#### `GreedyAgent`
- **Description**: An agent that selects actions based on the highest score from potential successor states.
  
##### Methods
- `getAction(state)`:
  - **Overview**: Chooses the best action based on successor state evaluation.
  - **Parameters**:
    - `state`: The current game state (instance of `GameState`).
  - **Returns**: A direction constant indicating the optimal action.
  - **Usage Example**: 
    ```python
    agent = GreedyAgent()
    next_action = agent.getAction(current_state)
    ```
  - **Exceptions**: Raises an error if no legal actions are available.

### Function Definitions

#### `scoreEvaluation(state)`
- **Description**: Evaluates the current game state by returning the score.
  
##### Parameters
- `state`: The current game state (instance of `GameState`).

##### Returns
- An integer representing the score of the game state.

##### Usage Example
```python
score = scoreEvaluation(current_state)
```
  
##### Exceptions
- None.

## Revision History
| Date Modified | Version Delta | Change Description                   | Author Initials |
|---------------|---------------|--------------------------------------|------------------|
| 2023-01-01    | 1.0.0        | Initial creation of the module      | JD               |
| 2023-10-01    | 1.0.1        | Refined agent logic, added comments | DK               |