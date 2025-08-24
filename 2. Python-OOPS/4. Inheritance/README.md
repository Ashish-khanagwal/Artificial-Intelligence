<h1 align=center>INHERITANCE</h1>

- [Multiple Inheritance](#multiple-inheritance)
- [MRO](#mro)
- [Multilevel Inheritance](#multilevel-inheritance)
- [Hierarchical Inheritance](#hierarchical-inheritance)
- [super in Multiple Inheritance](#super-in-multiple-inheritance)

### What is Inheritance?

- Inheritance is an Object-Oriented Programming (OOP) concept where a new class (child/subclass) inherits attributes and methods from an existing class (parent/superclass).
- It allows code reuse, and the child class can extend or override the behavior of the parent class.
- Think of it as a family tree where children inherit traits from their parents.

### Key Terminologies in Inheritance

1. Parent (Super) Class
   - The class whose properties and methods are inherited by another class.

2. Child (Sub) Class
   - The class that inherits properties and methods from the parent.
   - Can add its own attributes/methods or override existing ones.

3. Method Overriding
   - When a child class provides a new version of a method inherited from the parent.

4. super() Function
   - Used in the child class to call a method from the parent class.

5. Multiple Inheritance
   - A child class inherits from more than one parent class.

```
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

animal = Animal()
animal.sound()  # Output: Animal makes a sound

dog = Dog()
dog.sound()     # Output: Dog barks (overridden method)
```

- Dog inherits from Animal.
- Dog overrides the sound() method with its own version.

### Multiple Inheritance

- A class can inherit from more than one parent class.
- This allows combining behaviors from multiple classes.
- Be cautious of complexity and the “Diamond Problem” (ambiguity caused by multiple inheritance paths).

```
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()   # Output: Flying...
d.swim()  # Output: Swimming...
```

### MRO

- Occurs when a class inherits from two classes that both inherit from a single parent.
- Python uses MRO (Method Resolution Order) to decide the order to look for methods.

```
class A:
    def do_something(self):
        print("A's method")

class B(A):
    def do_something(self):
        print("B's method")

class C(A):
    def do_something(self):
        print("C's method")

class D(B, C):
    pass

d = D()
d.do_something()  # Output: B's method
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

### Multilevel Inheritance

- A class inherits from a child class, forming a chain of inheritance.

```
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Puppy(Dog):
    def sound(self):
        print("Puppy yelps")

p = Puppy()
p.sound()  # Output: Puppy yelps
```

### Hierarchical Inheritance

- Multiple classes inherit from the same parent class.

```
class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

cat = Cat()
dog = Dog()

cat.sound()  # Cat meows
dog.sound()  # Dog barks
```

### super in Multiple Inheritance

- super() works with Python’s MRO to call the next method in line.
- Important to follow cooperative multiple inheritance style to avoid unexpected behavior.

```
class A:
    def show(self):
        print("Inside A")
        super().show()

class B(A):
    def show(self):
        print("Inside B")
        super().show()

class C(A):
    def show(self):
        print("Inside C")
        super().show()

class D(B, C):
    def show(self):
        print("Inside D")
        super().show()

# Create an instance of D
d = D()
d.show()
```

### What happens here?

- Classes B and C both inherit from A.
- Class D inherits from both B and C (multiple inheritance).
- Each class’s show method calls super().show(), which calls the next method in Python’s MRO.

### OUTPUT

```
Inside D
Inside B
Inside C
Inside A
```

### Explanation:

- D.show() calls super().show() which goes to B.show().
- B.show() calls super().show() which goes to C.show().
- C.show() calls super().show() which goes to A.show().
- A.show() prints "Inside A" and tries to call super().show(), but since A is at the end, this usually stops (unless A has a parent).
- This shows how super() respects the MRO to call methods in the correct order in multiple inheritance.

### Important:

When using multiple inheritance, always use super() and design your classes cooperatively so each super() call is consistent; this avoids unexpected behaviors.
