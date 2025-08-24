"""
Class Methods -
- A class method belongs to the class rather than any instance.
- It receives the class itself as the first argument, conventionally named cls.
- Class methods can access and modify class state that applies across all instances.
- They are often used for factory methods and operations affecting the class-level data.

How to Define a Class Method?
- Use the @classmethod decorator above the method.
- The first parameter must be cls to receive the class itself.

class MyClass:
    @classmethod
    def my_class_method(cls, args)
        Pass
"""


# Example
class Dog:
    species = "German Shephard"
    no_of_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.no_of_dogs += 1

    @classmethod
    def get_dog_count(cls):
        return cls.no_of_dogs


dog1 = Dog("Rod")
dog2 = Dog("Billy")

print(Dog.get_dog_count())

"""
USE CASE - 
1. Class methods are functions defined inside a class but marked specially so they receive the class itself, 
not the instance, as the first argument (usually called cls). Here’s what makes them useful:

2. Access or modify class-level attributes:
They can see or change data that belongs to the whole class, not just one instance. 
For example, updating a counter that tracks how many objects have been made.

3. Factory methods that instantiate objects in specific ways:
Sometimes, you need different ways to create objects of your class. 
A class method can provide a special construction process. 
For instance, you can have a method that creates objects using data from a string, 
dictionary, or other format.

4. Alternative constructors:
These are extra ways to create new objects of your class, apart from the normal constructor (__init__). 
Class methods can serve as these alternative constructors.
"""


# Factory Method example using Class Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age)


p1 = Person.from_birth_year("Ashish", 2001)
print(p1.name, p1.age)

"""
Class methods let you work with and create objects using information that’s not passed to the usual 
constructor. They’re perfect for special creation patterns or modifying class-level settings.
"""
