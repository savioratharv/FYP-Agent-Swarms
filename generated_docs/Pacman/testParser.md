# TestParser Module

## Module Purpose
The `TestParser` module provides functionality to parse test case files, extracting meaningful data while ignoring comments and blank lines. It facilitates the structured representation of test cases, supporting both single-line and multi-line descriptions. This module is essential for managing automated test cases in a readable and efficient manner.

## Author List
- John DeNero: Lead Developer
- Dan Klein: Core Designer
- Brad Miller: Student Side Autograding Contributor
- Nick Hay: Student Side Autograding Contributor
- Pieter Abbeel: Student Side Autograding Contributor

## Creation/Modification Dates
- Created: 2023-10-01
- Last Modified: 2023-10-01

## Version
1.0.0

## Dependencies
- Python 3.6 or higher

## Public Interface Exports
- `TestParser`: Class for parsing test case files.
- `emitTestDict`: Function to emit a parsed test dictionary.

## Internal Implementation Details
### Class: `TestParser`
- **Attributes:**
  - `path (str)`: Path to the test file.
  
- **Methods:**
  - `__init__(self, path)`: Initializes the `TestParser` with the given file path.
  - `removeComments(self, rawlines)`: Removes comments from the raw lines of the test file.
  - `parse(self)`: Parses the test file and returns a structured dictionary of test data.

### Function: `emitTestDict`
- Emits the parsed test dictionary to a specified output handle.

## Constant Definitions
- None defined.

## Class/Function Relationships
- `TestParser` contains methods for reading and interpreting test case files.
- `emitTestDict` operates independently, utilizing the output from the `TestParser`.

## Functions

### `__init__(self, path)`
Initializes a new `TestParser` instance.

#### Parameters
- `path` (str): Path to the test file.

#### Returns
- None

#### Usage Example
```python
parser = TestParser("path/to/test_file")
```

### `removeComments(self, rawlines)`
Removes comments from the provided list of raw lines.

#### Parameters
- `rawlines` (list): A list of strings representing each line from the test file.

#### Returns
- str: The cleaned lines with comments removed.

#### Usage Example
```python
cleaned_lines = parser.removeComments(["line 1", "line 2 # comment"])
```

### `parse(self)`
Parses the contents of the test file and generates a structured dictionary.

#### Parameters
- None

#### Returns
- dict: A dictionary containing parsed test properties.

#### Usage Example
```python
test_dict = parser.parse()
```

### `emitTestDict(testDict, handle)`
Writes the contents of a given test dictionary to an output handle.

#### Parameters
- `testDict` (dict): The test dictionary to be emitted.
- `handle`: The output handle where the test dictionary content will be written.

#### Returns
- None

#### Usage Example
```python
with open("output.txt", "w") as f:
    emitTestDict(test_dict, f)
```

## Exception Hierarchy Documentation
- `Exception`: Base class for all exceptions raised in this module.
- `SystemExit`: Raised for termination during parsing errors.

## Revision History
| Date Modified | Version Delta | Change Description                        | Author Initials |
|---------------|---------------|------------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial version of the TestParser module| JD, DK           |