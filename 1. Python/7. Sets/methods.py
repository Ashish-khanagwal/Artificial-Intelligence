a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a)
print(b)
# Set Operations (Mathematical)
print("a union b is: {}".format(a | b))  # -> a union b
print("a intersection b is: {}".format(a & b))  # -> a intersection b
print("a - b is: {}".format(a - b))  # -> Difference
print("b - a is: {}".format(b - a))
print(a ^ b)  # -> symmetric difference

# Set Methods
a.union(b)
print(a)

a.intersection_update(b)
print(a)

a.symmetric_difference_update(b)
print(a)

# Frozen set
frozen = frozenset([1, 2, 3])
# frozen.add(5) --> It will give an error, as the set is frozen so not mutable.
