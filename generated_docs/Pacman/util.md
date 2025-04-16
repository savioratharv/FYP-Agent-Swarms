# Pacman Util Module

## Module Purpose
This module provides utility classes and functions for implementing 
search agents in the Pacman AI projects. It includes data structures 
like stacks, queues, and priority queues, which facilitate various 
search algorithms, as well as mathematical utilities such as distances 
and probability functions. The implementation emphasizes efficiency 
and extensibility for educational purposes.

## Authors
- John DeNero (Lead Developer)
- Dan Klein (Developer)
- Brad Miller (Autograder Contributor)
- Nick Hay (Autograder Contributor)
- Pieter Abbeel (Autograder Contributor)

## Creation/Modification Dates
- Creation Date: 2023-01-01
- Last Modification Date: 2023-10-20

## Version
- Version: 1.0.0

## Dependencies
- Python 3.6 or higher

## Public Interface Exports
- `Stack`: A LIFO data structure.
- `Queue`: A FIFO data structure.
- `PriorityQueue`: A priority queue implementation.
- `PriorityQueueWithFunction`: A priority queue that uses a custom 
  priority function.
- `Counter`: A specialized dictionary for counting hashable items.
- Mathematical utility functions:
  - `manhattanDistance(xy1, xy2)`
  - `normalize(vectorOrCounter)`
  - `flipCoin(p)`
  - `sample(distribution, values=None)`
  - `nSample(distribution, values, n)`
  
## Internal Implementation Details
The internal workings of the module use Python's built-in data structures 
and external libraries to enhance functionality. Efficiency is achieved 
through careful implementation of data structures. The fixed random number 
generator ensures reproducibility during experiments.

## Constant Definitions
- No constant definitions present in this module.

## Class/Function Relationships
- `Stack`, `Queue`, and `PriorityQueue` are independent data structures.
- `Counter` extends the dictionary class to provide counting functionality.
- Utility functions like `manhattanDistance` and `normalize` interact 
  with classes for various computational tasks.

## Class and Function Documentation

### Stack
- **Overview**: A container that implements a last-in-first-out (LIFO) 
  queuing policy.
- **Methods**:
  - `push(item)`: Add an item to the stack.
  - `pop()`: Remove and return the most recently added item.
  - `isEmpty()`: Check if the stack is empty.

### Queue
- **Overview**: A container that implements a first-in-first-out (FIFO) 
  queuing policy.
- **Methods**:
  - `push(item)`: Add an item to the queue.
  - `pop()`: Remove and return the earliest added item.
  - `isEmpty()`: Check if the queue is empty.

### PriorityQueue
- **Overview**: Implements a priority queue where items are stored in a way that 
  allows for quick retrieval of the lowest-priority item.
- **Methods**:
  - `push(item, priority)`: Add an item with its priority.
  - `pop()`: Remove and return the lowest-priority item.
  - `isEmpty()`: Check if the priority queue is empty.
  - `update(item, priority)`: Update the priority of an existing item or add it if 
    it’s not present.

### PriorityQueueWithFunction
- **Overview**: A priority queue that requires a priority function to determine 
  the order of items.
- **Methods**:
  - `push(item)`: Add an item with priority based on the provided function.

### Counter
- **Overview**: An extension of the dictionary for counting hashable items.
- **Methods**:
  - `incrementAll(keys, count)`: Increment the count for specified keys.
  - `argMax()`: Return the key with the highest count.
  - `normalized()`: Normalize the counts to sum to 1.

### Utility Functions
- **manhattanDistance(xy1, xy2)**
  - **Overview**: Calculate and return the Manhattan distance between two points.
  - **Parameters**: 
    - `xy1`: First point as a tuple (x, y).
    - `xy2`: Second point as a tuple (x, y).
  - **Returns**: Integer distance.
  
- **normalize(vectorOrCounter)**
  - **Overview**: Normalize counts or values in a vector or counter.
  - **Parameters**:
    - `vectorOrCounter`: Vector or Counter to normalize.
  - **Returns**: Normalized counter or vector.

- **flipCoin(p)**
  - **Overview**: Simulate a coin flip with a probability.
  - **Parameters**:
    - `p`: Probability of returning True.
  - **Returns**: Boolean result.

- **sample(distribution, values=None)**
  - **Overview**: Sample a value from a distribution.
  - **Parameters**:
    - `distribution`: List of probabilities.
    - `values`: List of values corresponding to the probabilities.
  - **Returns**: Sampled value.

- **nSample(distribution, values, n)**
  - **Overview**: Sample n values from a distribution.
  - **Parameters**:
    - `distribution`: List of probabilities.
    - `values`: List of values corresponding to the probabilities.
    - `n`: Number of samples to draw.
  - **Returns**: List of sampled values.

## Exception Hierarchy Documentation
- **TimeoutFunctionException**: Raised when a function exceeds 
  the specified timeout.
  
## Revision History

| Date Modified | Version Delta | Change Description                            | Author Initials |
|---------------|---------------|----------------------------------------------|------------------|
| 2023-01-01    | 1.0.0         | Initial creation of the module.             | J.D.             |
| 2023-10-20    | 1.0.1         | Updated docstrings and reorganized structure.| B.M.             |