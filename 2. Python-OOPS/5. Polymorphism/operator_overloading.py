print("Operator overloading")

"""
class Number:
    def __init__(self, n):
        self.n = n


n = Number(2)
m = Number(3)
# print(n + m) >> This will throw an error because addition is a class which can only be accessed through
operator overloading
"""


# Example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the '+' operator
    def __add__(self, other):
        return self.x + other.x, self.y + other.y


p1 = Point(5, 4)
p2 = Point(7, 6)
print(p1 + p2)
# Here, when p1 + p2 is called, Python runs p1.__add__(p2), returning a new Point


# Another Example
class Box:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return self.a < other.a

    def __eq__(self, other):
        return self.a == other.a


b1 = Box(10)
b2 = Box(20)
print(b1 < b2)
print(b1 == b2)
# When b1 < b2 is used, Python invokes b1.__lt__(b2)


# List merging Example
class listAdd:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


list1 = listAdd([4, 5])
list2 = listAdd([5, 4])
print(list1 + list2)


# String concatenation example
class InputString:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name


fname = InputString("Ashish")
lname = InputString(" Khanagwal")
print(fname + lname)
