# Python Basics

This document covers the fundamentals of Python programming with definitions, syntax, and examples for each topic.

---

## 1. Basics
Python is a high-level, interpreted programming language known for its readability and simplicity.

**Example:**
```python
print("Hello, World!")
```

---

## 2. Data Types
Python supports several built-in data types:
- int (Integer)
- float (Floating point)
- str (String)
- bool (Boolean)
- complex (Complex number)

**Syntax & Example:**
```python
x = 10          # int
y = 3.14        # float
name = "Ashish" # str
is_dev = True   # bool
z = 2 + 3j      # complex

print(type(x), type(y), type(name), type(is_dev), type(z))
```

---

## 3. User Input
Takes input from the user using `input()` function.

**Syntax & Example:**
```python
name = input("Enter your name: ")
print("Hello,", name)
```

---

## 4. Lists
Lists are ordered, mutable collections.

**Syntax & Example:**
```python
my_list = [1, 2, 3, "apple"]
my_list.append(4)
print(my_list)
```

---

## 5. Tuples
Tuples are ordered, immutable collections.

**Syntax & Example:**
```python
my_tuple = (1, 2, 3, "apple")
print(my_tuple[0])
```

---

## 6. Dictionaries
Dictionaries store key-value pairs.

**Syntax & Example:**
```python
my_dict = {"name": "Ashish", "age": 22}
print(my_dict["name"])
my_dict["age"] = 23
```

---

## 7. Sets
Sets are unordered collections of unique elements.

**Syntax & Example:**
```python
my_set = {1, 2, 3, 3, 4}
print(my_set)  # duplicates removed
my_set.add(5)
```

---

## 8. Loops
Used for iteration.

**For Loop Example:**
```python
for i in range(5):
    print(i)
```

**While Loop Example:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 9. Functions
Reusable blocks of code.

**Syntax & Example:**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Ashish"))
```

---

## 10. Recursion
A function calling itself.

**Example:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

## 11. File I/O
Used to read and write files.

**Syntax & Example:**
```python
# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, File!")

# Reading from a file
with open("example.txt", "r") as f:
    print(f.read())
```

---

## 12. Enumerate
Enumerate adds a counter to an iterable.

**Syntax & Example:**
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

---

✅ This document serves as a quick reference guide for Python basics.
