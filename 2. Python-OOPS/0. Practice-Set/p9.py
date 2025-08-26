"""
Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*'
which adds and multplies them respectively.
"""


class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        real_part = self.r * other.r - self.i * other.i
        imag_part = self.r * other.i + self.i * other.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(2, 3)
c2 = Complex(4, 5)

print(c1 + c2)
print(c1 * c2)
