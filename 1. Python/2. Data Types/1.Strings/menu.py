title = "menu".upper()
print(title.center(35, '-'))
food = "Food Item".upper()
print(food.ljust(26, '.') + "price".upper().rjust(9))
print("1. Pizza".ljust(26, '.') + "$10.99".rjust(9))
print("2. Burger".ljust(26, '.') + "$7.99".rjust(9))
print("3. Garlic bread".ljust(26, '.') + "$8.99".rjust(9))

# String Formatting
print('\n')

# f-string formatting
name = "Ashish Khanagwal"
age = 24
print("f-string formatting")
print(f"My name is {name} and I'm {age} yeras old")

# .format method
print("\n")
print(".format Method")
print("My name is {} and I'm {} years old".format(name, age))

# some methods return the boolean data
print(name.startswith("A"))
print(name.endswith("h"))
print(name.endswith("l"))