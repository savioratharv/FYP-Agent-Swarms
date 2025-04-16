# Ghost Agents

## Module Purpose
This module defines the behavior of ghost agents in a grid-based game environment, such as Pacman. It includes different ghost strategies for movement: one that acts randomly and another that prioritizes chasing the player or fleeing when in a scared state. The module utilizes action distribution mechanisms to determine ghost actions based on their state and proximity to Pacman.

## Author List
- John DeNero (Primary Developer)
- Dan Klein (Core Developer)
- Brad Miller (Autograding Integration)
- Nick Hay (Autograding Integration)
- Pieter Abbeel (Autograding Integration)

## Creation/Modification Dates
- Creation Date: 2021-09-01
- Last Modified Date: 2023-10-02

## Version
- Version: 1.0.0

## Dependency List
- Python >= 3.6
- Game Module >= 1.0.0
- Util Module >= 1.0.0

## Public Interface Exports
- `GhostAgent`: Base class defining a ghost agent.
- `RandomGhost`: Subclass implementing a ghost that acts randomly.
- `DirectionalGhost`: Subclass implementing a ghost that prefers to chase or flee.

## Internal Implementation Details
The `GhostAgent` class is an abstract base class for different types of ghosts. The `getDistribution` method is defined as an abstract method and must be implemented in derived classes. The `RandomGhost` class implements a uniform random action selection, while the `DirectionalGhost` implements behavior based on proximity to Pacman and whether the ghost is scared.

## Constant Definitions
- `STOP`: Direction indicating the ghost should not move.
- `DIRECTIONS`: Possible movement directions for the ghost.

## Class/Function Relationships
- `GhostAgent`: Parent class of `RandomGhost` and `DirectionalGhost`.
- `getDistribution`: Method implemented differently in `RandomGhost` and `DirectionalGhost`.

## Revision History
| Date Modified | Version Delta | Change Description                         | Author Initials |
|---------------|---------------|-------------------------------------------|------------------|
| 2021-09-01    | 1.0.0        | Initial creation of ghost agent classes. | JD                |
| 2023-10-02    | 1.0.1        | Refined `DirectionalGhost` logic for more nuanced behavior. | JD                |

## Class: GhostAgent
### Overview
Base class for ghost agents. Responsible for getting an action based on the current game state.

### Method: `getAction`
**Overview**: Chooses an action based on action distribution.

**Parameters**:
| Name   | Type   | Description                       |
|--------|--------|-----------------------------------|
| state  | State  | The current game state.          |

**Returns**:
| Type        | Description                     |
|-------------|---------------------------------|
| Direction   | The selected action direction.  |

**Usage Example**:
```python
ghost = GhostAgent(index=1)
action = ghost.getAction(currentState)
```

## Class: RandomGhost
### Overview
A ghost that chooses a legal action uniformly at random.

### Method: `getDistribution`
**Overview**: Returns a uniform distribution over legal actions.

**Parameters**:
| Name   | Type   | Description                       |
|--------|--------|-----------------------------------|
| state  | State  | The current game state.          |

**Returns**:
| Type        | Description                               |
|-------------|-------------------------------------------|
| Counter     | A distribution over legal actions.       |

**Usage Example**:
```python
randomGhost = RandomGhost(index=1)
distribution = randomGhost.getDistribution(currentState)
``` 

## Class: DirectionalGhost
### Overview
A ghost that prefers to move towards Pacman when not scared and flees when scared.

### Method: `getDistribution`
**Overview**: Returns a distribution over actions based on distance to Pacman.

**Parameters**:
| Name            | Type              | Description                       |
|-----------------|-------------------|-----------------------------------|
| state           | State             | The current game state.          |

**Returns**:
| Type        | Description                       |
|-------------|-----------------------------------|
| Counter     | A distribution over actions ranked by preference. |

**Usage Example**:
```python
directionalGhost = DirectionalGhost(index=1)
distribution = directionalGhost.getDistribution(currentState)
``` 

### Exception Hierarchy Documentation
No exceptions are explicitly raised in the current module. However, it is advisable to handle potential errors when calling external methods used within this module, such as fetching states or legal actions that may not exist.