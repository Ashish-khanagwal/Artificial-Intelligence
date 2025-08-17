# Write a recursive function to calculate the sum of first n natural numbers.
# sum = n + (n-1) + (n-2) + (n-3)......


def sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


n = int(input("Enter the natural number you want sum upto: "))
print(f"The sum of {n} natural numbers is: {sum(n)}")
