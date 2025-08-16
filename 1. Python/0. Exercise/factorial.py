def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num = int(input("Enter the number you want factorial for: "))
print(f"The factorial for {num} is: ")
print(factorial(num))
