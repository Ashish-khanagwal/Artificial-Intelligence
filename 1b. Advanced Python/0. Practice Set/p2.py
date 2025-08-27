"""
Write a program to print third, fifth, and seventh element from a list using enumerate function.
"""

l = [0, 4, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

for i, c in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(l[i])
