with open("this.txt") as file:
    content = file.read()

with open("this_copy.txt") as file:
    content_1 = file.read()

if content == content_1:
    print("Files are identical and mathces the content of another file")
else:
    print("Not identical")
