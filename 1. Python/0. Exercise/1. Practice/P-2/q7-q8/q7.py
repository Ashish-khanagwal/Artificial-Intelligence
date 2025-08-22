# Write a program to mine a log file and find out whether it contains 'python'.
# all_words = []
# word = "python"
# with open("log.txt") as file:
#     for line in file:
#         words = line.split()
#         all_words.extend(words)
# print(all_words)
#
# if "python" in all_words:
#     print(f"python is found at: {all_words.index('python')}")
# else:
#     print("doesn't contain word: 'python'")


# def find_word_in_file(filename, word):
#     line_numbers = []
#     with open(filename) as file:
#         # for line_num, line in enumerate(file, start=1):
#         #     if word in line:
#         #         line_numbers.append(line)
#         line_numbers = [(ln, l) for ln, l in enumerate(file, start=1) if word in l]
#     return line_numbers
#
#
# lines_with_python = find_word_in_file("log.txt", "python")
# if lines_with_python:
#     print(f"Word 'python' is found at line(s): {lines_with_python}")
# else:
#     print("Word 'python' not found in file.")

### Alternate
print("")

with open("log.txt") as f:
    content = f.read()

if "python" in content:
    print("Word 'python' is found")
else:
    print("Word 'python' is not found")
