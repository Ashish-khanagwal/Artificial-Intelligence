line = "*******************"
print(line)
print("Enumerate".center(20))
print(line)

# enumerate() is a built-in Python function that helps you loop over a sequence (like a list or string) and get both the index (position) and the value (item) in each iteration.

fruits = ["Apple", "banana", "grapes", "pineapple", "peach"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\n")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
