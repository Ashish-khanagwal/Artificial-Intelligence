"""
A file contains a word 'Donkey' multiple times. We need to write a program,
which replaces this word with ##### by updating the same file.
"""

with open("donkey.txt") as file:
    line = file.read()
line = line.replace("donkey", "#####")

with open("donkey.txt", "w") as file:
    file.write(line)
