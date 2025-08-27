<h1 align = center>Advanced Python</h1>

- [Walrus Operator](#walrus-operator)
- [Type Definition](#type-definition)
- [Match Case](#match-case)
- [Useful Features](#useful-features)
- [Exception Handling](#exception-handling)
- [Modules](#modules)
- [List Comprehension](#list-comprehension)
- [Lambda Function](#lambda-function)

## Walrus Operator

- Introduced in Python 3.8, the walrus operator := is also known as the assignment expression.
- It assigns a value to a variable as part of an expression.
- This allows for more concise and readable code by combining assignment and usage in a single line.

#### Basic Purpose

- Previously, you had to separate assignment from checking or using the value.
- With the walrus operator, you can assign and use the value in one step, often simplifying code, especially in loops and conditions.

```
variable := expression
```

- The expression on the right is evaluated, assigned to variable, and then the value is returned.
- It is an expression, not a statement, so it can be used inside other expressions.

## Type Definition

- Type definition means specifying what kind of data a variable, parameter, or return value can hold.
- Python is dynamically typed (variables can reference any type), but modern Python supports type hints / annotations for better code clarity and error checking.

#### Basic Type Hints (Annotations)

- Introduced in Python 3.5 (with typing module), improved in later versions.
- Adds hints to function parameters, return types, and variables.

```
variable_name: type
def func(arg: type) -> return_type
```

#### Type Checking: Static vs. Dynamic

- Python does not enforce type hints at runtime—they are for humans and tools (e.g., mypy, IDEs).
- They help catch mistakes early, document intent, and support smart code completion.

#### Advanced Types: The typing Module

- Add more detail to type definition using typing:
  - List, Dict, Tuple, Set, Optional, Union, Any, Callable, TypeVar, Generic

```
from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and a integer
person: Tuple[str, int] = ("Ashish", 24)

# Dictionary with string keys and integer values
scores : Dict[str, int] = {"Ashish": 24, "Harsh" : 22}

# Union type for vairables that can hold multiple types
identifier : Union[int, str] = "ID123"
identifier = 12345 # Also valid
```

## Match Case

- Introduced in Python 3.10, the match case statement is a form of structural pattern matching.
- It works like a powerful switch/case statement found in other languages, but with more expressive features.
- It matches an expression against patterns and executes code based on the first matching pattern.

#### Basic syntax and notation

```
match subject_expression:
    case pattern1:
        # code block
    case pattern2:
        # code block
    case _:
        # default/fallback case (similar to else)
```

- match evaluates the subject_expression once.
- Each case checks if the pattern matches the subject.
- \_ (underscore) is the wildcard pattern that matches anything (like default or else).

## Useful Features

#### | Operator to Merge Dictionaries

- What It Is
  - Introduced in Python 3.9, the | operator provides a clean and expressive way to merge two dictionaries.
  - It creates a new dictionary combining the keys and values of both, with the right dictionary’s values overriding in case of duplicate keys.

```
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

- Here, key 'b' appears in both. The value from dict2 (3) overrides dict1’s value (2).
- The original dictionaries remain unmodified because | creates and returns a new dict.

#### Multiple Context Managers in a Single with Statement

- What It Is
  - The with statement supports opening multiple context managers simultaneously.
  - Useful for resource management like opening multiple files, ensuring all are properly closed even in case of errors.

```
with open("file1.txt") as file1, open("file2.txt") as file2:
    data1 = file1.read()
    data2 = file2.read()
    # Process data
```

- Both files are opened, and when the with block ends, both file1 and file2 are automatically closed.
- Cleaner and safer than nested with statements

## Exception Handling

- Exception Handling allows a program to deal with runtime errors gracefully without crashing.
- When an error (exception) occurs, Python stops normal execution and raises an exception.
- Using exception handling, you can catch these exceptions and define how your program responds.

#### Basic Syntax: try-except Block

```
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handles division by zero error
    print("Cannot divide by zero!")
```

- If the code inside try raises ZeroDivisionError, the code in except runs instead of program crashing.

#### Catching Multiple Exceptions

```
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

- Different exceptions handled separately for specific errors.

#### Using a Single except for Multiple Exceptions

```
try:
    # code
except (ValueError, ZeroDivisionError):
    print("Caught ValueError or ZeroDivisionError")
```

#### The else clause

- Runs if no exception occurs

```
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number.")
else:
    print(f"You entered: {num}")
```

#### The finally Clause

- Runs always, whether exception occurs or not.
- Useful for cleanup (closing files, releasing resources).

```
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")
```

#### Raising Exceptions

- You can trigger exceptions intentionally.

```
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    print("Access granted")

check_age(16)  # Raises ValueError
```

#### Creating Custom Exception Classes

- Derive from built-in Exception for your own error types:

```
class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot compute square root of negative number")
    return x ** 0.5
```

## Modules

- A module is a Python file (.py) containing definitions (functions, classes, variables) and runnable code.
- Modules help organize code and reuse functionalities across different programs.
- You can import one module into another to use its features.

#### How to Import Modules (Files) into Your Main Python File

- Suppose you have two files:
  - math_utils.py:

  ```
  def add(a, b):
      return a + b
  ```

  - main.py

  ```
  import math_utils
  print(math_utils.add(5, 3))  # Output: 8
  ```

- Import Specific Functions or Classes

  ```
  from math_utils import add
  print(add(10, 20))  # Output: 30
  ```

- Import with Alias

  ```
  import math_utils as mu
  print(mu.add(2, 4))  # Output: 6
  ```

#### The Special Variable: **name** and **main**

- Every Python module has a built-in variable \_\_name\_\_.
- When a file is run directly, Python sets \_\_name\_\_ = "\_\_main\_\_".
- When a file is imported as a module, \_\_name\_\_ is set to the module’s filename (without .py).

- Why Use if \_\_name\_\_ == "\_\_main\_\_":?

  This condition allows parts of the code to run only when the file is executed directly, not when it’s imported.

  ```
  # my_module.py
  def greet():
      print("Hello!")

  if __name__ == "__main__":
      print("Running directly")
      greet()
  ```

  Running directly - Output

  ```
  Running directly
  Hello!
  ```

  Import from another file

  ```
  import my_module
  my_module.greet()
  ```

  Output:

  ```
  Hello!
  ```

## List Comprehension

- List comprehension is a concise way to create lists in Python.
- It offers a shorter syntax compared to using loops to build lists.
- Enhances readability and often results in more efficient code.

#### Basic Syntax and Notation

```
[expression for item in iterable]
```

- expression: The value or operation applied to each item.
- for item in iterable: Looping over items from any iterable object (list, tuple, range, etc.).

#### Basic Example

- Create a list of squares for numbers 0 to 4:

```
# Using Loop
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)  # Output: [0, 1, 4, 9, 16]

# Using List Comprehension
squares = [i**2 for i in range(5)]
print(squares)
```

#### List Comprehension with Condition (Filtering)

```
[expression for item in iterable if condition]
```

- Example: squares of even numbers from 0 to 9:

```
squared = [x**2 for x in range(11) if x % 2 == 0]
print(squared)
```

## Lambda Function

- A lambda function is a small anonymous function defined with the lambda keyword.
- It can have any number of arguments, but only one expression.
- The expression is evaluated and returned automatically.
- Used for short, simple functions without formally defining a full function using def.

#### Basic syntax and Notation

```
lambda arguments: expression
```

- arguments: zero or more inputs separated by commas.
- expression: single expression evaluated and returned.

#### Simple Lambda Function

```
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

- Equivalent regular function

```
def add(x, y):
    return x + y

print(add(2, 3))  # Output: 5
```

#### Limitations of Lambda Functions

- Limited to a single expression (no statements or multiple expressions).
- Less readable for complex logic.
- No function name (anonymous), less descriptive in tracebacks or debugging.

#### When to Use Lambda Functions?

- For quick, small functions used temporarily.
- When passing functions as arguments (callbacks, sorting keys, etc.).
- To avoid boilerplate code of defining full functions for simple operations.
