<h1 align=center>LEARNING FROM PROJECTS</h1>

- [Map](#map)
- [Zip](#zip)
- [Join](#join)
- [File data into list](#file-data-into-list)
- [File Handling](#file-handling)
- [Updating Keys and Values](#updating-keys-and-values)
- [Understanding CSV File](#understanding-csv-file)
- [Password Masking](#password-masking)
- [Password Validation](#password-validation)
- [List Concatenation](#list-concatenation)

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

## Updating Keys and Values

### Overview

A Python dictionary (dict) stores key-value pairs—unique keys mapped to corresponding values. Updating a dictionary involves changing existing keys, their values, or both.

### 1. Updating a Value for an Existing Key

- You can directly assign a new value to a key.
- If the key exists, its value is replaced.
- If the key doesn’t exist, a new key-value pair is created.

```
my_dict = {'name': 'Alice', 'age': 25}
my_dict['age'] = 26  # Updates existing 'age'
my_dict['city'] = 'New York'  # Adds new key 'city'

print(my_dict)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
```

### 2. Updating Multiple Key-Value Pairs

- Use the .update() method to update/add many pairs at once from another dictionary or iterable of key-value pairs.

```
my_dict = {'name': 'Alice', 'age': 25}
updates = {'age': 26, 'city': 'New York'}
my_dict.update(updates)

print(my_dict)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
```

### 3. Changing a Key (the Key Itself)

- Dictionaries do not support direct key renaming because keys are immutable.
- To "rename" a key:
  - Add a new key with the value of the old key.
  - Delete the old key.

```
my_dict = {'name': 'Alice', 'age': 25}

# Rename key 'name' to 'first_name'
my_dict['first_name'] = my_dict.pop('name')

print(my_dict)
# Output: {'age': 25, 'first_name': 'Alice'}
```

### 4. Modifying Both Keys and Values

- Since keys must be unique and immutable, changing keys involves reassigning.
- Values can be directly edited.

For multiple key changes:

```
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {}

for k, v in my_dict.items():
    new_key = k.upper()  # Example: change key to uppercase
    new_value = v * 10   # Example: modify value
    new_dict[new_key] = new_value

print(new_dict)
# Output: {'A': 10, 'B': 20, 'C': 30}
```

### 5. Important Points

- Keys must be immutable types (strings, numbers, tuples); you cannot modify keys in place.
- Values can be any type and freely updated.
- Use .pop(key) to remove a key while retrieving its value.
- .update() can merge two dictionaries and overwrite existing keys.
- Be mindful of dictionary size—modifying keys usually means creating a new dictionary or restructuring.

Example function to rename a key and update its value:

```
def rename_key_and_update_value(d, old_key, new_key, new_value):
    if old_key in d:
        d[new_key] = new_value
        if new_key != old_key:
            del d[old_key]
    else:
        print(f"Key {old_key} not found!")

my_dict = {'name': 'Alice', 'age': 25}
rename_key_and_update_value(my_dict, 'name', 'first_name', 'Bob')
print(my_dict)
# Output: {'age': 25, 'first_name': 'Bob'}
```

## Understanding CSV File

### What are csv.DictReader and csv.DictWriter?

- They are classes from Python’s built-in csv module that read and write CSV files using dictionaries instead of plain lists.
- Each row is handled as a dictionary where keys are column headers and values are the respective cell values.

### Why use DictReader and DictWriter over csv.reader and csv.writer?

#### 1. Readability and Convenience

- With DictReader, you access columns by header names (keys) rather than numeric indexes, which makes code easier to read and maintain.

Example with csv.reader (using indexes):

```
import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        print(row[0], row[2])  # Access columns by index (e.g., name, age)
```

Versus DictReader (using keys):

```
import csv

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Age'])  # Use column headers
```

#### 2. Robustness to Column Order

- DictReader does not rely on the order of columns in the CSV file, only on the column headers.
- Safer when column order may change or files come from varying sources.

#### 3. Writing CSV with Column Labels

- DictWriter writes rows as dictionaries, automatically placing values under the correct header column.
- You specify the fieldnames (columns) once, then write rows keyed by headers.

Example:

```
import csv

fieldnames = ['Name', 'Age']
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 30})
    writer.writerow({'Name': 'Bob', 'Age': 25})
```

Without DictWriter, writing requires managing columns by position explicitly.

#### 4. Easier Data Manipulation

- When reading, DictReader gives you a dictionary of values, which is often easier to use with other data structures or business logic.
- When writing, providing data as dictionaries is natural for many applications.

#### Things to Know When Using DictReader and DictWriter

- Header row is required: DictReader reads the first line as the header by default.
- If your CSV has no header, you can provide fieldnames manually:

```
reader = csv.DictReader(f, fieldnames=['col1', 'col2', 'col3'])
```

- When writing with DictWriter, make sure the keys in your data match the fieldnames.
- Use newline='' when opening files for writing to avoid extra blank lines on some platforms.
- They work well with Unicode and different encodings (open file with correct encoding).

## Password Masking

```
password = "mypassword123"
secret_password = "*" * len(password)
print(secret_password)  # Output: *************
```

#### What does this do?

- It creates a masked version of a password by replacing each character with an asterisk (\*).
- The number of asterisks equals the length of the original password, showing the length but hiding the actual characters.

#### How does it work?

- len(password) calculates the number of characters in the password string.
- The _ operator with strings performs repetition, creating a new string with the asterisk (_) repeated that many times.

#### Why use this?

- To hide sensitive information like passwords when displaying them on a screen or logging.
- Shows the length of the password without revealing the actual characters.
- Useful in UI or console programs to confirm input was received without exposing secrets.

## Password Validation

```
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)
```

#### These lines check whether a password contains at least one character of each category:

- Uppercase letter
- Lowercase letter
- Digit (0-9)
- Special character (punctuation marks)

#### How does it work?

- any() is a built-in function that returns True if any element of the iterable is truthy.
- c.isupper(), c.islower(), c.isdigit() are string methods that return True if the character c matches that type.
- string.punctuation is a constant string containing all special punctuation characters, such as !@#$%^&\*(), etc.
- The expressions use generator comprehensions to efficiently check every character c in password without building intermediate lists.

#### Step-by-step:

- any(c.isupper() for c in password): Checks if any character in password is uppercase.
- any(c.islower() for c in password): Checks if any character in password is lowercase.
- any(c.isdigit() for c in password): Checks if any character in password is a digit.
- any(c in string.punctuation for c in password): Checks if any character is a special symbol.

Example:

```
import string

password = "MyP@ssw0rd"

has_upper = any(c.isupper() for c in password)     # True ('M', 'P')
has_lower = any(c.islower() for c in password)     # True ('y', 's', 's', 'w', 'r', 'd')
has_digit = any(c.isdigit() for c in password)     # True ('0')
has_special = any(c in string.punctuation for c in password)  # True ('@')

print(has_upper, has_lower, has_digit, has_special)
# Output: True True True True
```

#### Why use this in projects?

- To enforce strong password policies by ensuring passwords have diverse character types.
- Efficient and readable way to validate password complexity.
- Using any() and generator expressions is memory-efficient as it stops checking as soon as it finds a matching character.

## List Concatenation

### What does `list = c_alpha + l_alpha + num + s_char` mean?

- This expression joins multiple lists into a single list by using the + operator.
- The + operator for lists performs list concatenation, i.e., it combines all elements from each list into a new list.

#### How does it work?

Suppose you have multiple lists:

```
c_alpha = ['A', 'B', 'C']        # Capital letters
l_alpha = ['a', 'b', 'c']        # Lowercase letters
num = ['1', '2', '3']            # Numbers as strings
s_char = ['!', '@', '#']         # Special characters
```

Using + to concatenate:

```
combined_list = c_alpha + l_alpha + num + s_char
print(combined_list)
# Output: ['A', 'B', 'C', 'a', 'b', 'c', '1', '2', '3', '!', '@', '#']
```

- A new list combined_list is created containing all elements of the given lists in order.

#### Important aspects:

- Order matters: Elements are added in the order of lists.
- The original lists remain unchanged.
- `+` creates a new list, so if the original lists are long, this can impact memory.

#### Alternative ways:

Using list.extend() method to modify one list in-place:

```
c_alpha.extend(l_alpha)
c_alpha.extend(num)
c_alpha.extend(s_char)
print(c_alpha)
# Same combined contents, but original c_alpha modified
```

Using list comprehension or unpacking (Python 3.5+):

```
combined = [*c_alpha, *l_alpha, *num, *s_char]
```

#### Why join lists like this?

- Useful for combining character sets when building password pools.
- Combines data from different sources into one for processing.
- Makes iteration over multiple groups simpler.
