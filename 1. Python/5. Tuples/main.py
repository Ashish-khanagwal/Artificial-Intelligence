line = "***********************"
print(line)
print("Tuples".center(22))
print(line)

# Tuples is a ordered, immutable collection of items.
mytuple = tuple((1, "Ashish", 3.141, "Khanagwal", True))
print(mytuple)
print(type(mytuple))

# To create a one item tuple, we must add a comma at the end
oneitem = ("Ashish",)  # --> Tuple
item = "Ashish"  # --> String (without comma)
print(type(oneitem))
print(type(item))

# Converting into a list and then adding a item.
mylist = list(mytuple)
mylist.append(
    "Manish",
)
newtuple = tuple(mylist)
print(newtuple)

# Packing a tuple
anothertuple = 1, "Python", 69, 3.141
print(anothertuple)

# Unpacking a tuple
a, b, *c = anothertuple
print(a)
print(b)
print(c)
