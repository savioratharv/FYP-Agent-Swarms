# Ghost Agents in Pacman

## Overview

This file defines classes and behaviors for ghost agents in a Pacman game. The primary functionality revolves around determining actions for ghosts based on the game state. The main classes are `GhostAgent`, `RandomGhost`, and `DirectionalGhost`, each implementing specific strategies for ghost movement.

### Classes

#### `GhostAgent`

- **Purpose**: An abstract class serving as the base for all ghost agents. It handles the action selection process based on the game state.
  
- **Methods**:
  - `__init__(self, index)`: Initializes the ghost agent with a unique index.
  - `getAction(self, state)`: Determines the action to take based on a probability distribution of actions derived from the game state.
    - **Parameters**: 
      - `state`: The current state of the game, containing information about legal actions and positions.
    - **Returns**: An action direction or `Directions.STOP` if there are no legal actions.
  - `getDistribution(self, state)`: An abstract method intended to return a probability distribution over possible actions. Must be implemented by subclasses.

#### `RandomGhost`

- **Purpose**: A subclass of `GhostAgent` that chooses a legal action randomly with equal probability among all available actions.
  
- **Methods**:
  - `getDistribution(self, state)`: Returns a uniform distribution over legal actions.
    - **Parameters**: 
      - `state`: The current state of the game.
    - **Returns**: A `util.Counter` representing the probability distribution of actions.

#### `DirectionalGhost`

- **Purpose**: A subclass of `GhostAgent` that chooses actions based on the proximity to Pacman and whether the ghost is scared.
  
- **Attributes**:
  - `prob_attack`: Probability of attacking Pacman when not scared.
  - `prob_scaredFlee`: Probability of fleeing from Pacman when scared.

- **Methods**:
  - `__init__(self, index, prob_attack=0.8, prob_scaredFlee=0.8)`: Initializes the ghost with the specified attack and flee probabilities.
  - `getDistribution(self, state)`: Computes a biased distribution favoring attacks when not scared and retreats when scared.
    - **Parameters**: 
      - `state`: The current state of the game.
    - **Returns**: A `util.Counter` representing the calculated action distribution based on distance to Pacman.

### Dependencies

- **Functions**:
  - `manhattanDistance(xy1, xy2)`: This function calculates the Manhattan distance between two points, playing a crucial role in determining the best actions for the ghost agents regarding their positions relative to Pacman.

### Usage in Project

Ghost agents utilize the decision-making framework defined in this file within the broader context of the Pacman game, affecting both gameplay and strategies employed by players seeking to evade or chase down Pacman. Each ghost type behaves according to its strategy, enriching the game's complexity and enhancing player experience.