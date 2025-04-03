# pacmanAgents.py Documentation

## Classes

### LeftTurnAgent
An agent that prioritizes turning left at every opportunity.

#### Methods

- **getAction(state)**: 
  - **Parameters**: 
    - `state`: The current game state.
  - **Returns**: A direction for Pacman to move, based on available legal actions and the left-turning strategy.
  - **Description**: 
    This method retrieves all legal actions for Pacman, determines the current direction of Pacman, and calculates the leftward direction. If turning left is allowed, it returns that action. If not, it checks for the current direction or a right turn, and defaults to stopping if no movement is possible.

---

### GreedyAgent
An agent that chooses actions based on maximizing a predefined evaluation function.

#### Methods

- **__init__(evalFn="scoreEvaluation")**: 
  - **Parameters**: 
    - `evalFn`: A string representing the name of the evaluation function to use (default is "scoreEvaluation").
  - **Description**: 
    Initializes the GreedyAgent and sets the evaluation function by looking it up in the global context.

- **getAction(state)**: 
  - **Parameters**: 
    - `state`: The current game state.
  - **Returns**: A direction for Pacman to move, selected from the best available actions.
  - **Description**: 
    This method generates candidate actions from the current state and evaluates the potential successors using the evaluation function. It identifies the best possible action(s) based on the maximum score and randomly selects one from among the best actions to execute.

---

## Functions

### scoreEvaluation(state)
- **Parameters**: 
  - `state`: The current game state.
- **Returns**: An integer that represents the score of the game state.
- **Description**: 
  This function serves to evaluate the current score of the game state, facilitating the decision-making process of agents that utilize this evaluation. It is primarily used by the GreedyAgent to assess the quality of actions.