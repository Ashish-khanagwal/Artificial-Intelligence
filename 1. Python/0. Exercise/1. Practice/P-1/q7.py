# Write a python function to print a multiplicatin table for a given number


def multiplicatin(n, m):
    if n == 0 or m == 0:
        return 0
    else:
        result = []
        for i in range(1, m + 1):
            result.append(n * i)
        return result


n = int(input("Enter the number you want multiplicatin table for: "))
m = int(input("Enter the number you want multiplicatin till the end of: "))
print(f"Multiplication table for {n} is: {multiplicatin(n, m)}")
