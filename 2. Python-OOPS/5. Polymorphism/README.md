<h1 align = center>POLYMORPHISM</h1>

- [Method Overriding](#method-overriding)
- [Duck Typing](duck-typing)
- [Method Overloading](#method-overloading)
- [Operator Overloading](#operator-overloading)

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

### Operator Overloading

Operator overloading is a feature in Python that allows you to define custom behavior for standard operators (like +, -, \*, ==, etc.) when they are used with objects of your own classes. This makes your objects behave more intuitively and flexibly, much like built-in types (e.g., adding two strings concatenates them, adding two numbers sums them).

- Key Terminologies:
  - Operator: Symbols like +, -, \*, == that perform operations.
  - Operands: The values or objects the operators act on.
  - Magic/Dunder Methods: Special methods with double underscores (e.g., **add**, **eq**) that Python calls automatically for operator overloading.
  - Operands' Types: Operator behavior can differ depending on the types involved.

- How It Works
  - Define a special magic method in your class—Python maps each operator to a method (such as **add** for +).
  - When the operator is used, Python automatically calls this method on your objects.

- Common Operator overloading methods
  | Operator | Magic Method |
  | :------- | :------: |
  | + | \_\_add\_\_ |
  | - | \_\_sub\_\_ |
  | \* | \_\_mul\_\_ |
  | == | \_\_eq\_\_ |
  | > | \_\_gt\_\_ |
  | < | \_\_lt\_\_ |

- Python Built-in Operator Overloading Examples
- 1 + 2 calls int.**add**.
- "Hello" + "World" calls str.\_\_add\_\_ (concatenation).
- [1,2] + [3,4] calls list.\_\_add\_\_ (merging lists).

<h4>Reflected (Reverse) Methods</h4>

- Reflected (Reverse) Methods help Python handle operators when the left-side object doesn’t know what to do with the operation—especially with mixed types (like an int and a custom object).

- Simple Explanation:
  - When you write 5 + my_object, Python first tries int.**add**(my_object).
  - If the built-in int class doesn't know how to add my_object, Python tries the reverse method on your object: my_object.**radd**(5).
  - This lets your custom class control how it interacts with built-in types when your object is on the right side of the operator.

  ```
  class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # For expressions like my_object + 5
        return MyNumber(self.value + other)

    def __radd__(self, other):
        # For expressions like 5 + my_object
        return MyNumber(self.value + other)

    def __repr__(self):
        return f"MyNumber({self.value})"

    num = MyNumber(10)

  print(num + 5)   # Calls __add__: MyNumber(15)
  print(5 + num)   # Calls __radd__: MyNumber(15)
  ```

  - num + 5 calls MyNumber.**add**(num, 5).
  - 5 + num first tries int.**add**(num), fails, then calls MyNumber.**radd**(num, 5).
  - \_\_repr\_\_
    - \_\_repr\_\_ is a special method in Python that tells Python how to represent your object as a string.
    - When you print an object, Python calls this method to get a meaningful string to display.
    - If you don’t define it, Python shows a default message showing the object’s memory address, which looks like gibberish (e.g., <\_\_main\_\_.Vector object at 0x100e1d3d0>).

<h4>Chaining Operator Overloads</h4>

- Operator overloads can be used in chains, especially arithmetic operators.
  It's important to return a new object (or a suitable value) in magic methods to allow further operations.
