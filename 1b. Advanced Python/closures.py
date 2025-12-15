"""
# A function that remembers variables from the place where it was created, even after that place is gone.

Think of it as :-

a function + its memory
"""


# Normal Function:
def greet():
    message = "Hello"
    print(message)


greet()

"""
Here:
Message exists only when greet() runs
After function ends -> message is gone
"""

"""
# Function inside a function
def outer():
    message = 'hello'
    def inner():
        print(message)
    inner ()
outer()


Still no closure yet - inner() is called immediately.
"""


def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner


f = outer()
f()
print(f.__name__)  # inner
# This f is inner function here.

"""
What just happened here?

outer() finished execution
message should be destroyed
But inner() still remembers message

Why does this work?

Because python keeps the variables alive if an inner function
still needs them.
"""


def outer_box(msg):
    def inner_box():
        print(msg)

    return inner_box


hi = outer_box("hello")
hello = outer_box("hey hey")

hi()
hello()
