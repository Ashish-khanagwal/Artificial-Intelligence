# Reading a file

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# Read file line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
        # strip() will remove the newline character

# If we have to write a file, this is not the correct approach until unless we want to overwrite.
# Writing in a file (Overwriting)
with open("example.txt", "w") as file:
    file.write("Hello\n")
    file.write("This is the new file")

# Write a file (without overwritting)
with open("example.txt", "a") as file:
    file.write("This is how we append text in file")

# Writing a list of lines to a file
lines = ["\nfirst line \n", "second line \n", "third line"]
with open("example.txt", "a") as file:
    file.writelines(lines)

data = b"\x00\x01\x02\x03\x04"
with open("example.bin", "wb") as file:
    file.write(data)

with open("example.bin", "rb") as file:
    print(file)

with open("example.txt", "r") as source_file:
    content = source_file.read()

with open("destination.txt", "w") as destination_file:
    destination_file.write(content)


def count_text_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
    return line_count, word_count, char_count


file_path = "example.txt"
line, words, chars = count_text_file(file_path)
print(
    f"total number of lines {line}, file has total number of words: {words}, and total number of characters: {chars}"
)

with open("example.txt", "w+") as file:
    file.write("Hello world\n")
    file.write("This is the new line")

    file.seek(0)
    content = file.read()
    print(content)
