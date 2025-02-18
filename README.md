# Python Data Structures: Lists, Tuples, Sets, and Dictionaries

This repository provides an overview of the four fundamental data structures in Python: **Lists**, **Tuples**, **Sets**, and **Dictionaries**. Each data structure has unique properties and use cases, making them essential tools for organizing and manipulating data in Python.

---

## Table of Contents
1. [Lists](#lists)
2. [Tuples](#tuples)
3. [Sets](#sets)
4. [Dictionaries](#dictionaries)
5. [Summary](#summary)

---

## Lists
A **list** is an **ordered**, **mutable** (changeable), and **heterogeneous** (can hold different types of data) collection of items. Lists are one of the most commonly used data structures in Python.

### Key Features:
- Created using square brackets `[]`.
- Can contain integers, floats, strings, booleans, other lists, or mixed data types.
- Supports operations like appending, removing, slicing, and more.

### Example:
```python
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Add an element
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

---

## Tuples
A **tuple** is an **ordered**, **immutable** (unchangeable), and **heterogeneous** collection of items. Tuples are similar to lists but cannot be modified after creation.

### Key Features:
- Created using parentheses `()`.
- Can contain integers, floats, strings, booleans, other tuples, or mixed data types.
- Useful for storing fixed data that should not be changed.

### Example:
```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Access the first element: Output: 1
```

---

## Sets
A **set** is an **unordered**, **mutable**, and **unique** collection of items. Sets do not allow duplicate values and are useful for operations like union, intersection, and difference.

### Key Features:
- Created using curly braces `{}` or the `set()` function.
- Can contain integers, floats, strings, booleans, or tuples (but not lists or other sets).
- Automatically removes duplicate values.

### Example:
```python
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Add an element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
```

---

## Dictionaries
A **dictionary** is an **unordered**, **mutable**, and **key-value pair** collection of items. Dictionaries are optimized for retrieving values based on unique keys.

### Key Features:
- Created using curly braces `{}` with key-value pairs.
- Keys must be unique and immutable (e.g., strings, numbers, or tuples).
- Values can be of any data type, including lists, sets, or other dictionaries.

### Example:
```python
my_dict = {'apple': 4, 'banana': 10, 'orange': 8}
my_dict['banana'] = 12  # Update a value
print(my_dict)  # Output: {'apple': 4, 'banana': 12, 'orange': 8}
```

---

## Summary
| Data Structure | Ordered | Mutable | Duplicates Allowed | Key-Value Pairs | Use Case |
|----------------|---------|---------|---------------------|-----------------|----------|
| **List**       | Yes     | Yes     | Yes                 | No              | Storing ordered, changeable collections |
| **Tuple**      | Yes     | No      | Yes                 | No              | Storing fixed, unchangeable collections |
| **Set**        | No      | Yes     | No                  | No              | Storing unique, unordered collections |
| **Dictionary** | No      | Yes     | Keys: No, Values: Yes | Yes             | Storing key-value pairs for fast lookups |

---

## How to Use This Repository
1. Clone the repository:
   ```bash
   git clone https://github.com/henrymbuguak/python-data-structure.git
   ```
2. Navigate to the repository:
   ```bash
   cd python-data-structures
   ```
3. Explore the examples and code snippets provided for each data structure.

---

## Contributing
If you have suggestions, improvements, or additional examples, feel free to open an issue or submit a pull request. Contributions are welcome!

---

Happy coding! 🚀