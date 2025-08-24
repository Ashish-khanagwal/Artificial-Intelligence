print("***" + "*" * 24 + "***")
print("*" + "Abstraction".center(28) + "*")
print("***" + "*" * 24 + "***")

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method - no implementation


class Dog(Animal):
    def sound(self):
        print("Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


# animal = Animal()  # Error: Can't instantiate abstract class
dog = Dog()
dog.sound()
cat = Cat()
cat.sound()

# Anothe Example


class Vehicle(ABC):

    def __init__(self, model):
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    def display_model(self):
        print(f"Vehicle model: {self.model}")


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key!")


class ElectricScooter(Vehicle):
    def start_engine(self):
        print("Electric Scooter starts with power!")


car = Car("Toyota Safari")
car.start_engine()
car.display_model()

scooter = ElectricScooter("Xiamoi M365")
scooter.start_engine()
scooter.display_model()
