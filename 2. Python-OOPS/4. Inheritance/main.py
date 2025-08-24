print("***" + "*" * 24 + "***")
print("*" + "Inheritance".center(28) + "*")
print("***" + "*" * 24 + "***")


# Basic Implementation of Inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


animal = Animal()
animal.sound()  # Output: Animal makes a sound

dog = Dog()
dog.sound()  # Output: Dog barks (overridden method)

# Another Example


class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting...")

    def stop(self):
        print("Vehicle is stoping...")


class Car(Vehicle):

    def __init__(self, brand, model, year, no_of_wheels, no_of_doors):
        super().__init__(brand, model, year)
        self.no_of_wheels = no_of_wheels
        self.no_of_doors = no_of_doors


class Bike(Vehicle):

    def __init__(self, brand, model, year, no_of_wheels):
        super().__init__(brand, model, year)
        self.no_of_wheels = no_of_wheels


car = Car("Ford", "Focus", 2008, 4, 4)
print(car.__dict__)
car.start()
bike = Bike("BMW", "Blue", 2011, 2)
print(bike.__dict__)
bike.start()
