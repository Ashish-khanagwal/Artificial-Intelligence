def word_present_at(filename, word):
    num_line = []
    with open(filename) as file:
        num_line = [(ln, l) for ln, l in enumerate(file, start=1) if word in l]
    return num_line


line_numbers = word_present_at("log.txt", "python")
if line_numbers:
    print(f"Word 'python' is present at line(s): {line_numbers}")
else:
    print("Word 'python' is not present")
