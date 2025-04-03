# projectParams.py Documentation

## Overview
The `projectParams.py` file is a configuration file that sets up various parameters for the Pacman AI projects as developed at UC Berkeley. The file primarily defines constants that are used across multiple components of the project.

## Constants

### STUDENT_CODE_DEFAULT
- **Type**: String
- **Value**: `'searchAgents.py,search.py'`
- **Description**: This constant holds the default filenames for the student code files that will be used for grading purposes. It specifies the main search-related files where the student's implementation is expected to reside.

### PROJECT_TEST_CLASSES
- **Type**: String
- **Value**: `'searchTestClasses.py'`
- **Description**: This constant contains the name of the file that includes the test classes for validating the student's implementations. It serves as a reference point for the autograder to check the functionality of search algorithms.

### PROJECT_NAME
- **Type**: String
- **Value**: `'Project 1: Search'`
- **Description**: This constant names the project, indicating that it is the first project in a series focused on search algorithms within the Pacman game context. This is helpful for user context and clarity about the project's purpose.

### BONUS_PIC
- **Type**: Boolean
- **Value**: `False`
- **Description**: This boolean constant indicates whether a bonus picture is available for the project. A value of `False` suggests that there are no additional bonus features accessible in the current setup. 

## Note
This file serves as a foundational setup for the larger Pacman AI projects and should be modified with caution to maintain consistency across the project.