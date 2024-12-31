# njson

![](https://github.com/user-attachments/assets/40498f88-3dfe-485b-acba-db34e76b374e)

# DESCRIPTION
* doc. writen by gpt-4o
* Happy new year <3

# About
njson - lib for work with json in python

# How to install
download .whl file out 'release'
and
```
pip install njson.whl
```

## Class: njson

### njson.load(json: str) -> dict

Loads a JSON file and returns its contents as a Python dictionary.

#### Parameters
- json: The path to the JSON file.

#### Returns
- A dictionary containing the parsed JSON data.

#### Raises
- Raises a FileError if the specified file does not exist or is not a valid JSON file.

### njson.write(json: str, ur_dict: dict) -> None

Writes a given dictionary to a specified JSON file, overwriting any existing content.

#### Parameters
- json: The path to the JSON file.
- ur_dict: The dictionary to write to the file.

#### Raises
- Raises a FileError if the specified file does not exist or is not a valid JSON file.

### njson.add(json: str, ur_dict: dict) -> None

Adds key-value pairs from a given dictionary to an existing JSON file without overwriting the existing content.

#### Parameters
- json: The path to the JSON file.
- ur_dict: The dictionary containing the key-value pairs to add.

#### Raises
- Raises a FileError if the specified file does not exist or is not a valid JSON file.

## Usage Example
```python
from njson.main import njson

# Load JSON data from a file

data = njson.load('data.json')

# Modify data

data['newkey'] = 'newvalue'

# Write updated data back to the file

njson.write('data.json', data)

# Add new data to the existing JSON file

njson.add('data.json', {'anotherkey': 'anothervalue'})
```

## Notes

- Ensure that your JSON files are properly formatted.
- The library currently raises a generic error string "FileError" which should ideally be replaced with a specific exception class for better error handling.
