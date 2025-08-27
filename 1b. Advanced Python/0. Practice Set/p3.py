"""
Write a list comprehension to print a list which contains the multiplicatoin table of a user entered
number.
"""

n = int(input("Enter the number: "))

multiplicatoin_table = [(n * i) for i in range(1, 11)]
print(multiplicatoin_table)
