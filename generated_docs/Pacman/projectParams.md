# Project 1: Search

## Module Purpose
The `projectParams.py` module defines essential configuration parameters and constants 
for the Pacman AI project, specifically targeting search algorithms. This module 
facilitates parameter management for project components like the default student 
code files, project name, and relevant test classes, ensuring that all necessary 
elements are correctly referenced and centralized for ease of development.

## Author List
- John DeNero: Primary developer and project maintainer
- Dan Klein: Core project architect
- Brad Miller: Student-side autograder implementation
- Nick Hay: Student-side autograder support
- Pieter Abbeel: Student-side autograder implementation

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Modification Date: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- Python >= 3.6

# Public Interface Exports
- `STUDENT_CODE_DEFAULT`: Default student code files for the project.
- `PROJECT_TEST_CLASSES`: Test classes for project validation.
- `PROJECT_NAME`: Identifies the project title.
- `BONUS_PIC`: Indicates the inclusion of bonus picture functionalities.

# Internal Implementation Details
The `projectParams.py` module serves as a configuration holder, providing 
global constants that can be imported and utilized in other parts of the Pacman 
AI project. Its design promotes organization and prevents hardcoding of values.

# Constant Definitions
- `STUDENT_CODE_DEFAULT`: 
    - **Type**: String
    - **Purpose**: Defines the default files containing the student's code.
- `PROJECT_TEST_CLASSES`: 
    - **Type**: String
    - **Purpose**: Specifies the test classes to be used in project evaluation.
- `PROJECT_NAME`: 
    - **Type**: String
    - **Purpose**: Holds the name of the project for identification.
- `BONUS_PIC`: 
    - **Type**: Boolean
    - **Purpose**: A flag that determines whether bonus picture functionality is included.

# Class/Function Relationships
No classes or functions are defined in this module. It primarily serves as a 
container for constants and configuration parameters.

# Revision History
| Date Modified | Version Delta | Change Description                       | Author Initials |
|---------------|---------------|-----------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of project parameters. | JD, DK           |