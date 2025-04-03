# Grades Class Documentation

## Overview
The `Grades` class is designed to manage and compute project grades for educational assignments. It provides functionalities for grading, output formatting, and exception handling during the grading process. This class also supports output for platforms like edX and GradeScope.

## Function-by-Function Overview

### `__init__(self, projectName, questionsAndMaxesList, gsOutput=False, edxOutput=False, muteOutput=False)`
- **Purpose**: Initializes an instance of the `Grades` class with project name, questions, maximum scores, and output options.
- **Parameters**:
  - `projectName`: Name of the project being graded.
  - `questionsAndMaxesList`: A list of tuples containing question names and their respective maximum scores.
  - `gsOutput`: Boolean option to enable GradeScope output.
  - `edxOutput`: Boolean option to enable edX output.
  - `muteOutput`: Boolean option to suppress output during grading.
- **Attributes**:
  - Initializes dictionaries to track points, messages, and prerequisites for the questions.
  - Captures the start time for the grading session.

### `addPrereq(self, question, prereq)`
- **Purpose**: Adds a prerequisite relationship between questions.
- **Parameters**:
  - `question`: The question that has a prerequisite.
  - `prereq`: The prerequisite question that must be completed before the specified question.

### `grade(self, gradingModule, exceptionMap={}, bonusPic=False)`
- **Purpose**: Grades each specified question using functions defined in the provided grading module.
- **Parameters**:
  - `gradingModule`: The grading module containing grading functions for each question.
  - `exceptionMap`: A mapping of exceptions to specific questions for tailored hints.
  - `bonusPic`: Boolean option to print a bonus image upon achieving full credit.
- **Logic**:
  - Iterates through each question to execute grading functions, handling exceptions, and maintaining a completion status.

### `addExceptionMessage(self, q, inst, traceback)`
- **Purpose**: Formats and adds a message for any exceptions raised during grading.
- **Parameters**:
  - `q`: The current question being graded.
  - `inst`: The instance of the raised exception.
  - `traceback`: The traceback object for the exception.

### `addErrorHints(self, exceptionMap, errorInstance, questionNum)`
- **Purpose**: Adds hints related to errors encountered during grading, based on the type of exception.
- **Parameters**:
  - `exceptionMap`: A map of exceptions to hints for each question.
  - `errorInstance`: The instance of the encountered error.
  - `questionNum`: The number of the question where the error occurred.

### `produceGradeScopeOutput(self)`
- **Purpose**: Generates and writes the output for GradeScope in JSON format.
- **Logic**:
  - Creates an output dictionary containing total scores and individual question results, then saves this as `gradescope_response.json`.

### `produceOutput(self)`
- **Purpose**: Generates and writes the output for edX in HTML format.
- **Logic**:
  - Aggregates the results for each question and overall score, writing the formatted results to `edx_response.html` and the total score to `edx_grade`.

### `fail(self, message, raw=False)`
- **Purpose**: Marks the grading state as failed, assigns zero credit to the current question, and logs the failure message.
- **Parameters**:
  - `message`: The message indicating failure details.
  - `raw`: Boolean option indicating whether the message should be treated as raw output.

### `assignZeroCredit(self)`
- **Purpose**: Assigns zero points for the current question being graded.

### `addPoints(self, amt)`
- **Purpose**: Adds a specified amount of points to the current question's score.
- **Parameters**:
  - `amt`: The amount of points to be added.

### `deductPoints(self, amt)`
- **Purpose**: Deducts a specified amount of points from the current question's score.
- **Parameters**:
  - `amt`: The amount of points to be deducted.

### `assignFullCredit(self, message="", raw=False)`
- **Purpose**: Assigns the maximum possible points to the current question and optionally logs a message.
- **Parameters**:
  - `message`: Optional message to log regarding full credit assignment.
  - `raw`: Boolean option indicating if the message is raw output.

### `addMessage(self, message, raw=False)`
- **Purpose**: Adds a message to the current question, optionally formatting it for HTML output.
- **Parameters**:
  - `message`: The message to be added.
  - `raw`: Boolean option to indicate if the message should be treated as raw output.

### `addMessageToEmail(self, message)`
- **Purpose**: (Deprecated) Intended to add a message for email notifications.
- **Parameters**:
  - `message`: The message text to be added.
  
### Counter Class Overview

#### `__getitem__(self, idx)`
- **Purpose**: Extends dict behavior to return a default value of zero for missing keys.

#### `totalCount(self)`
- **Purpose**: Returns the sum of values for all keys within the `Counter` instance.