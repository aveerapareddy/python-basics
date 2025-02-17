# Python String Functions
Python provides a rich set of built-in string functions that allow easy manipulation and analysis of strings. Below is a comprehensive list of commonly used string functions with examples.

## Table of Contents
- [String Creation & Basic Operations](#string-creation--basic-operations)
- [String Modification](#string-modification)
- [String Checking](#string-checking)
- [String Formatting](#string-formatting)
- [String Indexing & Slicing](#string-indexing--slicing)
- [Finding Substrings](#finding-substrings)

---

## String Creation & Basic Operations
```python
s = "Hello, World!"
```

---

## String Modification

| Function | Description | Example |
|----------|------------|---------|
| `lower()` | Converts string to lowercase | `"HELLO".lower()` → `"hello"` |
| `upper()` | Converts string to uppercase | `"hello".upper()` → `"HELLO"` |
| `title()` | Capitalizes the first letter of each word | `"hello world".title()` → `"Hello World"` |
| `capitalize()` | Capitalizes only the first letter of the string | `"hello world".capitalize()` → `"Hello world"` |
| `strip()` | Removes leading and trailing spaces | `" hello ".strip()` → `"hello"` |
| `lstrip()` | Removes leading spaces | `" hello ".lstrip()` → `"hello "` |
| `rstrip()` | Removes trailing spaces | `" hello ".rstrip()` → `" hello"` |
| `replace(old, new)` | Replaces all occurrences of a substring | `"hello".replace("l", "z")` → `"hezzo"` |
| `split(separator)` | Splits the string into a list | `"a,b,c".split(",")` → `["a", "b", "c"]` |
| `join(iterable)` | Joins elements of an iterable into a string | `",".join(["a", "b", "c"])` → `"a,b,c"` |

---

## String Checking

| Function | Description | Example |
|----------|------------|---------|
| `startswith(prefix)` | Checks if the string starts with a given substring | `"hello".startswith("he")` → `True` |
| `endswith(suffix)` | Checks if the string ends with a given substring | `"hello".endswith("lo")` → `True` |
| `isalpha()` | Checks if all characters are alphabets | `"hello".isalpha()` → `True` |
| `isdigit()` | Checks if all characters are digits | `"123".isdigit()` → `True` |
| `isalnum()` | Checks if all characters are alphanumeric | `"abc123".isalnum()` → `True` |
| `isspace()` | Checks if the string consists only of whitespace | `"   ".isspace()` → `True` |

---

## String Formatting

| Function | Description | Example |
|----------|------------|---------|
| `format()` | Formats strings | `"My name is {}".format("John")` → `"My name is John"` |
| `f-strings` | Modern way to format strings | `name = "John"; f"My name is {name}"` → `"My name is John"` |

---

## String Indexing & Slicing
```python
s = "Hello, World!"
print(s[0])     # 'H'  (First character)
print(s[-1])    # '!'  (Last character)
print(s[0:5])   # 'Hello' (Substring from index 0 to 4)
print(s[::-1])  # '!dlroW ,olleH' (Reversed string)
```

---

## Finding Substrings

| Function | Description | Example |
|----------|------------|---------|
| `find(substring)` | Returns the index of the first occurrence, or `-1` if not found | `"hello".find("l")` → `2` |
| `index(substring)` | Similar to `find()`, but raises an error if not found | `"hello".index("l")` → `2` |
| `count(substring)` | Counts occurrences of a substring | `"hello".count("l")` → `2` |

---

## Contributing
If you find any errors or have suggestions for improvements, feel free to create a pull request!

## License
This project is licensed under the MIT License.

