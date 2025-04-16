# Test Classes

## Module Purpose
The `testClasses.py` module provides a framework for defining and executing test cases for educational projects, particularly for grading assignments in AI and machine learning. It supports various question types for assigning credits based on test outcomes.

## Author List
- John DeNero (Developer)
- Dan Klein (Developer)
- Brad Miller (Autograder Engineer)
- Nick Hay (Autograder Engineer)
- Pieter Abbeel (Autograder Engineer)

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Modification Dates: 2023-10-15

## Version
- Version: 1.0.0

## Dependency List
- Python 3.6 or higher

## Public Interface Exports
- `Question`: The abstract base class for creating specific question types.
- `PassAllTestsQuestion`: A class for questions that require all tests to pass.
- `ExtraCreditPassAllTestsQuestion`: A class extending `Question` with extra credit.
- `HackedPartialCreditQuestion`: A class supporting partial credit based on test cases.
- `Q6PartialCreditQuestion`: A class that checks for failures but does not affect grades.
- `PartialCreditQuestion`: A class for managing partial credit tests.
- `NumberPassedQuestion`: A class that grades based on the number of passed test cases.
- `TestCase`: The base class for defining individual test cases.

## Internal Implementation Details
- The module employs a class-based approach to model questions and test cases.
- Each question type defines specific grading logic in the `execute` method.
- Test case execution results are managed through a `grades` object, which tracks scores and messages.

## Constant Definitions
- None defined within this module.

## Class/Function Relationships
- `Question` (base class) is extended by multiple classes which implement various grading schemes.
- Each `Question` instance contains a list of test cases (`TestCase` objects) that are executed to determine grading.

## Class Descriptions

### `Question`
- Overview: Base class for defining questions with test cases.
- Parameters:
  - `questionDict`: Dictionary containing configuration for the question.
  - `display`: Display string for the question.
- Methods:
  - `addTestCase(testCase, thunk)`: Adds a test case.
  - `execute(grades)`: Executes the defined test cases.
- Raises:
  - NotImplementedError: When calling the abstract `execute` method.

### `PassAllTestsQuestion`
- Overview: Inherits from `Question`; requires all test cases to pass for full credit.
- Inherits:
  - `Question`
- Overrides:
  - `execute(grades)` to handle grading based on all tests passing.

### `ExtraCreditPassAllTestsQuestion`
- Overview: Extends `PassAllTestsQuestion` to support extra credit.
- Inherits:
  - `PassAllTestsQuestion`
- Overrides:
  - `execute(grades)` to add extra points if all tests pass.

### `HackedPartialCreditQuestion`
- Overview: A question type that allows partial credit based on specific tests.
- Inherits:
  - `Question`
- Overrides:
  - `execute(grades)` for custom logic on credit allocation.

### `Q6PartialCreditQuestion`
- Overview: A question checking for failures while not affecting grade unless tests fail.
- Inherits:
  - `Question`
- Overrides:
  - `execute(grades)` to track test results.

### `PartialCreditQuestion`
- Overview: Manages partial credit for questions.
- Inherits:
  - `Question`
- Overrides:
  - `execute(grades)` for grading.

### `NumberPassedQuestion`
- Overview: Awards points based on the number of passed test cases.
- Inherits:
  - `Question`
- Overrides:
  - `execute(grades)` to tally passed tests.

### `TestCase`
- Overview: Base class for defining the individual tests associated with questions.
- Parameters:
  - `question`: Reference to the parent question.
  - `testDict`: Dictionary with test configuration.
- Methods:
  - `execute(grades, moduleDict, solutionDict)`: Executes the test and handles grading.
  - `testPass(grades)`: Marks a test as passed.
  - `testFail(grades)`: Marks a test as failed.

## Revision History
| Date Modified | Version Delta | Change Description                      | Author Initials |
|---------------|---------------|----------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial version                        | JD, DK            |
| 2023-10-15    | 1.0.1        | Updated documentation and comments     | JD, DK            |