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


# Attributes and Methods
class Cat:
    def __init__(self, name, age):  # --> Constructor Method
        self.name = name  # --> Attributes
        self.age = age

    def meow(self):
        print(f"{self.name} is meowing...")


cat1 = Cat("Kitty", 4)
cat1.meow()

print("")


# Class attributes and Instance attributes
class Cow:
    species = "Holstein Friesian"

    def __init__(self, name, sound, owner):
        self.name = name
        self.sound = sound
        self.owner = owner

    def moo(self):
        print(f"{self.name} sounding {self.sound}")


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

    def intro(self):
        print(
            f"Owner is {self.name}, lives at {self.address}, you can contact at {self.phone_number}"
        )


owner1 = Owner("John", "Bali", "888-999-000")
cow1 = Cow("Heera", "moo", owner1)
print(cow1.name)
cow1.moo()
cow1.owner.intro()
print(cow1.species)

print("")

owner2 = Owner("Sina", "ilab", "999-000-888")
cow2 = Cow("Moti", "moo", owner2)
print(cow2.name)
cow2.moo()
cow2.owner.intro()
print(cow2.species)

# Another Example
print("")
print("**" + "*" * 16 + "**")
print("*" + "Example 1".center(18) + "*")
print("**" + "*" * 16 + "**")


class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def intro(self):
        print(
            f"My name is {self.name}, I am {self.age} years old and my profession is {self.profession}"
        )


person1 = Person("Ashish", 24, "DevOps Engineer")
person1.intro()

person2 = Person("Manish Kumar gupta", 23, "App Developer")
person2.intro()

# Another Example
print("")
print("**" + "*" * 16 + "**")
print("*" + "Example 2".center(18) + "*")
print("**" + "*" * 16 + "**")


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}, it's {self.username}"
        )


user1 = User("Ashish", "ashish.gmail", "123")
user2 = User("Croovi", "croovi@croovi", "abc")
user2.say_hi_to_user(user1)
