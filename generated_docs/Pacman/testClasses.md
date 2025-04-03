# Function-by-Function Overview of `testClasses.py`

## Class `Question`
- **Purpose**: Models a question in a project, consisting of test cases and a maximum score.
  
### `__init__(self, questionDict, display)`
- **Parameters**:
  - `questionDict`: A dictionary containing question details, including maximum points.
  - `display`: A string for displaying question information.
- **Description**: Initializes a Question object with the maximum points and an empty list of test cases.

### `getDisplay(self)`
- **Returns**: Displays the question information.
- **Description**: Getter method for the display property of the question.

### `getMaxPoints(self)`
- **Returns**: The maximum points assigned to the question.
- **Description**: Getter method for the maximum points property.

### `addTestCase(self, testCase, thunk)`
- **Parameters**:
  - `testCase`: A test case object to be added.
  - `thunk`: A function that will be used to execute the test case.
- **Description**: Adds a test case and its associated function to the list of test cases.

### `execute(self, grades)`
- **Description**: Raises an exception indicating that this method must be overridden in derived classes.

## Class `PassAllTestsQuestion(Question)`
- **Purpose**: Represents a question where all test cases must pass to receive credit.

### `execute(self, grades)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
- **Description**: Executes all test cases; assigns zero credit if any test fails, otherwise assigns full credit.

## Class `ExtraCreditPassAllTestsQuestion(Question)`
- **Purpose**: A variant of the PassAllTests question that allows for extra credit points.

### `__init__(self, questionDict, display)`
- **Parameters**:
  - `questionDict`: A dictionary containing question details including extra points.
  - `display`: A string describing the question.
- **Description**: Initializes an ExtraCreditPassAllTestsQuestion with extra points.

### `execute(self, grades)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
- **Description**: Executes test cases with logic for awarding extra points if all tests pass.

## Class `HackedPartialCreditQuestion(Question)`
- **Purpose**: Assigns partial credit based on specific test cases.

### `execute(self, grades)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
- **Description**: Executes test cases, assigns points based on passed tests, and ensures proper crediting logic.

## Class `Q6PartialCreditQuestion(Question)`
- **Purpose**: Fails the question if any test case fails, without affecting grades otherwise.

### `execute(self, grades)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
- **Description**: Executes test cases and assigns zero credit if any test case fails.

## Class `PartialCreditQuestion(Question)`
- **Purpose**: Similar to Q6PartialCredit with partial credit logic.

### `execute(self, grades)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
- **Description**: Executes test cases; assigns zero credit on failure or recognizes partial credit points.

## Class `NumberPassedQuestion(Question)`
- **Purpose**: Grades based on the number of test cases passed.

### `execute(self, grades)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
- **Description**: Counts the number of passed test cases and adds that to the grade.

## Class `TestCase`
- **Purpose**: Models a generic test case for a question.

### `__init__(self, question, testDict)`
- **Parameters**:
  - `question`: The question to which this test case belongs.
  - `testDict`: A dictionary containing test case details.
- **Description**: Initializes a TestCase object with its parent question and details.

### `raiseNotDefined(self)`
- **Description**: Raises an exception indicating that a method must be overridden in derived classes.

### `getPath(self)`
- **Returns**: The path of the test case.
- **Description**: Getter method for the test case path.

### `__str__(self)`
- **Description**: Raises an exception; intended to be overridden in derived classes to provide string representation.

### `execute(self, grades, moduleDict, solutionDict)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
  - `moduleDict`: A dictionary containing modules for the solution.
  - `solutionDict`: A dictionary containing the solutions.
- **Description**: Raises an exception; intended to be overridden in derived classes to execute the test case.

### `writeSolution(self, moduleDict, filePath)`
- **Parameters**:
  - `moduleDict`: A dictionary containing modules related to the solution.
  - `filePath`: A path where the solution will be written.
- **Returns**: A boolean indicating success or failure.
- **Description**: Raises an exception; intended to be overridden in derived classes to write the solution.

### `testPass(self, grades)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
- **Returns**: True if the test passes.
- **Description**: Logs a message for a passing test case and returns True.

### `testFail(self, grades)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
- **Returns**: False if the test fails.
- **Description**: Logs a message for a failing test case and returns False.

### `testPartial(self, grades, points, maxPoints)`
- **Parameters**:
  - `grades`: An object that manages the grading process.
  - `points`: The points awarded for the test case.
  - `maxPoints`: The maximum points possible for the test case.
- **Returns**: True if the partial test passes.
- **Description**: Logs the results of partial credit tests.

### `addMessage(self, message)`
- **Parameters**:
  - `message`: A string to be added to the test case's messages.
- **Description**: Adds a message to the test case's log for output during grading.