line = "******************************"
print(line)
print("Dictionaries".center(30))
print(line)

# A dictionary in python is unordered, mutable collection of key-value pairs.
# Ways to create Dictonaries
user1 = {"firstname": "Ashish", "lastname": "Khanagwal", "age": 24, "height": 1.77}

user2 = dict(firstname="Manish", lastname="Kumar Gupta", age=23, height=1.67)

print(user1)
print(user2)
print(len(user1))
print(type(user1))

# Accessing the values
print(user1["firstname"])

# get() is safer, it returns None instead of error if the key doesn't exist
print(user1.get("lastname"))

# List all the keys
print(user1.keys())

# List all the values
print(user1.values())

# List all the key-value pairs as tuples
print(user1.items())

print("firstname" in user1)
print("age" in user1)

# Changing the values
user1["age"] = 25  # --> Modifies the valye of the key
user1["city"] = "Delhi"  # --> Adds new key-value pair at the last
user1.update({"Profession": "Engineer"})
print(user1)
print("")

# Removing items
user1.pop("city")  # --> Removes value with key
print("City element is removed: {}".format(user1))
print("")

user1.popitem()  # --> Removes the last inserted key-value pair
print("Last element of the dict is removed: {}".format(user1))
print("")

del user1["lastname"]  # --> deletes the mentioned key-value pair
print(user1)

# Looping through a dictionary

# Keys and Values
for key in user1:
    print(key, user1[key])

# Only values
for value in user1.values():
    print(value)

# Key-value pairs
for key, value in user1.items():
    print(key, value)
