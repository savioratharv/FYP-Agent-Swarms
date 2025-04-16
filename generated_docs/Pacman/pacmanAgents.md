# Pacman Agents

## Module Purpose
This module implements the behavior of autonomous agents in the Pacman game. 
The agents defined in this module include `LeftTurnAgent`, which turns left at every opportunity and `GreedyAgent`, which utilizes a scoring evaluation function to determine the best action based on the current game state. The module interfaces with the Pacman engine to retrieve legal actions and the game state.

## Author List
- John DeNero: Lead Developer
- Dan Klein: Senior Developer
- Brad Miller: Autograding Specialist
- Nick Hay: Software Engineer
- Pieter Abbeel: AI Researcher

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- pacman >= 1.0.0
- game >= 1.0.0
- util >= 1.0.0

## Public Interface Exports
- `LeftTurnAgent`: An agent that turns left at every opportunity.
- `GreedyAgent`: An agent that selects actions based on a scoring evaluation function.
- `scoreEvaluation(state)`: Evaluates the game state score.

## Internal Implementation Details
- **Classes**:
  - `LeftTurnAgent`: Implements behavior for left-turning agent.
  - `GreedyAgent`: Selects the best action based on evaluated scores.

- **Functions**:
  - `getAction(state)`: Determines the next action based on game state.
  - `scoreEvaluation(state)`: Returns the score of the passed game state.

## Constant Definitions
- `Directions`: A predefined set of possible actions (NORTH, SOUTH, EAST, WEST, STOP).
- `game.Agent`: Base class for agents in the game.

## Class/Function Relationships
- `LeftTurnAgent` derives from `game.Agent`.
- `GreedyAgent` derives from `game.Agent`.
- Both agents implement the `getAction` method for decision-making.
- `scoreEvaluation` function is utilized by `GreedyAgent` for evaluating the state score.

## Revision History
| Date Modified | Version Delta | Change Description                       | Author Initials |
|---------------|---------------|-----------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of Pacman agents file | JD, DK, BM, NH, PA|

## Functionality Overview
### `getAction(self, state)`
Determines the next action for the given state based on the agent's logic.

#### Parameters
| Parameter | Type   | Description                             |
|-----------|--------|-----------------------------------------|
| state     | State  | The current game state.                 |

#### Returns
| Return Value | Type       | Description                             |
|--------------|------------|-----------------------------------------|
| action       | Direction  | The chosen action for the agent.        |

#### Usage Examples
- Typical usage: `action = agent.getAction(current_state)`
- Edge case: When no legal actions are available, it will return `STOP`.

### `scoreEvaluation(state)`
Evaluates the current game state score.

#### Parameters
| Parameter | Type   | Description                             |
|-----------|--------|-----------------------------------------|
| state     | State  | The current game state.                 |

#### Returns
| Return Value | Type       | Description                             |
|--------------|------------|-----------------------------------------|
| score        | int        | The score of the current game state.    |

#### Usage Examples
- Typical usage: `score = scoreEvaluation(current_state)`
- Edge case: The score is consistently evaluated without game events affecting it. 

### Exception Hierarchy Documentation
- `ValueError`: Raised if the action requested is invalid.
- `IndexError`: Raised if an attempt is made to access an illegal action.