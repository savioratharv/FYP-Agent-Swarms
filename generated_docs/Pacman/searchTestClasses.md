# Function Documentation for `searchTestClasses.py`

## `wrap_solution(solution)`
This helper function formats a solution into a human-readable string. It checks if the input `solution` is a list and joins the elements with spaces, wrapping the result to ensure it doesn't exceed certain line lengths. If the solution is not a list, it converts it to a string and returns it.

### Parameters
- `solution`: A list of actions or a single action to be formatted.

### Returns
- A string representing the wrapped solution.

---

## `followAction(state, action, problem)`
This function determines the successor state given a current `state` and an `action` to perform within a specified `problem`. It retrieves successors from the problem and checks if the action matches any of the successors.

### Parameters
- `state`: The current state in the search problem.
- `action`: The action to be executed from the current state.
- `problem`: An instance of `SearchProblem` from which to get successors.

### Returns
- The successor state if the action is valid; otherwise, `None`.

---

## `followPath(path, problem)`
This function computes the sequence of states resulting from following a specified `path` starting from the initial state of a given `problem`. It uses `followAction` to determine each subsequent state.

### Parameters
- `path`: A list of actions to follow.
- `problem`: An instance of `SearchProblem`.

### Returns
- A list of states visited while following the path.

---

## `checkSolution(problem, path)`
This function checks if a given `path` leads to a goal state in a specified `problem`. It iteratively executes the actions in the provided path and checks the resulting state against the goal state.

### Parameters
- `problem`: An instance of `SearchProblem`.
- `path`: A list of actions to execute.

### Returns
- `True` if the path leads to a goal state; otherwise, `False`.

---

## `GraphSearch`
This class implements a search problem based on a graph representation. It initializes with a given graph specification and defines methods to manage states, goals, successors, and costs.

### Methods:
- **`__init__(self, graph_text)`**: Parses the graph definition from a text input and initializes start state, goal states, and successor relations.
- **`getStartState(self)`**: Returns the starting state of the graph.
- **`isGoalState(self, state)`**: Checks if the provided state is one of the goal states.
- **`getSuccessors(self, state)`**: Provides a list of successor states for a given state, recording the expanded states.
- **`getCostOfActions(self, actions)`**: Calculates the total cost of a sequence of actions.
- **`getExpandedStates(self)`**: Returns a list of states that have been expanded during the search.
- **`__str__(self)`**: Returns a string representation of the graph.

---

## `parseHeuristic(heuristicText)`
This function parses a heuristic definition from text input, creating a heuristic mapping for states. It returns a function that retrieves heuristic values for given states.

### Parameters
- `heuristicText`: A string representing the heuristic specification.

### Returns
- A function that takes a state and an optional problem instance and returns the corresponding heuristic value.

---

## `GraphSearchTest`
This class defines tests for a graph search algorithm. It manages the graph input, the search algorithm to use, and expected results for validating the search implementation.

### Methods:
- **`__init__(self, question, testDict)`**: Initializes the test with a graph description and settings.
- **`getSolInfo(self, search)`**: Retrieves the solution and expanded states from the search algorithm given the problem instance.
- **`execute(self, grades, moduleDict, solutionDict)`**: Runs the actual test against the provided solution and records the results.
- **`writeSolution(self, moduleDict, filePath)`**: Writes the found solutions back to a specified output file.

---

## `PacmanSearchTest`
This class extends `GraphSearchTest` to specifically manage search tests within a Pacman application, adapting the input formats for Pacman layouts and actions.

### Methods:
- **`__init__(self, question, testDict)`**: Initializes with layout information specific to Pacman.
- **`getSolInfo(self, search, searchAgents)`**: Similar to `GraphSearchTest`, but tailored for Pacman search problems, using Pacman-specific agents and states.
- **`execute(self, grades, moduleDict, solutionDict)`**: Executes the search and validates the found path against expected outputs based on the layout.
- **`writeSolution(self, moduleDict, filePath)`**: Writes the discovered solutions to a file in a Pacman context.

---

## `getStatesFromPath(start, path)`
This function converts a list of actions into the corresponding states visited, starting from a given position. It is particularly useful for tracking how paths translate into state transitions in the Pacman environment.

### Parameters
- `start`: The starting coordinate for the path.
- `path`: A list of actions to be followed.

### Returns
- A list of states visited according to the actions in the path.

---

## `CornerProblemTest`
This class tests the solution of the Corners Problem in the Pacman context. It checks the correctness of paths leading to all corners.

### Methods:
- **`solution(self, search, searchAgents)`**: Computes the path for solving the Corners Problem and determines if all corners are visited.
- **`execute(self, grades, moduleDict, solutionDict)`**: Validates the computed solution against the expected outcomes regarding corners.
- **`writeSolution(self, moduleDict, filePath)`**: Writes the solution length back to a output file.

---

## `HeuristicTest`
This class tests the validity of heuristics for search problems associated with Pacman, ensuring they adhere to heuristic properties.

### Methods:
- **`__init__(self, question, testDict)`**: Initializes with details about the heuristic to be tested.
- **`setupProblem(self, searchAgents)`**: Sets up the specific search problem with layout and heuristic.
- **`checkHeuristic(self, heuristic, problem, state, solutionCost)`**: Validates the heuristic against several conditions (non-negativity, admissibility, consistency).
- **`execute(self, grades, moduleDict, solutionDict)`**: Runs heuristic checks and reports on their validity.
- **`writeSolution(self, moduleDict, filePath)`**: Writes the result of heuristic evaluation to a specified output file.

---

## `HeuristicGrade`
This class evaluates heuristics based on specific grading criteria related to how well they perform in reducing node expansions.

### Methods:
- **`__init__(self, question, testDict)`**: Initializes the grading test with layout and thresholds.
- **`setupProblem(self, searchAgents)`**: Prepares the search problem for testing.
- **`execute(self, grades, moduleDict, solutionDict)`**: Executes the grading procedure, scoring based on performance of the heuristic.
- **`writeSolution(self, moduleDict, filePath)`**: Writes the grading solution file without content.

---

## `ClosestDotTest`
This class tests the functionality of a search function to find the closest dot in a Pacman layout.

### Methods:
- **`solution(self, searchAgents)`**: Computes the path to the closest dot.
- **`execute(self, grades, moduleDict, solutionDict)`**: Validates the solution length against expected results.
- **`writeSolution(self, moduleDict, filePath)`**: Writes the solution length to the designated file.

---

## `CornerHeuristicSanity`
This class performs sanity checks on corner heuristics to ensure they meet specified conditions, checking properties like admissibility.

### Methods:
- **`execute(self, grades, moduleDict, solutionDict)`**: Executes the checks and validates the heuristic measures.
- **`writeSolution(self, moduleDict, filePath)`**: Writes the cost and path related to the corner problem for further analysis.

---

## `CornerHeuristicPacman`
This class specializes in validating heuristics within the context of the Pacman Corners Problem, focusing on their effect on search efficiency.

### Methods:
- **`execute(self, grades, moduleDict, solutionDict)`**: Runs the heuristic validation checks, assessing costs and expanded nodes.
- **`writeSolution(self, moduleDict, filePath)`**: Writes the results of the heuristic evaluation to a solution file.