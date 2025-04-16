# Pacman Game Documentation

## Project Name
Pacman

## Module Purpose
The Pacman module encapsulates the logic for the classic Pacman game along with functionalities to manage the game state, actions, and rules governing the interactions between Pacman and ghosts. It serves as a foundation for implementing various agent behaviors and provides a framework for running the game through a command line interface.

## Author List
- John DeNero (Lead Developer)
- Dan Klein (Co-Developer)
- Brad Miller (Student Side Autograder)
- Nick Hay (Student Side Autograder)
- Pieter Abbeel (Student Side Autograder)

## Creation/Modification Dates
- Creation Date: 2023-10-02
- Last Modified Date: 2023-10-02

## Version
1.0.0

## Dependency List
- Python >= 3.8
- util
- game
- layout

## Public Interface Exports
- GameState: Class managing the game state and actions.
- ClassicGameRules: Class managing the game rules and flow.
- PacmanRules: Class governing Pacman's actions and interactions.
- GhostRules: Class dictating ghost behavior and interactions.

## Internal Implementation Details
The Pacman module comprises several classes, each responsible for a specific aspect of the game:
- `GameState`: Represents the full game state, encapsulating information about food, capsules, and agent configurations.
- `ClassicGameRules`: Controls the rule mechanics of the game, managing the start and end conditions.
- `PacmanRules` and `GhostRules`: Contain methods for legal actions, state updates, and interactions specific to Pacman and ghosts.

## Constant Definitions
- `SCARED_TIME`: The duration ghosts remain scared after consuming a power capsule (40 moves).
- `COLLISION_TOLERANCE`: The maximum distance at which a ghost can collide with Pacman (0.7 units).
- `TIME_PENALTY`: Points deducted for not making a move (1 point).

## Class/Function Relationships
- `GameState`: Utilizes `GameStateData` for storing the game data, includes methods to access and manipulate agent states.
- `ClassicGameRules`: Interfaces with `PacmanRules` and `GhostRules` to apply specific rules during gameplay.
- `PacmanRules`: Requires functions from `Actions`, `nearestPoint`, and `manhattanDistance` to manage movement and interactions.
- `GhostRules`: Similar to `PacmanRules`, relies on external functions to dictate ghost behavior.

## Revision History
| Date Modified | Version Delta | Change Description                                      | Author Initials |
|---------------|---------------|--------------------------------------------------------|------------------|
| 2023-10-02    | 1.0.0        | Initial creation of the Pacman game module.           | JD, DK            |
|               |               |                                                        |                  |

## Class and Function Documentation

### GameState
Represents the full state of the game. Handles food, capsules, ghost states, and scoring.

#### Methods
- `getLegalActions(agentIndex=0)`: Returns the legal actions available to the specified agent.
- `generateSuccessor(agentIndex, action)`: Generates a successor game state after the specified agent takes the action.
- `getNumAgents()`: Returns the total number of agents in the game.

### ClassicGameRules
Manages the rules and flow of the game.

#### Methods
- `newGame(layout, pacmanAgent, ghostAgents, display, quiet=False, catchExceptions=False)`: Initializes a new game state.
- `process(state, game)`: Checks if the game has been won or lost and processes the outcome.

### PacmanRules
Governs Pacman's interactions and movements within the game.

#### Methods
- `getLegalActions(state)`: Returns a list of possible actions for Pacman.
- `applyAction(state, action)`: Updates the game state based on the action taken by Pacman.
- `consume(position, state)`: Modifies the state by removing food or capsules when consumed.

### GhostRules
Dictates the behavior and interactions of ghosts in the game.

#### Methods
- `getLegalActions(state, ghostIndex)`: Returns the legal actions available to the specified ghost.
- `applyAction(state, action, ghostIndex)`: Updates the state based on the ghost's action.
- `checkDeath(state, agentIndex)`: Checks if Pacman has been killed by a ghost.

## Exception Hierarchy Documentation
- `Exception`: Base class for exceptions raised in the module.
- `Illegal action Exception`: Raised when an illegal action is attempted by an agent.
- `Invalid index Exception`: Raised when an invalid index is passed to a ghost state query. 

This documentation provides an overview and detailed reference for the Pacman module, including its design, functionalities, and usage.