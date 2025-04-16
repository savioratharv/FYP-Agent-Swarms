# Autograder

## Module Purpose
The Autograder module is designed to facilitate the evaluation of student submissions for programming assignments, specifically tailored for AI projects involving the Pacman game framework. It automates the testing process by managing test cases, handling outputs, and generating grading reports based on predefined criteria and student implementation. This enhances the educational experience by providing timely feedback and structured assessment.

## Author List
- John DeNero: Lead Developer
- Dan Klein: Core Developer
- Brad Miller: Student Grading Integrator
- Nick Hay: Student Grading Integrator
- Pieter Abbeel: Educational Outreach

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- Python 3.6+
- grading 1.0.0
- optparse 1.0.0
- os 1.0.0
- re 1.0.0
- sys 1.0.0
- projectParams 1.0.0
- random 1.0.0

## Public Interface Exports
- `readCommand(argv)`: Parses command line options for the autograder.
- `confirmGenerate()`: Confirms if the user wants to overwrite existing solution files.
- `loadModuleFile(moduleName, filePath)`: Loads a module from a specified file path.
- `evaluate(...)`: Evaluates student code against the defined test cases.
- `getDisplay(graphicsByDefault, options=None)`: Returns a graphics display if enabled.

## Internal Implementation Details
- Utilizes `imp` module to load student code dynamically.
- Parses test case configurations using a customized `testParser`.
- Implements a flexible grading system using the `grading` module.
- Supports dependency resolution between test questions.
- Outputs results in various formats depending on user preferences.

## Constant Definitions
- `ERROR_HINT_MAP`: A mapping of error types to helpful hints for the students.
- `PROJECT_NAME`: The name of the current project as defined in `projectParams`.

## Class/Function Relationships
- The primary functions `evaluate()`, `runTest()`, and `getDepends()` interact closely with test cases and grading logic.
- `loadModuleFile()` aids in dynamically importing modules, crucial for handling student submissions.

## Revision History
| Date Modified | Version Delta | Change Description                          | Author Initials |
|---------------|---------------|-------------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of the autograder module.| JD, DK, BM, NH, PA | 

## Functionality Overview
The key functions within this module include:
- `readCommand()`: Processes command-line arguments and options for configuring the tests.
- `confirmGenerate()`: Prompts the user before overwriting solution files.
- `loadModuleFile()`: Loads the specified module from the given file path.
- `evaluate()`: Runs the tests against student code, managing outputs and grading.

### Parameters and Return Value Tables
#### `readCommand(argv)`
| Parameter | Type      | Description                          |
|-----------|-----------|--------------------------------------|
| argv      | list     | List of command line arguments.      |
| Return    | object    | Parsed options object.                |

#### `confirmGenerate()`
| Parameter | Type      | Description                          |
|-----------|-----------|--------------------------------------|
| None      | None      | Prompts user for confirmation.      |

#### `loadModuleFile(moduleName, filePath)`
| Parameter | Type      | Description                                 |
|-----------|-----------|---------------------------------------------|
| moduleName| str       | Name of the module to load.                |
| filePath  | str       | Path to the module file.                   |
| Return    | module    | Loaded module object.                      |

#### `evaluate(generateSolutions, testRoot, moduleDict, ...)`
| Parameter                 | Type      | Description                                          |
|---------------------------|-----------|-----------------------------------------------------|
| generateSolutions         | bool      | Whether to generate solution files.                 |
| testRoot                  | str       | Root directory for test cases.                      |
| moduleDict                | dict      | Dictionary of modules (student code).               |
| ...                       | ...       | Additional parameters for various options.          |
| Return                    | int       | Total points scored by the student.                 |

## Usage Examples & Edge Cases
- To run the autograder with specified options:
  ```
  python autograder.py --student-code student_code.py --test-directory test_cases
  ```
- If intending to generate solutions, verify beforehand:
  ```
  python autograder.py --generate-solutions
  ```
- Edge case handling for non-existent test files should be incorporated within the test parsing logic.

## Exception Hierarchy Documentation
- `IndexError`: Raised when accessing elements from an empty list or out-of-bound indices during grading.
- `AttributeError`: Raised when attempting to access an attribute that does not exist in the provided object state.
- Custom error handling can be augmented through the `ERROR_HINT_MAP` for clearer student feedback.