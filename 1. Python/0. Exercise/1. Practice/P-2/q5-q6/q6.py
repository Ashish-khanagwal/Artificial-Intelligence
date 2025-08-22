# Convert word to lowercase only if it is capitalized (first letter uppercase, rest lowercase)


def captial_lower(word):
    if word[0].isupper() and word[1:].islower():
        return word.lower()
    else:
        return word


with open("capital.txt") as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    words = line.split()
    words = [captial_lower(w) for w in words]
    new_lines.append(" ".join(words))

with open("capital.txt", "w") as file:
    file.write("\n".join(new_lines))
