# Example


class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 5)

print(rect1 > rect2)
print(rect1 == rect2)

# Reflected (reverse)  Methods


class Vector:

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x)
        return Vector(self.x + other)

    def __radd__(self, other):
        return Vector(self.x + other)

    def __repr__(self):
        return f"Vector({self.x})"


v = Vector(95)

print(v + 5)
print(5 + v)


# Chaining Operator Overload
class Num:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Num(self.value + other.value)

    def __mul__(self, other):
        return Num(self.value * other.value)


a = Num(10)
b = Num(2)
c = Num(8)
result = a + b * c
print(result.value)
