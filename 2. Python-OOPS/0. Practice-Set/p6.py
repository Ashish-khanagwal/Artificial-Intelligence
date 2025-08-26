"""
Create a class (2-D Vector) and use it to create another class representig a 3-D vector.
"""


class TwoVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        return f"The vector is {self.i} and {self.j}"


class ThreeVector(TwoVector):
    def __init__(self, vec1, k):
        super().__init__(vec1.i, vec1.j)
        self.k = k

    def show(self):
        base_str = super().show()  # Get string from TwoVector's show
        return f"{base_str} and {self.k}"


vector1 = TwoVector(2, 4)
print(vector1.show())
vector2 = ThreeVector(vector1, 6)
print(vector2.show())
