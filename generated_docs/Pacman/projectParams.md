# Project Name: Project 1: Search

## Module Purpose
The `projectParams.py` module serves as a configuration file for the Pacman AI projects developed at UC Berkeley. It defines essential parameters required for the operation of search algorithms, including project-specific settings and module references needed for educational purposes. This file helps streamline the codebase by holding project-level constants and defaults, ensuring organization and clarity throughout various implementations.

## Author List
- John DeNero - Project Lead
- Dan Klein - Co-Developer
- Brad Miller - Student Autograder Development
- Nick Hay - Student Autograder Development
- Pieter Abbeel - Student Autograder Development

## Creation/Modification Dates
- Created: 2023-10-01
- Last Modified: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- Python >= 3.6

## Public Interface Exports
- `STUDENT_CODE_DEFAULT`
- `PROJECT_TEST_CLASSES`
- `PROJECT_NAME`
- `BONUS_PIC`

## Internal Implementation Details
The module largely serves as a constants holder and does not define complex functions or classes. Each parameter is designed to provide specifications clearly without processing logic.

## Constant Definitions
### STUIDENT_CODE_DEFAULT
Default file names for student code submissions.
- Type: `str`
- Example: 'searchAgents.py,search.py'

### PROJECT_TEST_CLASSES
Test classes module reference.
- Type: `str`
- Example: 'searchTestClasses.py'

### PROJECT_NAME
The name framing the current project.
- Type: `str`
- Example: 'Project 1: Search'

### BONUS_PIC
Flag indicating the availability of a bonus picture.
- Type: `bool`
- Example: `False`

## Class/Function Relationships
This file does not contain classes or functions; it merely defines constants for use in other modules related to the Pacman AI project.

## Revision History

| Date Modified | Version Delta | Change Description                                   | Author Initials |
|---------------|---------------|-----------------------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of project parameter definitions.  | JD, DK           |