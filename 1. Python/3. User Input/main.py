line = "********************"
print(line)
print("User Input".center(20))
print(line)

# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# age = int(input("Enter your age: "))
# print(f"You are {age} years old.")

# height = float(input("Enter your height in meters: "))
# print(f"Your height is {height} meters.")

# adding two numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("The sum of {} and {} is {}".format(num1, num2, num1 + num2))
# print("Thank you for your input!")

# # Multiple inputs in one line
# print("")
# a, b = input("Enter two numbers separated by a space: ").split()
# a = int(a)
# b = int(b)
# print("The product of {} and {} is {}".format(a, b, a * b))

# c,d = input("Enter first name and last name separated by a space: ").split()
# print("hello: {} {}".format(c, d))

# map(int, ...) converts each input to integer automatically.
n1, n2, n3, n4 = map(int, input("Enter four numbers separated by spaces: ").split())
print("The sum of {} and {} is {}".format(n1, n2, n1 + n2))
print("The remainder of the division of {} by {} is {}".format(n3, n4, n3 % n4))