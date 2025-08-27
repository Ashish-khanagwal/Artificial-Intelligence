# Basic syntax and example

try:
    num = int(input("Enter an integer: "))

except Exception as e:
    print(e)

# Example-2

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot be divided by zero")

# Catching multiple exceptions

try:
    a = int(input("Enter an integer "))
    b = 35
    result = b / a
    print(result)
except ValueError:
    print("Invalid input, Please enter a number")
except ZeroDivisionError:
    print("Cannot be divided by zero")

# Using a single except for multiple exceptions
try:
    a = int(input("Enter an integer "))
    b = 35
    result = b / a
    print(result)
except (ValueError, ZeroDivisionError):
    print("Caught ValueError or ZeroDivisionError")

# The else clause - runs when no exception occurs
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number.")
else:
    print(f"You entered: {num}")


# The Finally clause
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")


# Custom Exception classes
class NegativeNumberError(Exception):
    pass


def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot compute square root of a negative number")
    return x**0.5


num = int(input("Enter a number: "))
print(square_root(num))


# Raising exceptions
# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be 18 or older")
#     print("Access granted")
#
#
# check_age(16)  # Raises ValueError
