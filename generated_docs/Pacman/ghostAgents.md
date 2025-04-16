# Pacman Ghost Agents

## Module Purpose
This module implements ghost agents for the Pacman game, providing various strategies 
for ghost interactions. Two types of ghost behaviors are represented: a random ghost that 
chooses actions uniformly at random, and a directional ghost that behaves intelligently 
by either chasing Pacman or fleeing when scared. These agents utilize the current game 
state to make decisions.

## Author List
- John DeNero (Lead Developer)
- Dan Klein (Lead Developer)
- Brad Miller (Automated Grader)
- Nick Hay (Automated Grader)
- Pieter Abbeel (Automated Grader)

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- game 0.1.0
- util 0.1.0

## Public Interface Exports
- `GhostAgent`: The base class for ghost agents.
- `RandomGhost`: A ghost that chooses legal actions uniformly at random.
- `DirectionalGhost`: A ghost that prefers to rush Pacman or flee when scared.

## Internal Implementation Details
The ghosts utilize the game state to determine their actions. The `getDistribution` method 
is overridden in derived classes to customize behavior based on ghosts' current states 
and positions relative to Pacman.

## Constant Definitions
- None

## Class/Function Relationships
- `GhostAgent` is the base class for ghost agents and provides the interface for getting 
  actions based on the game state.
- `RandomGhost` inherits from `GhostAgent` and implements random movement behavior.
- `DirectionalGhost` inherits from `GhostAgent` and implements intelligent chasing or 
  fleeing behavior.

## Class Definitions

### GhostAgent
```python
class GhostAgent(Agent):
```
#### Functionality Overview
Base class for ghost agents, providing a common interface for all types of ghosts.

#### Parameters
- `index (int)`: Index representing the ghost's identification.

#### Methods
- `def getAction(self, state) -> str`: Determines the ghost's action based on 
  the distribution.
- `def getDistribution(self, state) -> util.Counter`: Should be implemented by 
  subclasses.

### RandomGhost
```python
class RandomGhost(GhostAgent):
```
#### Functionality Overview
A ghost that chooses a legal action uniformly at random.

#### Parameters
- `index (int)`: Index representing the ghost's identification.

#### Methods
- `def getDistribution(self, state) -> util.Counter`: Returns a uniform distribution 
  over legal actions.

### DirectionalGhost
```python
class DirectionalGhost(GhostAgent):
```
#### Functionality Overview
A ghost that prefers to rush Pacman or flee when scared.

#### Parameters
- `index (int)`: Index representing the ghost's identification.
- `prob_attack (float)`: Probability of attacking if not scared.
- `prob_scaredFlee (float)`: Probability of fleeing when scared.

#### Methods
- `def getDistribution(self, state) -> util.Counter`: Returns a distribution 
  favoring either attacking or fleeing based on the state.

## Revision History
| Date Modified | Version Delta | Change Description | Author Initials |
|---------------|---------------|---------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial implementation | JD, DK |