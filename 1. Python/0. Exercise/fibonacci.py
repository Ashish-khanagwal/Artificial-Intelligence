def fibonacci(n):
    a, b = 0, 1
    series = []

    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


n = int(input("Enter the number you want fibonacci series for: "))
print(f"Fibonacci series for {n} numbers: ")
print(fibonacci(n))
