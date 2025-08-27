"""
A list contains the multiplication table of 7. Write a program to convert it into a vertical string
of same numbers.
"""

table = [str(7 * i) for i in range(1, 11)]

vertical_table = "\n".join(table)
print(vertical_table)
