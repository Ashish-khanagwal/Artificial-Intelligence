line = "********************"
print(line)
print("Functions".center(20))
print(line)

# A function is a block of reusable code designed to perform a specific task. Functions help:
# Organize code better
# Avoid repetition
# Make code modular and easier to debug and maintain


def hello():
    print("Hello, World!")


hello()


def summ(num1, num2):
    return num1 + num2


total = summ(2, 4)
print(total)


def greet(name):
    print(f"Hey! {name}")


greet("Ashish")


def describe_animal(animal, name):
    return f"I have an {animal} named {name}"


myanimal = describe_animal("Elephant", "Gajraj")
print(myanimal)


# *args -> Variable number of positional arguments - Tuples
def add_all(*args):
    return sum(args)


print(add_all(2, 4, 6, 8))


# **kwargs -> Vairable number of keyword arguments - Dictionary
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Ashish", age=24)
