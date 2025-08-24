<h1 align = center>POLYMORPHISM</h1>

- [Method Overriding](#method-overriding)
- [Duck Typing](duck-typing)
- [Method Overloading](#method-overloading)

### What is Polymorphism?

- Polymorphism means "many forms."
- It is an OOP concept where objects of different classes can be treated as objects of a common superclass, especially when they share common methods.
  - What it means:
    - You have a common superclass (a parent class).
    - You have different classes (subclasses) that inherit from this superclass.
    - These subclasses share common methods (methods with the same name).
    - You can treat objects of these different subclasses as if they are objects of the superclass because they have those shared methods.
    - This lets you write generic code that works with all those different objects in the same way.

    ```
    class Animal:  # Common superclass
        def speak(self):
            pass  # Placeholder method

    class Dog(Animal):  # Subclass 1
        def speak(self):
            print("Woof!")

    class Cat(Animal):  # Subclass 2
        def speak(self):
            print("Meow!")

    def make_animal_speak(animal: Animal):  # Treats any subclass object as Animal
        animal.speak()  # Calls the subclass’s method

    dog = Dog()
    cat = Cat()

    make_animal_speak(dog)  # Outputs: Woof!
    make_animal_speak(cat)  # Outputs: Meow!
    ```

  - Explanation:
    - Animal is the common superclass.
    - Dog and Cat are different subclasses.
    - Both Dog and Cat share the common method speak().
    - The function make_animal_speak takes an argument typed as Animal, but you can pass a Dog or Cat instance.
    - Inside make_animal_speak, animal.speak() calls the correct method depending on the actual object passed.
    - So, even though dog and cat are different types, you can treat them both as Animal when calling make_animal_speak.

- It allows methods to do different things based on the object that calls them, even if they have the same name.
- Enables flexible and extensible code.

### Key Terminologies in Polymorphism

1. Method Overriding
   - When a subclass provides a specific implementation of a method already defined in its superclass.
   - The version of the method that gets called depends on the actual object's class.

2. Duck Typing
   - Duck typing is Python’s way of doing polymorphism without worrying about the actual class of an object.
   - The saying:
     "If it walks like a duck and quacks like a duck, it’s a duck."
   - means:
     If an object has the right methods or behaviors you need, you don’t care what type or class it really is.
   - Simple Explanation:
     - You don’t need to check if an object is a certain class.
     - You just use it as long as it has the methods you expect.
     - This makes code more flexible and easier to work with many different kinds of objects.

   ```
   class Duck:
   def quack(self):
       print("Quack, quack!")

   class Person:
       def quack(self):
           print("I’m pretending to be a duck!")

   def make_it_quack(entity):
       entity.quack()  # Just calls quack() method, doesn’t check class

   duck = Duck()
   person = Person()

   make_it_quack(duck)    # Output: Quack, quack!
   make_it_quack(person)  # Output: I’m pretending to be a duck!

   ```

   - What’s happening here?
     - Both Duck and Person have a quack() method.
     - The function make_it_quack() calls quack() on whatever you give it.
     - It doesn’t care what type of object you pass, only that it has a quack() method.
     - This is duck typing—using objects based on their behavior, not their class.

### Method Overloading

- Method overloading traditionally means defining multiple methods with the same name but different parameters (number or type) within the same class.
- It allows a method to behave differently based on its arguments.

- Important:

  > Python does not support true method overloading like languages such as Java or C++. Defining multiple methods with the same name in Python will override the previous method.

- Python simulates method overloading using:
  - Default parameter values
  - Variable-length argument lists (\*args, \*\*kwargs)
  - Manual type checking within a single method
  ```
  def method_name(arg1, arg2=default_value, *args, **kwargs):
  # function body
  ```

```
class Calculator:

    def add(self, a=None, b=None, *args):
        if a is not None and b is not None and args:
            # When more than two arguments provided
            total = a + b + sum(args)
            print(f"Sum of {a}, {b} and {args} = {total}")
        elif a is not None and b is not None:
            # When exactly two arguments provided
            print(f"Sum of {a} and {b} = {a + b}")
        elif a is not None:
            # When one argument provided
            print(f"Single argument provided: {a}")
        else:
            print("No arguments provided")

calc = Calculator()
calc.add()               # No arguments provided
calc.add(10)             # Single argument provided: 10
calc.add(10, 20)         # Sum of 10 and 20 = 30
calc.add(1, 2, 3, 4, 5)  # Sum of 1, 2 and (3, 4, 5) = 15
```

> In Python, true method overloading (defining multiple methods with the same name but different signatures) does not occur because the latest method definition overrides any previous ones.

    Instead, Python uses flexible method definitions with:

- \*args (variable-length positional arguments)
- \*\*kwargs (variable-length keyword arguments)
- Default argument values

These techniques allow you to write methods that can handle different numbers and types of arguments, effectively mimicking method overloading.
So, while method overloading as a language feature isn’t supported in Python, you achieve similar behavior by writing versatile, flexible methods.
