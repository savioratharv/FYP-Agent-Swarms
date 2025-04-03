# Pacman Search.py Documentation

## Overview
This module implements generic search algorithms used by Pacman agents. The algorithms include Depth-First Search, Breadth-First Search, Uniform Cost Search, and A* Search. These algorithms navigate through a defined search space represented by a `SearchProblem` class which outlines the structure of potential search problems in the Pacman game.

## Class Definition

### SearchProblem
This abstract class defines the methods necessary for any search problem but does not implement any of them. It includes methods to retrieve the start state, check if a state is a goal, get successors of a state, and calculate the cost of a sequence of actions.

---

## Function Summaries

### tinyMazeSearch(problem)
Returns a predefined sequence of moves that solves the tinyMaze problem. This function should only be used for the specific tinyMaze and is not applicable for other mazes.

**Key Tasks:**
- Define specific moves (SOUTH and WEST) to navigate a static maze layout.

### depthFirstSearch(problem)
Implements the Depth-First Search (DFS) algorithm to explore the search space by traversing as deep as possible before backtracking.

**Key Tasks:**
- Utilize a `Stack` to manage the nodes to be explored.
- Track visited nodes to avoid cycles.
- Return the path of actions to reach the goal state.

### breadthFirstSearch(problem)
Implements the Breadth-First Search (BFS) algorithm to explore the shallowest nodes in the search tree first.

**Key Tasks:**
- Use a `Queue` to explore nodes level by level.
- Maintain a list of visited nodes to prevent revisiting them.
- Return the path of actions leading to the goal state.

### uniformCostSearch(problem)
Implements the Uniform Cost Search algorithm which prioritizes nodes based on the cumulative cost to reach them.

**Key Tasks:**
- Utilize a `PriorityQueue` to efficiently explore the least costly paths first.
- Maintain a list of visited nodes and update priorities as needed.
- Return the path leading to the goal state based on the least cost.

### nullHeuristic(state, problem=None)
Provides a trivial heuristic for search algorithms. Returns a value of zero, indicating no estimated cost from the current state to the nearest goal.

**Key Tasks:**
- Serve as a placeholder for scenarios where no heuristic is provided.

### aStarSearch(problem, heuristic=nullHeuristic)
Implements the A* Search algorithm that combines the lowest cost from the start state and an estimated cost to the goal.

**Key Tasks:**
- Utilize a `PriorityQueue` to explore nodes based on their combined cost (g(n) + h(n)).
- Track visited nodes and make use of heuristics to optimize the search process.
- Return the path of actions that leads to the goal state.

---

## Abbreviations
- `bfs`: Alias for `breadthFirstSearch`
- `dfs`: Alias for `depthFirstSearch`
- `astar`: Alias for `aStarSearch`
- `ucs`: Alias for `uniformCostSearch`