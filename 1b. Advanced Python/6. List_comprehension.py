# Basic Example

# Using Loop
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)  # Output: [0, 1, 4, 9, 16]

# Using List Comprehension
squares = [i**2 for i in range(5)]
print(squares)


# List comprehension with conditions
squared = [x**2 for x in range(11) if x % 2 == 0]
print(squared)
