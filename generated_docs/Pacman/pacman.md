# Pacman.py Documentation

## Overview
`Pacman.py` contains the main game logic for the classic Pacman game, including the definition of the game state, rules, and framework to run the game. The code is structured into three main sections: game interface, hidden logic, and game framework.

## Classes

### GameState
The `GameState` class encapsulates the complete game state, including the position of Pacman, ghosts, food, capsules, and scores. It provides methods to access and manipulate game data.

#### Methods

- **getLegalActions(agentIndex=0)**: 
  - Returns the legal actions available for the specified agent (Pacman or a ghost). If the game is won or lost, it returns an empty list.

- **generateSuccessor(agentIndex, action)**: 
  - Returns the state that results from the specified agent taking the given action. It updates the state accordingly, handling agent movements and interactions in the game.

- **getPacmanState()**: 
  - Returns the current state of Pacman as an AgentState object.

- **getPacmanPosition()**: 
  - Returns Pacman's current position in the game.

- **getGhostStates()**: 
  - Returns a list of states for all ghosts in the game.

- **getGhostState(agentIndex)**: 
  - Returns the state of the ghost at the specified index.

- **getGhostPosition(agentIndex)**: 
  - Returns the position of the ghost at the specified index.

- **getNumAgents()**: 
  - Returns the total number of agents (Pacman and ghosts) in the game.

- **getScore()**: 
  - Returns the current score of the game.

- **getCapsules()**: 
  - Returns a list of the remaining capsules' positions.

- **getNumFood()**: 
  - Returns the number of remaining food items in the game.

- **getFood()**: 
  - Returns a grid representation of food locations.

- **getWalls()**: 
  - Returns a grid representation of wall locations.

- **isLose()**: 
  - Checks if the game is in a lost state.

- **isWin()**: 
  - Checks if the game is in a won state.

- **initialize(layout, numGhostAgents=1000)**: 
  - Initializes the game state based on the provided layout and number of ghost agents.

### ClassicGameRules
The `ClassicGameRules` class manages the control flow of the game, determining when the game starts and ends.

#### Methods

- **newGame(layout, pacmanAgent, ghostAgents, display, quiet=False, catchExceptions=False)**: 
  - Creates a new game instance with the specified layout, agents, and display settings.

- **process(state, game)**: 
  - Checks the game state to determine whether to end the game.

- **win(state, game)**: 
  - Handles the winning event and displays the win message.

- **lose(state, game)**: 
  - Handles the losing event and displays the loss message.

- **getProgress(game)**: 
  - Returns the progress of the game based on the remaining food.

### PacmanRules
The `PacmanRules` class defines how Pacman interacts with the game environment.

#### Methods

- **getLegalActions(state)**: 
  - Returns a list of actions that Pacman can legally take.

- **applyAction(state, action)**: 
  - Updates the game state based on Pacman's chosen action, handling movements and interactions such as consuming food.

- **consume(position, state)**: 
  - Updates the state when Pacman eats food or capsules.

### GhostRules
The `GhostRules` class defines how ghosts interact with the game environment.

#### Methods

- **getLegalActions(state, ghostIndex)**: 
  - Returns a list of legal actions available to a ghost.

- **applyAction(state, action, ghostIndex)**: 
  - Updates the game state based on the ghost's chosen action.

- **decrementTimer(ghostState)**: 
  - Decreases the scared timer for a ghost, affecting movement behavior.

- **checkDeath(state, agentIndex)**: 
  - Checks if Pacman has been caught by a ghost and handles the collision accordingly.

### Functions

#### readCommand(argv)
Processes command-line arguments for running the game and returns game components based on user input.

#### loadAgent(pacman, nographics)
Loads the appropriate Pacman or ghost agent based on the specified type.

#### replayGame(layout, actions, display)
Replays a recorded game using the provided layout and actions.

#### runGames(layout, pacman, ghosts, display, numGames, record, numTraining=0, catchExceptions=False, timeout=30)
Runs multiple games based on the specified parameters and records results.

## Constants
- **SCARED_TIME**: The duration for which ghosts are scared after consuming a capsule.
- **COLLISION_TOLERANCE**: Defines the proximity required for ghosts to collide with Pacman.
- **TIME_PENALTY**: Points deducted for each round that Pacman does not move.