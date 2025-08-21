# With Statement

f = open("main.txt")
print(f.read())
f.close()

print("1\n")

# This is how with statment is written to read a file.
# Same can be written using the With statement like this.
with open("main.txt") as f:
    print(f.read())

print("2\n")

# Reading line by line
with open("main.txt") as f:
    for line in f:
        print(line.strip())

print("3\n")

with open("main.txt") as file:
    lines = file.readlines()
    line_count = len(lines)

print("Number of lines: ", line_count)
