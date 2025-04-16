# Test Classes

## Module Purpose
This module provides classes for modeling questions and test cases in an educational grading system. Each question can have multiple test cases that determine the credit awarded based on their results. The module's design allows for various grading strategies, including full credit, partial credit, and extra credit, facilitating the evaluation of student submissions in a structured and transparent manner.

## Author List
- John DeNero (Primary Developer)
- Dan Klein (Primary Developer)
- Brad Miller (Student Side Autograding)
- Nick Hay (Student Side Autograding)
- Pieter Abbeel (Student Side Autograding)

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified: 2023-10-01

## Version
Version: 1.0.0

## Dependencies
- Python >= 3.6

## Public Interface Exports
- `Question`
- `PassAllTestsQuestion`
- `ExtraCreditPassAllTestsQuestion`
- `HackedPartialCreditQuestion`
- `Q6PartialCreditQuestion`
- `PartialCreditQuestion`
- `NumberPassedQuestion`
- `TestCase`

## Internal Implementation Details
The module implements a class hierarchy where `Question` serves as the base class for different question types that define how the grading process interacts with their respective test cases. Each test case is an instance of the `TestCase` class, which provides standardized output messages for pass and fail scenarios.

## Constant Definitions
(None)

## Class/Function Relationships
- `Question` is the base class for all question types.
- `PassAllTestsQuestion`, `ExtraCreditPassAllTestsQuestion`, `HackedPartialCreditQuestion`,
  `Q6PartialCreditQuestion`, `PartialCreditQuestion`, and `NumberPassedQuestion` inherit from `Question`.
- All test cases are instances of the `TestCase` class.

## Class Descriptions

### Question
Represents a generic question in the grading system.
- **Constructor Parameters**
    - `questionDict`: Dictionary containing question attributes.
    - `display`: String representing how the question should be displayed.
  
- **Methods**
    - `raiseNotDefined()`: Raises an error if the method is not implemented.
    - `getDisplay()`: Returns the display string for the question.
    - `getMaxPoints()`: Returns the maximum points for the question.
    - `addTestCase(testCase, thunk)`: Adds a test case to the question.
    - `execute(grades)`: Executes the test cases and grades them.

### PassAllTestsQuestion
Inherits from `Question`. Requires all tests to pass for full credit.
- **Methods**
    - `execute(grades)`: Executes each test case and assigns credit based on the results.

### ExtraCreditPassAllTestsQuestion
Inherits from `Question`. Allows for extra credit if all tests pass.
- **Constructor Parameters**
    - `questionDict`: Dictionary containing question attributes, including extra points.
  
- **Methods**
    - `execute(grades)`: Executes tests and awards extra points for passing all tests.

### HackedPartialCreditQuestion
Inherits from `Question`. Supports partial credit based on test results.
- **Methods**
    - `execute(grades)`: Executes tests, awarding points for passing tests with specified points.

### Q6PartialCreditQuestion
Inherits from `Question`. Executes tests and fails if any test returns False.
- **Methods**
    - `execute(grades)`: Executes test cases and assigns credit accordingly, based on test results.

### PartialCreditQuestion
Inherits from `Question`. Similar to `Q6PartialCreditQuestion`, manages partial credit.
- **Methods**
    - `execute(grades)`: Similar implementation to `Q6PartialCreditQuestion`.

### NumberPassedQuestion
Inherits from `Question`. The score is equal to the number of passed tests.
- **Methods**
    - `execute(grades)`: Counts the number of passed test cases and assigns that as the score.

### TestCase
Represents an individual test case for a question.
- **Constructor Parameters**
    - `question`: The associated question object.
    - `testDict`: Dictionary containing test attributes.
  
- **Methods**
    - `raiseNotDefined()`: Raises an error if the method is not implemented.
    - `getPath()`: Returns the path for the test case.
    - `execute(grades, moduleDict, solutionDict)`: Executes the test and grades it.
    - `writeSolution(moduleDict, filePath)`: Writes the solution to a file.
    - `testPass(grades)`: Handles the output and grading for a passing test.
    - `testFail(grades)`: Handles the output and grading for a failing test.
    - `testPartial(grades, points, maxPoints)`: Handles partial credit scoring.
    - `addMessage(message)`: Adds message output during test case evaluation.

## Revision History
| Date Modified | Version Delta | Change Description                        | Author Initials |
|---------------|---------------|------------------------------------------|-----------------|
| 2023-10-01    | 1.0.0        | Initial creation of the grading classes. | JD, DK           |