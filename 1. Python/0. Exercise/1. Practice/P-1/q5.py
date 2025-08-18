# Write a python function which converts inches to cms.
# 1 inch = 2.54 centimeters
# n inches = n * 2.54
def conversion(n):
    n *= 2.54
    return round(n, 2)


n = float(input("Enter the value in inhces you want to converted in to cms: "))
print(f"Converted value of {n}inches into centimeters is: {conversion(n)}")


def pattern(n):
    if n == 0:
        return
    for i in range(n, 0, -1):
        print("*" * i)


pattern(0)
