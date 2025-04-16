# Test Parser

## Module Purpose
The Test Parser module is designed to read test files, remove comments, and parse key-value pairs from the content. It supports both single-line and multi-line string values, facilitating the configuration of test cases in a structured manner. The resulting data can be utilized for automated testing frameworks, ensuring correctness and reliability in software development.

## Author List
- John DeNero: Lead Developer
- Dan Klein: Co-Developer
- Brad Miller: Student Side Autograding Contributor
- Nick Hay: Student Side Autograding Contributor
- Pieter Abbeel: Student Side Autograding Contributor

## Creation/Modification Dates
- Created: 2023-10-01
- Last Modified: 2023-10-01

## Version
- Version: 1.0.0

## Dependency List
- Python 3.6 or higher

## Public Interface Exports
```python
class TestParser(object)
```

## Internal Implementation Details
- `removeComments`: Private method that removes comments from lines of text, leaving only functional code.
- `parse`: Public method that reads a test file, processes its content, and returns a structured dictionary.

## Constant Definitions
N/A

## Class/Function Relationships
- `TestParser`: Main class that contains methods to read and parse test files.
  - `removeComments`: Method to filter out comments from the input lines.
  - `parse`: Method to parse key-value pairs and multiline strings.

## Class Documentation

### `TestParser`

#### Functionality Overview
The `TestParser` class provides an interface to read test files and retrieve structured data while extracting useful content and removing comments. 

#### Parameters
- `path` (str): The file path of the test file to be parsed.

#### Returns
N/A

#### Usage Example
```python
parser = TestParser('path/to/testfile.txt')
test_data = parser.parse()
```

#### Exception Hierarchy Documentation
- `SystemExit`: Raised when an error occurs during parsing.

## Method Documentation

### `removeComments(rawlines)`

#### Functionality Overview
Removes comments from the provided list of raw lines.

#### Parameters
- `rawlines` (list of str): Lines of text from which comments will be removed.

#### Returns
- `str`: The cleaned lines as a single string with comments removed.

#### Usage Example
```python
lines = ["key: value # this is a comment", "another_key: another_value"]
cleaned = parser.removeComments(lines)
```

---

### `parse()`

#### Functionality Overview
Reads the test file, removes comments, and parses its content into a structured dictionary.

#### Parameters
N/A

#### Returns
- `dict`: A dictionary with parsed test data.

#### Usage Example
```python
test = parser.parse()
print(test['key'])  # Output: value
```

#### Exception Hierarchy Documentation
- `SystemExit`: Raised when a parsing error is detected.

## Revision History

| Date Modified | Version Delta | Change Description                     | Author Initials |
|---------------|---------------|---------------------------------------|------------------|
| 2023-10-01    | 1.0.0        | Initial creation of the Test Parser. | JD, DK            |