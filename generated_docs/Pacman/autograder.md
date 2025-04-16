# Autograder

## Module Purpose
The Autograder module conducts automated grading of student code submissions for 
projects in a structured format. It manages test case execution, captures results, 
handles dependencies among questions, and can generate solution files. This module 
is integral for both the evaluation of student submissions and for providing feedback 
to enhance their learning experience.

## Authors
- John DeNero: Lead Developer
- Dan Klein: Co-Developer
- Brad Miller: Student Assessment Specialist
- Nick Hay: Student Software Engineer
- Pieter Abbeel: Educational Advisor

## Creation/Modification Dates
- Creation Date: 2022-01-15
- Last Modified Date: 2023-10-22

## Version
- Version: 1.2.0

## Dependencies
- Python >= 3.6
- grading >= 1.0
- optparse >= 1.0
- os >= 1.0
- re >= 1.0
- sys >= 1.0
- projectParams >= 1.0
- random >= 1.0

## Public Interface Exports
- readCommand(argv): Parses command line arguments and returns options.
- confirmGenerate(): Confirms if the user wants to overwrite solution files.
- evaluate(generateSolutions, testRoot, moduleDict, ...): Evaluates student 
  code submissions based on defined test cases.
- getDisplay(graphicsByDefault, options=None): Returns the appropriate display 
  object based on user options and graphics settings.

## Internal Implementation Details
- The module utilizes various helper functions to manage module loading, 
  exception handling, and obtaining test subdirectories.
- Test cases and their results are parsed using the TestParser class, integrating 
  with grading modules to compute final scores.

## Constant Definitions
- ERROR_HINT_MAP: A mapping of potential errors to corresponding hints or 
  suggestions for students encountering those issues during testing.
- projectParams: Imports project-specific parameters such as project name, 
  default student code, and bonus picture definitions.

## Class/Function Relationships
- Run tests by creating instances of Question class within the testClasses module.
- Interacts with the grading module to grade test cases against specified solutions.
- Handles file I/O using os and sys libraries for reading test and solution files 
  from disk.

## Revision History
| Date Modified | Version Delta | Change Description                                           | Author Initials |
|---------------|---------------|-------------------------------------------------------------|------------------|
| 2023-10-22    | 1.2.0        | Enhanced error handling and added dependency checks.        | JD                |
| 2023-07-10    | 1.1.0        | Updated functions for improved readability and performance.  | BK                |
| 2022-01-15    | 1.0.0        | Initial creation of the autograder module.                  | JD, DK            |

## Functionality Overview

### readCommand(argv)
Parses command line arguments for autograder options.

#### Parameters
- argv: List of command line arguments.

#### Returns
- options: Parsed options object containing user-specified settings.

### confirmGenerate()
Confirms if the user intends to overwrite existing solution files.

### evaluate(generateSolutions, testRoot, moduleDict, ...)
Evaluates student code against defined test cases and generates grading reports.

#### Parameters
- generateSolutions: Boolean indicating whether to write solution files.
- testRoot: Root directory containing test cases.
- moduleDict: Dictionary of loaded student modules and classes.

#### Returns
- grades.points: Total points earned by the student based on test results.

### getDisplay(graphicsByDefault, options=None)
Determines the appropriate display settings for running the tests.

#### Parameters
- graphicsByDefault: Boolean indicating default display behavior.
- options: Optional command line options.

#### Returns
- graphics display object: Configured display utility for visual output during tests.

### Exception Handling
The module anticipates various exceptions (e.g., IndexError, AttributeError) 
that might arise during code execution. It aims to provide students with 
meaningful hints to rectify their submissions based on these exceptions. 

### Usage Examples
#### Example of Running the Autograder
```bash
python autograder.py --test-directory test_cases --student-code student_code.py
```

### Edge Cases
- The code must handle non-existent files gracefully and provide clear error messages.
- Must validate user inputs and command line arguments to prevent runtime crashes.