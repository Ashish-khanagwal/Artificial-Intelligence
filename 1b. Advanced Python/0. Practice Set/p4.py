"""
Write a program to display a/b where a and b are integers. if b = 0, display infinite by handling the
'ZeroDivisionError'.
"""

try:
    b = int(input("Enter the number: "))
    a = 35
    result = a / b
except ZeroDivisionError:
    print("infinite")
else:
    print(result)
