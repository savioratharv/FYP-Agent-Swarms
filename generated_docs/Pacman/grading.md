# Grading System for Pacman AI Projects

## Module Purpose
The grading module provides a structured way to score student submissions for the Pacman AI projects at UC Berkeley. It allows the definition of grading schemes, captures errors and messages, and outputs scores for various platforms such as GradeScope and edX. The functionality aids educators in evaluating student work and providing feedback systematically and clearly.

## Author List
- John DeNero (Lead Developer)
- Dan Klein (Co-developer)
- Brad Miller (Student Grading Integration)
- Nick Hay (Student Grading Integration)
- Pieter Abbeel (Student Grading Integration)

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified: 2023-10-20

## Version
- Version: 1.0.0

## Dependencies
- Python 3.6 or higher
- cgi 1.0
- time 1.0
- sys 1.0
- json 1.0
- traceback 1.0
- pdb 1.0
- collections 1.0
- util (custom module)

## Public Interface Exports
- `Grades`: Main class for managing grading logic.
- `Counter`: A utility class for counting scores with default values.

## Internal Implementation Details
- The `Grades` class handles initialization, grading operations, message formatting, and output generation for grades.
- The `Counter` class extends dictionary functionality for score management.

## Constant Definitions
- No constants are defined in this module, but the project might include configurations in the external `util` module.

## Class/Function Relationships
- `Grades` utilizes the `Counter` class for scoring.
- `Grades` defines methods such as `grade`, `addPoints`, `fail`, and output methods for integration with grading platforms.

## Class: Grades
### Overview
A data structure for project grades, along with formatting code to display them.

### Parameters
- `projectName` (str): The name of the project.
- `questionsAndMaxesList` (list): A list of tuples containing question names and their maximum points.
- `gsOutput` (bool): Flag to enable GradeScope output.
- `edxOutput` (bool): Flag to enable edX output.
- `muteOutput` (bool): Flag to suppress console output.

### Methods
- `addPrereq(question, prereq)`: Adds a prerequisite relationship between questions.
- `grade(gradingModule, exceptionMap={}, bonusPic=False)`: Grades each question using a provided grading module.
- `produceOutput()`: Generates HTML output for edX integration.
- `produceGradeScopeOutput()`: Produces output for GradeScope integration.
- Additional methods for managing points and messages.

## Class: Counter
### Overview
A dictionary-based structure with a default value of zero for score counting.

### Parameters
- Inherits from `dict`.

### Methods
- `__getitem__(idx)`: Returns the current score or zero if not set.
- `totalCount()`: Returns the sum of counts for all keys.

## Revision History
| Date Modified | Version Delta | Change Description               | Author Initials |
|---------------|---------------|----------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of grading module | JD                |
| 2023-10-20    | 1.0.1        | Added exception handling and formatting updates | DK, BM            |

## Usage Examples
```python
# To create an instance of Grades:
grades = Grades("Pacman Project", [("q1", 10), ("q2", 15)], gsOutput=True)

# Grading the project:
grades.grade(sys.modules[__name__], exceptionMap={})
```

### Exception Hierarchy Documentation
- `Exception`: Base class for all exceptions.
  - `KeyError`: Raised when a non-existing question is accessed.
  - `TypeError`: Raised for incorrect handling of types during operations.
  - Custom exceptions may be raised by the grading functions in the `gradingModule`.