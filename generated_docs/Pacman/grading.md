# Grading Module Documentation

## Project Name
Pacman Autograder

## Module Purpose
The Grading module is designed to facilitate the automated grading of student projects 
in the Pacman AI project series. It establishes a grading scheme, collects points 
awarded for various questions, and provides formatted output for various platforms, 
including email and web-based courses. This module also incorporates exception handling 
to provide informative feedback on grading outcomes while maintaining a structured 
overview of the grading process.

## Author List
- John DeNero: Lead Developer
- Dan Klein: Core Contributor
- Brad Miller: Student Side Autograding
- Nick Hay: Student Side Autograding
- Pieter Abbeel: Student Side Autograding

## Creation/Modification Dates
- Creation Date: 2023-10-01
- Last Modified: 2023-10-01

## Version
1.0.0

## Dependency List
- Python 3.6+

## Public Interface Exports
- `Grades`: Main class responsible for managing grading functionality.
- `Counter`: Subclass enhancing dictionary behavior for counting operations.

## Internal Implementation Details
The `Grades` class encapsulates methods for grading questions, managing 
prerequisites, and producing outputs tailored for educational platforms such 
as Gradescope and edX. The `Counter` class maintains a count of points, simplifying 
total calculations.

## Constant Definitions
None defined.

## Class/Function Relationships
- `Grades` class uses:
  - `Counter` for point tallying.
  - `util.TimeoutFunction` to manage execution time for grading functions.
  - Exception handling functions from the built-in Python library.

## Class `Grades`

### Functionality Overview
Handles the grading logic for project-based assessments, including setup, question 
grading, exception handling, and output formatting.

### Methods

#### `__init__(projectName, questionsAndMaxesList, gsOutput=False, edxOutput=False, muteOutput=False)`
- **Parameters:**
  - `projectName`: Name of the project.
  - `questionsAndMaxesList`: List of tuples containing question name and max score.
  - `gsOutput`: Boolean for enabling Gradescope output.
  - `edxOutput`: Boolean for enabling edX output.
  - `muteOutput`: Boolean to suppress console output.
- **Returns:** None
- **Usage Example:**
  ```python
  grades = Grades("Pacman Project", [("q1", 10), ("q2", 15)])
  ```

#### `addPrereq(question, prereq)`
- **Parameters:**
  - `question`: The question requiring a prerequisite.
  - `prereq`: The prerequisite question.
- **Returns:** None
- **Usage Example:**
  ```python
  grades.addPrereq("q2", "q1")
  ```

#### `grade(gradingModule, exceptionMap={}, bonusPic=False)`
- **Parameters:**
  - `gradingModule`: Module containing grading functions.
  - `exceptionMap`: Map of specific exception hints.
  - `bonusPic`: Boolean flag for displaying a bonus message.
- **Returns:** None
- **Usage Example:**
  ```python
  grades.grade(sys.modules[__name__])
  ```
- **Exception Hierarchy Documentation:**
  - Might raise exceptions related to timeouts or grading logic failures.

#### `addExceptionMessage(q, inst, traceback)`
- **Parameters:**
  - `q`: Question identifier.
  - `inst`: Exception instance.
  - `traceback`: Traceback information.
- **Returns:** None

#### `produceOutput()`
- **Parameters:** None
- **Returns:** None
- **Usage Example:** Called internally after grading is finished to generate output.

...

## Revision History

| Date Modified | Version Delta | Change Description                           | Author Initials |
|---------------|---------------|---------------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of grading module.         | JD, DK           |