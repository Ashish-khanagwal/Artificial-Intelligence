<h1 align=center>BASICS</h1>

- [Class](#1-class)
- [Object](#2-object)
- [Attributes and Methods](#3-attributes-and-methods)
- [Constructor Method](#4-constructor-method)
- [Self-Keyword](#5-self-Keyword)
- [Instance-Methods](#6-instance-methods)
- [Class Attributes and Instance Attributes](#7-class-attributes-and-instance-attributes)

### 1. Class:

- A class is a blueprint for creating objects.
- It defines a set of attributes and behaviors (methods) that the created objects will have.

```
class MyClass
    pass
```

### 2. Object:

- An object is an instance of a class.
- it has the properties and behaviors defined by the class.

```
obj = MyClass()
```

### 3. Attributes and Methods:

- Attributes: Variables inside a class that store data
- Methods: Functions inside a class that define behaviours.

```
class Dog():                       --> Class
    def __init__(self, name, age): --> Constructor Method
        self.name = name           --> Attributes
        self.age = age
    def bark():                    --> Method
        print(f"{self.name}" is barking..)

dog = Dog("Bruno", 4)              --> Object
dog.bark()                         --> Calling Method
```

### 4. Constructor Method

- `__init__`
- Automatically called when a new object is created.
- Used to initialize attributes of the object.

```
def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2
```

### 5. self Keyword

- Represents the instance of the class.
- Allows access to the attributes and methods of the class in Python.
- Must be the first parameter of instance methods.

### 6. Instance Methods

- Methods that work with the instance/object data.
- Can access and modify object state.

```
class Car:
    def __init__(self, color, brand):
        self.color = color     # Instance attribute
        self.brand = brand     # Instance attribute

    def paint(self, new_color):
        self.color = new_color  # Change the car's color (modify object state)

    def display(self):
        print(f"This car is a {self.color} {self.brand}.")  # Access object state


# Create an instance (object) of Car
my_car = Car("red", "Toyota")

my_car.display()      # Output: This car is a red Toyota.

my_car.paint("blue")  # Change the color using instance method

my_car.display()      # Output: This car is a blue Toyota.
```

### 7. Class Attributes and Instance Attributes

- Instance attributes are unique to each object.
- Class attributes are shared across all instances.

```
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
```
