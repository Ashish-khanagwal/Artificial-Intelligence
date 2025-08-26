class Calculator:

    def __init__(self, a):
        self.a = a

    def square(self):
        print(f"The square of {self.a} is {self.a**2}")

    def cube(self):
        print(f"The cube of {self.a} is {self.a**3}")

    def square_root(self):
        print(f"The square root of {self.a} is {round(self.a**(1/2))}")

    @staticmethod
    def greet(user):
        return f"Hello {user}"


demo = Calculator(4)
demo.square()
demo.cube()
demo.square_root()
print(Calculator.greet("Ashish"))
