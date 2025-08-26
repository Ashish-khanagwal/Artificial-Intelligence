"""
Write __str__() method to print the vector as follows:
7i + 8j + 10k
"""


class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        result = Vector(self.a + other.a, self.b + other.b, self.c + other.c)
        return result

    def __mul__(self, other):
        result = self.a * other.a + self.b * other.b + self.c * other.c
        return result

    def __str__(self):
        return f"({self.a}i + {self.b}j + {self.c}k)"


# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50
