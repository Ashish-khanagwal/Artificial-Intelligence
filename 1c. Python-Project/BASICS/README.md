<h1 align=center>LEARNING FROM PROJECTS</h1>

- [Map](#map)
- [Zip](#zip)
- [Join](#join)
- [File data into list](#file-data-into-list)
- [File Handling](#file-handling)

## map

#### What is map()?

- map() is a built-in Python function that applies a given function to every item in an iterable (like a list, tuple, etc.).
- It returns an iterator that produces the results of applying the function to each element.

```
Syntax:
map(function, iterable, ...)
```

- `function:` A function that takes as many arguments as there are iterables.
- `iterable:` One or more iterable objects (e.g., lists, tuples).

#### How does map() work?

- It calls the provided function on each item from the iterable(s) and produces an iterator of the results.
- You often convert this iterator to a list or iterate through it using a loop.

#### When to use map()?

- When needing to transform all items in an iterable by applying the same operation or function.
- When you want to apply one function to all elements easily without writing an explicit loop.
- It can make code more elegant, concise, and sometimes more efficient.

#### Examples:

1. Square all numbers in a list

```
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
```

2. Using a lambda for inline function

```
numbers = [1, 2, 3, 4, 5]

squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
```

3. Applying a function to multiple iterables

```
a = [1, 2, 3]
b = [4, 5, 6]

summed = map(lambda x, y: x + y, a, b)
print(list(summed))  # Output: [5, 7, 9]
```

#### Important notes:

- map() returns an iterator in Python 3, so you can only iterate through it once unless you convert it to a list or tuple.
- Using map() with built-in functions like str, int, etc., can be very useful:

## zip

#### What is zip()?

- zip() is a built-in Python function that aggregates elements from multiple iterables (like lists, tuples) into tuples, pairing elements by their position.
- It produces an iterator of tuples, where each tuple contains the i-th element from each iterable.

```
Syntax:
zip(iterable1, iterable2, ...)
```

- Takes two or more iterables as arguments.

#### How does `zip()` work?

- It pairs elements from each iterable in order.
- Stops creating tuples when the shortest iterable is exhausted.
- Returns an iterator of tuples.

#### When to use `zip()?`

- When you want to combine multiple iterables element-wise.
- Useful in loops when you wish to iterate over two or more lists in parallel.
- Great for pairing keys and values or merging data sets.

#### Examples:

1. Basic example with two lists

```
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

paired = zip(names, ages)
print(list(paired))
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

2. Iterating in parallel

```
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Output:
# Alice is 25 years old.
# Bob is 30 years old.
# Charlie is 35 years old.
```

3. Different length iterables

```
a = [1, 2, 3]
b = ['a', 'b']

print(list(zip(a, b)))
# Output: [(1, 'a'), (2, 'b')]
# Stops at the shortest iterable length (2)
```

4. Unzipping

- You can also unzip zipped lists back to separate lists using the \* operator:

```
pairs = [('John', 22), ('Jane', 28)]
names, ages = zip(*pairs)

print(names)  # ('John', 'Jane')
print(ages)   # (22, 28)
```

#### Important notes:

- The result of zip() is an iterator; convert it to list/tuple to reuse or print.
- Works with any iterables (not just lists), such as strings, tuples, sets.
- For unequal length iterables, it truncates to shortest by default. Use itertools.zip_longest if you want to pad instead.

## join

#### What is "".join()?

- join() is a string method used to concatenate a sequence (like a list or tuple) of strings into a single string, with the string it is called on inserted between each element.
- The string before .join() acts as the separator between the joined elements.

```
Syntax:
separator_string.join(iterable_of_strings)
```

- The `iterable_of_strings` is an iterable containing strings to combine.
- `separator_string` is the string placed between elements during joining.

#### How does it work?

- It takes all the strings in the iterable and concatenates them into one continuous string.
- Between each adjacent pair of strings, it inserts the separator string.

#### When to use "".join()?

- To efficiently combine multiple strings into one.
- Preferred over repeatedly using + for strings, because it is faster and more memory-efficient.
- Useful for building strings when you have a list or another iterable of strings.

#### Examples:

1. Join list of words with a space

```
words = ['Hello', 'world', 'Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence)  # Output: Hello world Python is fun
```

2. Join with no separator

```
chars = ['H', 'e', 'l', 'l', 'o']
word = "".join(chars)
print(word)  # Output: Hello
```

3. Join with comma separator

```
items = ['apple', 'banana', 'cherry']
result = ", ".join(items)
print(result)  # Output: apple, banana, cherry
```

#### mportant notes:

- The iterable must contain only strings; otherwise, join() will raise a TypeError.
- To join a list of non-string items (e.g., numbers), convert them to strings first using map(str, iterable):

```
numbers = [1, 2, 3]
number_str = ", ".join(map(str, numbers))
print(number_str)  # Output: 1, 2, 3
```

## File data into list

#### What does it mean?

- When you read a file's contents into a list, you typically load each line of the file as an individual string element of that list.
- This makes it easy to work with lines individually for processing, editing, or analysis.

#### How to store file data in a list?

- The common way is to use the readlines() method of a file object:

```
with open("filename.txt", "r") as file:
    lines = file.readlines()
```

- lines will be a list of strings, one for each line including newline characters (\n).
- Example:
- Assume a file example.txt contains:

```
Hello world
This is a file
With multiple lines
```

- Reading it into a list:

```
with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)
# Output: ['Hello world\n', 'This is a file\n', 'With multiple lines\n']
```

#### Why store lines in a list?

- Process lines individually: You can loop through lines and modify or analyze each line separately.
- Easy editing: Modify certain lines then write all back to the file.
- Manipulate data structure: Insert, delete, or rearrange lines as list elements.

#### Removing trailing newlines while storing lines

- To avoid newline characters (\n), you can strip them:

```
with open("example.txt", "r") as file:
    lines = [line.rstrip('\n') for line in file]
```

- This keeps lines clean from extra newlines when processing.

#### Writing the list back to a file

- After modifying the list, you can write it back using:

```
with open("example.txt", "w") as file:
    file.writelines(lines)
```

# File Handling

## Correct vs Incorrect Methods for Storing File Lines in a List

### WRONG APPROACH

```
# CODE

for line in lines:
    line = line.strip("\n")
    data = list(line)   # converts line string to list of characters!
    print(data)
```

#### What happens:

- For each line, stripping the newline is fine.
- But then list(line) converts the string line into a list of its characters, splitting it character-by-character.
- So instead of a list of lines, you get a list of characters for each line printed separately.

```
# OUTPUT

['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'f', 'i', 'l', 'e']
['W', 'i', 't', 'h', ' ', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', ' ', 'l', 'i', 'n', 'e', 's']
```

#### Why this is wrong for your use case:

- You wanted to store whole lines as elements, but instead you stored each character of a line as a separate list element, losing the line structure.

### RIGHT APPROACH

```
# CODE

with open("example.txt") as file:
    lines = file.readlines()
    data = []
    for line in lines:
        line = line.strip("\n")  # Remove trailing newline
        data.append(line)        # Append whole line as a string
        print(line)
print(data)
```

#### What happens:

- Reads all lines into lines (each ending with \n).
- Strips the newline character from each line using .strip("\n").
- Appends the entire cleaned line as a single string to data.
- Prints each full line.
- data becomes a list of full lines as strings.

```
# OUTPUT

Hello world
This is a file
With multiple lines
['Hello world', 'This is a file', 'With multiple lines']
```

#### Why this is right:

- You want each element of data to be a full line string, not broken down into characters.

## General Approach to Store Key-Value Pairs from File Lines in Python

### 1. Identify a delimiter

- Usually, key-value pairs have a delimiter separating them, e.g., :, =, ->, or tabs.
- Examples:

```
key:value
key = value
name -> John Doe
```

- You need to define or detect the delimiter before splitting.

### 2. Splitting and stripping reliably

- Use .split(delimiter, 1) to split line into two parts — key and value.
- Use .strip() on both to remove unwanted whitespace.

```
delimiter = ':'  # or '=', '->', '\t', etc.

with open("file.txt", "r") as file:
    data = {}
    for line in file:
        if delimiter in line:
            key, value = line.split(delimiter, 1)
            key = key.strip()
            value = value.strip()
            data[key] = value
```

### 3. When delimiter is unknown or lines have no delimiter

- You can detect delimiter dynamically based on common candidates:

```
possible_delimiters = [":", "=", "->", "\t"]

with open("file.txt", "r") as file:
    data = {}
    for line in file:
        for delim in possible_delimiters:
            if delim in line:
                key, value = line.split(delim, 1)
                data[key.strip()] = value.strip()
                break
        else:
            # No delimiter found, maybe store whole line as key or ignore
            print(f"No delimiter found in line: {line.strip()}")
```

### 4. If file structure is more complex (e.g., JSON, CSV, INI files) use specialized parsers

- For JSON: use json module.
- For CSV: use csv.DictReader.
- For INI: use configparser.

### 5. first space character `" "`

```
with open("file.txt", "r") as file:
    data = {}
    for line in file:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        if " " in line:
            key, value = line.split(" ", 1)
            data[key.strip()] = value.strip()
        else:
            # No space found - could treat whole line as key or value
            data[line] = None  # or data[line] = "" depending on your need
```

#### Explanation:

- `.split(" ", 1)` splits at the first space only, resulting in two parts:
- key: text before the first space
- value: rest of the line after the first space (including additional spaces)
- This works well for lines like:

```
task1 Do the laundry today
username JohnDoe123
```

- `"task1"` and `"username"` are keys, `"Do the laundry today"` and `"JohnDoe123"` are values.
