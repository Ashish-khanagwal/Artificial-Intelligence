print("***" + "*" * 14 + "***")
print("*" + "Basics".center(18) + "*")
print("***" + "*" * 14 + "***")


# Basic Version
class Dog:
    def bark(self):
        print("Woof Woof")


dog1 = Dog()
dog1.bark()

print("")


class Cat:
    def __init__(self, name, age):  # --> Constructor Method
        self.name = name  # --> Attributes
        self.age = age

    def meow(self):
        print(f"{self.name} is meowing...")


cat1 = Cat("Kitty", 4)
cat1.meow()
