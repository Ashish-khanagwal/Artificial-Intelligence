line = "*************************"
print(line)
print("Sets".center(23))
print(line)

# Sets are unordered, mutable collection of unique itmes, it means no duplicate values are allowed.

fruits = {"apple", "banana", "orange"}
nums = set((1, 2, 3, 4, 5))

print(fruits)
print(nums)
print(type(fruits))
print(type(nums))
print(len(fruits))
print(len(nums))

# Empty set
empty_set = set()
# not_a_set = {} # This is not a set, instead it is a empty dictionary.

# No duplicate values are allowed
nums.add(
    2
)  # --> Addind 2 won't give an error but instead, it will be ignored as it is a duplicate
print(nums)

# True is a dupe of 1 and False is a dupe of zero.
nums = {1, True, 4, 3, False, 2, 0}
print(nums)

# Check if a value exists in set or not
print(0 in nums)

# But we cannot refer to an element in the set with an index position or a key, as it is unordered.

# Accessing the element
for i in nums:
    print(i)

# Adding element or updating the set

print("Original set of fruits: {}".format(fruits))

fruits.add("Mango")  # -> To add a single element
fruits.update(["Pineappple", "Grapes", "kiwi"])  # -> To add multiple elements in a set

print("Set of fruits after updating or adding elements to it: {}".format(fruits))

# Removing the elements
fruits.remove("apple")  # -> removes the element, error if not found.
print("On using remove method: {}".format(fruits))
fruits.discard("Mango")  # -> removes the element, no error if not found.
print("On using discard method: {}".format(fruits))
fruits.pop()  # -> removes a random element
print("On using pop method: {}".format(fruits))
fruits.clear()  # -> removes all elements
print("On using clear method: {}".format(fruits))
