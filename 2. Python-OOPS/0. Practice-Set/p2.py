# Write a class "Calculator" capable of finding square, cube and square root of a number.


class Calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n**2}")

    def cube(self):
        print(f"The cube is {self.n**3}")

    def square_root(self):
        print(f"The square root is {round(self.n**(1/2), 3)}")


number = Calculator(4)
number.square_root()
number.square()
number.cube()
