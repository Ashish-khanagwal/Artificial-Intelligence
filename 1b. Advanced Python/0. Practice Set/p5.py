"""
Store the multiplication tables generated in problem 3 in a file named Tables.txt
"""

n = int(input("Enter the number: "))

multiplicatoin_table = [(n * i) for i in range(1, 11)]
print(multiplicatoin_table)
# table = ", ".join(str(t) for t in multiplicatoin_table)


with open("Tables.txt", "a") as file:
    file.write(f"\nMultiplication table for {n} is {str(multiplicatoin_table)}")
