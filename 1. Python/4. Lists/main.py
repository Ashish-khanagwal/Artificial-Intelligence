line = "***********************"
print(line)
print("Lists".center(23))
print(line)

# List is mutable, ordered, and can store mixed data types.
fruits = [
    "Apple",
    "Banana",
    "mango",
    "Grapes",
    "Strawberry",
    "Pineapple",
    "Guvava",
    "Dragonfruit",
]
print(fruits)

print(fruits[1])
mixed = ["Ashish", 24, 1, 1.79]
print(mixed[2])
print(mixed[-1])
print("Ashish" in mixed)

print(fruits.index("Pineapple"))

# Slicing in lists
print(fruits[1:4])

num = ["Ashish", 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(num[5])
print(num.index(16))
print(num[2:7])

# Changing the item
fruits[2] = "Peach"
print(fruits)
print(len(fruits))
print("")

# Append -> Add item at the end
fruits.append("Orange")
print(fruits)
print(len(fruits))
print("")

# Add item at a specific index
fruits.insert(2, "pomegranate")
print(fruits)
print(len(fruits))
print("")

# Extend -> to add multiple items
fruits.extend(["Watermelon", "blueberry"])
print(fruits)
print(len(fruits))

fruits.extend(num)
print(fruits)
print(len(fruits))
