"""
Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates
the sum and dot(.) product of them.
"""


class Vector:
    def __init__(self, components):
        self.components = components

    def show(self):
        print(f"The vector is {', '.join(map(str, self.components))}")

    def __add__(self, other):
        result = [a + b for a, b in zip(self.components, other.components)]
        return result

    def __mul__(self, other):
        result = [a * b for a, b in zip(self.components, other.components)]
        return result

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"


dim = input("Enter the dimension of the vector: ")
values = input(f"Enter the {dim} components separated by space: ").split()
components = [int(v) for v in values]

v1 = Vector(components)
v1.show()

values2 = input(f"Enter the {dim} components separated by space: ").split()
components2 = [int(v) for v in values2]

v2 = Vector(components2)
v2.show()
print(v1 + v2)
print(v1 * v2)
