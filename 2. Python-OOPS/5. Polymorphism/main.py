print("***" + "*" * 24 + "***")
print("*" + "Polymorphism".center(28) + "*")
print("***" + "*" * 24 + "***")

# Example-1: Polymorphism with method overriding


class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog makes sound of Woof Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat makes sound of Meow Meow!")


def animal_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)

# Example-2: Polymorphism with Duck Typing


class Bird:
    def fly(self):
        print("Bird is flying..")


class Aeroplane:
    def fly(self):
        print("Aeroplane is flying..")


def let_it_fly(entity):
    entity.fly()


bird = Bird()
aeroplane = Aeroplane()

let_it_fly(bird)
let_it_fly(aeroplane)
