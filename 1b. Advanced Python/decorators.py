"""
DECORATORS:-

A function that takes another function, adds extra behaviour to it,
and  returns a new function.

Without decorators -> repeated code everywhere
With decorators -> one reusable wrapper

Decorators work only because of three python features:-
1. First class functions
2. Closures
3. Function replacement


When python sees this:
@decorator
def greet():
    print('Hello')

Python actually does this:
greet = decorator(greet)
"""


# Basic decorator structure
def decorator(func):
    def wrapper(*args, **kwargs):  # -> New function that adds behavious
        # extra behaviour before
        result = func(*args, **kwargs)
        # extra behaviour after
        return result

    return wrapper


# Exampe logging decorator
def log(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)

    return wrapper


@log
def add(a, b):
    return a + b


print(add(2, 3))


# Decorator with arguments (two layer confusion)
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hi")


greet()

"""
Why 3 layers?

repeat(n) -> capture decorator arguments
decorator(func) -> recieve function
wrapper() -> add behaviour
"""

"""
Python expands this to:

greet = repeat(3)(greet)

So structure becomes:-

repeat(n) -> decorator(func) -> wrapper()
"""


def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper


# Class decorator


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("wrapper executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


# @decorator_class
# def display():
# print("display function ran!!")


# @decorator_class
# def display_info(name, age):
# print("display_info ran with argument ({}, {})".format(name, age))


# display()
# display_info("Ashish", 24)
from functools import wraps

# functools.wraps preserves the identity of the original function when it is wrapped by a decorator.


def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename="{}.log".format(orig_func.__name__), level=logging.INFO
    )

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper


import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print("display_info ran with arguments ({}, {})".format(name, age))


"""

display_info = my_logger(my_timer(display_info))

This is how execution happens
"""
display_info("Tom", 22)
