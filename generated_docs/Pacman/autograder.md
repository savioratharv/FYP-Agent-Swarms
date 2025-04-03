# Pacman Autograder Documentation

## Overview
The `autograder.py` file is designed to facilitate the evaluation of student projects within the context of the Pacman AI projects developed at UC Berkeley. This script manages the execution of tests against student code, providing grading and feedback based on specified test cases.

## Functions

### readCommand(argv)
Registers command-line options and sets default values for grading configurations. Returns an object containing the parsed command-line arguments.

**Parameters:**
- `argv`: List of arguments passed from the command line.

**Returns:**
- `options`: An object containing the parsed options.

---

### confirmGenerate()
Prompts the user for confirmation before overwriting solution files. This ensures that users are aware of data loss when generating new solution files.

---

### setModuleName(module, filename)
Attempts to set the `__file__` attribute for functions and classes in a module to the provided filename, aiming to enhance traceback clarity.

**Parameters:**
- `module`: The module whose functions and classes will have their `__file__` attribute set.
- `filename`: The name of the file associated with the module.

---

### loadModuleString(moduleSource)
Loads a module from a string containing the source code. This method is intended for dynamic module loading in a more flexible manner.

**Parameters:**
- `moduleSource`: The source code of the module as a string.

**Returns:**
- The dynamically loaded module.

---

### loadModuleFile(moduleName, filePath)
Loads a module from a specified file path. This function handles the file input/output for reading the student or test class code.

**Parameters:**
- `moduleName`: The name of the module to load.
- `filePath`: The file path to the module.

**Returns:**
- The loaded module.

---

### readFile(path, root="")
Reads the content of a file from disk and returns it as a string.

**Parameters:**
- `path`: The relative path to the file.
- `root`: The root directory from which the path is constructed (default is an empty string).

**Returns:**
- The content of the file as a string.

---

### evaluate(generateSolutions, testRoot, moduleDict, exceptionMap=ERROR_HINT_MAP, edxOutput=False, muteOutput=False, gsOutput=False, printTestCase=False, questionToGrade=None, display=None)
Executes tests on student code and evaluates its correctness based on specified parameters. This function aggregates grading results and outputs.

**Parameters:**
- `generateSolutions`: Boolean flag determining if solutions should be generated.
- `testRoot`: The directory containing test case files.
- `moduleDict`: Dictionary mapping module names to loaded modules.
- `exceptionMap`: Optional mapping for error hints (default is pre-defined).
- `edxOutput`: Boolean flag for outputting in edX format.
- `muteOutput`: Boolean flag to suppress output during execution.
- `gsOutput`: Boolean flag for generating GradeScope output.
- `printTestCase`: Boolean for printing each test case before running.
- `questionToGrade`: Specific question to grade (if any).
- `display`: Display settings for graphics.

**Returns:**
- The total points awarded based on test evaluations.

---

### getDepends(testParser, testRoot, question)
Determines all dependencies for a specified question and collects them recursively. This is critical for ensuring all required tests are executed.

**Parameters:**
- `testParser`: An instance for parsing test configurations.
- `testRoot`: The root directory for test cases.
- `question`: The specific question for which to find dependencies.

**Returns:**
- A list of all dependent questions.

---

### getTestSubdirs(testParser, testRoot, questionToGrade)
Retrieves subdirectories corresponding to tests that need to be run based on dependencies and configuration.

**Parameters:**
- `testParser`: An instance for parsing test configurations.
- `testRoot`: The root directory for test cases.
- `questionToGrade`: The specific question to grade.

**Returns:**
- A list of questions/subdirectories to be tested.

---

### runTest(testName, moduleDict, printTestCase=False, display=None)
Executes a single test case specified by `testName`. This function manages both the evaluation and potential display of test outputs.

**Parameters:**
- `testName`: The name of the test case to run.
- `moduleDict`: Dictionary mapping module names to loaded modules.
- `printTestCase`: Boolean to determine if the test case details should be printed.
- `display`: Optional display settings.

---

### getDisplay(graphicsByDefault, options=None)
Determines the graphics settings for the display based on user options and default settings.

**Parameters:**
- `graphicsByDefault`: Boolean indicating if graphics are enabled by default.
- `options`: Object containing command-line options.

**Returns:**
- An instance of a display class appropriate for running Pacman games or a null graphics class if graphics are disabled.

---

### main
The entry point of the script, handling command-line arguments and orchestrating the loading of student code, the execution of tests, and evaluation.