<h1 align=center>ABSTRACTION</h1>

### What is Abstraction?

- Abstraction is an Object-Oriented Programming (OOP) concept that hides complex implementation details and shows only the essential features to the user.
- It simplifies interaction by exposing only the relevant parts and hiding the unnecessary internal workings.
- Think of it like driving a car: you just use the steering wheel and pedals, without needing to understand how the engine works.

### Key Terminologies to Know

1. Abstract Class
   - A class that cannot be instantiated directly.
   - It often contains abstract methods that must be implemented by its subclasses.
   - Used as a blueprint for other classes.

2. Abstract Method
   - A method declared in an abstract class but without implementation.
   - Subclasses must override these methods.

3. Concrete Class
   - A class that inherits from an abstract class and implements all abstract methods.
   - Can be instantiated to create objects.

4. How Abstraction Is Implemented in Python
   - Python uses the abc module (abstract base class) to define abstract classes and abstract methods.
   - @abstractmethod decorator is used to declare abstract methods.

   ```
   from abc import ABC, abstractmethod

   class Animal(ABC):
       @abstractmethod
       def sound(self):
           pass  # Abstract method - no implementation
   ```

### Abstraction vs Encapsulation

- Encapsulation is about hiding the data and protecting object state by bundling data and methods and controlling access with access modifiers.
- Abstraction is about hiding complexity and showing only the essential features and interfaces to the user.
- While related, abstraction focuses on what an object does, and encapsulation focuses on how the data is protected.

### Benefits of Abstraction

- Simplifies code usage by hiding complex details.
- Allows changing internal implementation without affecting users.
- Encourages modular and maintainable code.
- Facilitates polymorphism, enabling interchangeable objects via common interface.

### Abstraction in Real Life

- Using a TV remote: You press a button without knowing the internal circuitry.
- Driving a car: You use the steering wheel and pedals without worrying about how the engine works.

### Abstract Properties

Python allows abstraction of properties along with methods using @property and @abstractmethod together.

```
from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side * self._side

sq = Square(4)
print(sq.area)  # Output: 16
```
