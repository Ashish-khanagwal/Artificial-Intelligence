line = "********************"
print(line)
print("Recurssion".center(20))
print(line)

# Recursion occurs when a function calls itself to solve a smaller piece of the original problem.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter the number you want factorial for: "))
print(factorial(n))
