with open("this.txt") as file:
    content = file.read()

with open("this_copy.txt", "w") as file:
    file.write(content)
