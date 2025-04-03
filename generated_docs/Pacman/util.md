# Pacman Util Documentation

## Overview
The `util.py` file contains various utility classes and functions that support search algorithms and data manipulation in the Pacman AI project. The main classes include `Stack`, `Queue`, `PriorityQueue`, and helper functionalities for probability sampling, distance calculation, and data normalization.

## Classes

### FixedRandom
This class encapsulates a fixed random number generator using a predetermined state, ensuring consistent random values across runs.

### Stack
- **Purpose**: Implements a last-in-first-out (LIFO) container.
- **Methods**:
  - `push(item)`: Adds an item to the top of the stack.
  - `pop()`: Removes and returns the most recently added item.
  - `isEmpty()`: Returns `True` if the stack is empty, otherwise `False`.

### Queue
- **Purpose**: Implements a first-in-first-out (FIFO) container.
- **Methods**:
  - `push(item)`: Inserts an item at the end of the queue.
  - `pop()`: Removes and returns the earliest added item.
  - `isEmpty()`: Returns `True` if the queue is empty, otherwise `False`.

### PriorityQueue
- **Purpose**: Implements a priority queue allowing quick retrieval of the lowest-priority item.
- **Methods**:
  - `push(item, priority)`: Adds an item with a specified priority.
  - `pop()`: Removes and returns the item with the lowest priority.
  - `isEmpty()`: Returns `True` if the priority queue is empty, otherwise `False`.
  - `update(item, priority)`: Updates the priority of an existing item or adds it if not present.

### PriorityQueueWithFunction
- **Purpose**: Extends `PriorityQueue` to accept a custom priority function.
- **Methods**:
  - `push(item)`: Adds an item using the priority defined by the provided function.

### Counter
- **Purpose**: A dictionary-like class for counting occurrences of keys with additional functionalities.
- **Methods**:
  - `__getitem__(idx)`: Retrieves the count for the specified key, defaulting to zero if not present.
  - `incrementAll(keys, count)`: Increments the count for all specified keys.
  - `argMax()`: Returns the key with the highest count.
  - `sortedKeys()`: Returns a sorted list of keys based on their counts.
  - `totalCount()`: Returns the sum of all counts.
  - `normalize()`: Normalizes the counts to sum to 1.
  - `divideAll(divisor)`: Divides all counts by a specified divisor.
  - `copy()`: Returns a copy of the counter.
  - Arithmetic operations: Supports addition, subtraction, and multiplication with other counters.

## Functions

### manhattanDistance(xy1, xy2)
Calculates the Manhattan distance between two points `xy1` and `xy2`.

### raiseNotDefined()
Raises an error indicating that a functional method has not been implemented, mentioning the context of the call.

### normalize(vectorOrCounter)
Normalizes a provided vector or `Counter` by dividing its values by the total sum.

### nSample(distribution, values, n)
Samples `n` values according to a probability distribution provided in `distribution`.

### sample(distribution, values=None)
Samples a single value from a distribution or `Counter`, normalizing if necessary.

### sampleFromCounter(ctr)
Samples a value from a `Counter` based on its distributions.

### getProbability(value, distribution, values)
Calculates the probability of a specific value under a given discrete distribution.

### flipCoin(p)
Simulates a coin flip for a probability `p`, returning `True` or `False`.

### chooseFromDistribution(distribution)
Samples from a distribution which can be a Counter or a list of (probability, key) pairs.

### nearestPoint(pos)
Finds the nearest grid point to a floating-point position by rounding.

### sign(x)
Returns `1` or `-1` based on the sign of `x`.

### arrayInvert(array)
Inverts a 2D matrix represented as a list of lists.

### matrixAsList(matrix, value=True)
Transforms a matrix into a list of coordinates matching a specified boolean value.

### lookup(name, namespace)
Retrieves a method or class by name from a given namespace, enabling dynamic method lookups.

### pause()
Pauses execution and waits for user input to continue.

### TimeoutFunction
- **Purpose**: Wraps functions to implement a timeout feature.
- **Methods**:
  - `__call__(*args, **keyArgs)`: Calls the wrapped function with set timeout handling.

### mutePrint()
Suppresses console output for cleaner execution during tests.

### unmutePrint()
Restores console output after it has been muted.