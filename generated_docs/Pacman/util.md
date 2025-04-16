# Pacman Utility Module

## Module Purpose
The `util.py` module provides various utility classes and functions for implementing search agents and supporting other functionalities. It includes data structures like stacks, queues, and priority queues, and various utility functions for handling numerical operations, distributions, and more. These components aid in developing AI applications, specifically within the context of the Pacman AI project.

## Author List
- John DeNero: Primary Developer
- Dan Klein: Co-Developer
- Brad Miller: Autograding Contributor
- Nick Hay: Autograding Contributor
- Pieter Abbeel: Autograding Contributor

## Creation/Modification Dates
- Creation Date: 2022-08-15
- Last Modified Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependencies
- Python 3.7 or higher
- NumPy 1.19.0 or higher (if used in advanced applications)

## Public Interface Exports
- Classes:
  - `Stack`: A last-in-first-out (LIFO) container.
  - `Queue`: A first-in-first-out (FIFO) container.
  - `PriorityQueue`: A priority queue data structure.
  - `PriorityQueueWithFunction`: A priority queue that uses a custom priority function.
  - `FixedRandom`: A fixed random number generator.
  - `Counter`: A specialized dictionary for counting keys.
- Functions:
  - `manhattanDistance`: Computes the Manhattan distance between two points.
  - `normalize`: Normalizes a vector or counter.
  - `nSample`: Samples multiple values from a given distribution.
  - `sample`: Samples a single value from a given distribution.
  - `flipCoin`: Simulates a coin flip with a given probability.
  - `getProbability`: Calculates the probability of a value under a discrete distribution.
  - `pause`: Pauses output stream for user interaction.

## Internal Implementation Details
The module uses standard Python data structures but extends them to include specific functionalities related to search algorithms. It defines custom structures for counting, random number generation, and priority handling. It also implements utility functions to provide commonly used operations like normalization and sampling.

## Constant Definitions
- Fixed random state data is embedded within the `FixedRandom` class to achieve deterministic results during testing.

## Class/Function Relationships
- The `Stack` and `Queue` classes provide basic data structures.
- The `PriorityQueue` class is enhanced by `PriorityQueueWithFunction`, which allows for priority-based insertion using a custom function.
- The `Counter` class extends dictionary functionality with additional counting methods.
- Utility functions interact with these classes to provide operations such as sampling and distance calculation.

## Docstrings

### `class Stack`
A container following the last-in-first-out (LIFO) policy.

#### Methods:
- `push(item)`: Adds an item to the top of the stack.
- `pop()`: Removes and returns the most recently added item.
- `isEmpty()`: Checks if the stack is empty.

### `class Queue`
A container following the first-in-first-out (FIFO) policy.

#### Methods:
- `push(item)`: Adds an item to the back of the queue.
- `pop()`: Removes and returns the earliest added item.
- `isEmpty()`: Checks if the queue is empty.

### `class PriorityQueue`
A priority queue supporting O(1) access to the lowest-priority item.

#### Methods:
- `push(item, priority)`: Adds an item with a given priority.
- `pop()`: Removes and returns the item with the lowest priority.
- `isEmpty()`: Checks if the priority queue is empty.
- `update(item, priority)`: Updates priority for an existing item or adds it if new.

### `class PriorityQueueWithFunction`
A priority queue that utilizes a custom priority function.

#### Methods:
- `push(item)`: Adds an item using the priority defined by the priority function.

### `class FixedRandom`
Represents a fixed random number generator.

#### Methods:
- `__init__()`: Initializes with a fixed random state.

### Global Functions

#### `manhattanDistance(xy1, xy2)`
Calculates the Manhattan distance between two points.

| Parameter  | Type    | Description                           |
|------------|---------|---------------------------------------|
| xy1        | tuple   | First point (x1, y1)                 |
| xy2        | tuple   | Second point (x2, y2)                |

| Returns    | Type    | Description                           |
|------------|---------|---------------------------------------|
|            | int     | Manhattan distance                    |

##### Usage Example:
```python
distance = manhattanDistance((1, 2), (4, 6))  # returns 7
```

#### `normalize(vectorOrCounter)`
Normalizes a vector or counter by dividing each value by the total sum.

| Parameter           | Type        | Description                            |
|---------------------|-------------|----------------------------------------|
| vectorOrCounter     | Counter or list | Vector or Counter to normalize          |

| Returns    | Type    | Description                           |
|------------|---------|---------------------------------------|
|            | Counter or list | Normalized vector or counter          |

##### Edge Case:
An empty counter will return the counter unchanged.

#### `nSample(distribution, values, n)`
Samples multiple values from a given distribution.

| Parameter           | Type    | Description                            |
|---------------------|---------|----------------------------------------|
| distribution        | list    | List of probabilities                  |
| values              | list    | List of values corresponding to distribution |
| n                   | int     | Number of samples to generate          |

| Returns    | Type    | Description                           |
|------------|---------|---------------------------------------|
|            | list    | List of sampled values                |

##### Usage Example:
```python
samples = nSample([0.2, 0.3, 0.5], ['a', 'b', 'c'], 10)
```

### Revision History
| Date Modified | Version Delta | Change Description                                 | Author Initials |
|---------------|---------------|----------------------------------------------------|------------------|
| 2022-08-15    | 1.0.0        | Initial creation                                   | JD                |
| 2023-10-01    | 1.0.1        | Minor refactor and added docstrings                | DK                |