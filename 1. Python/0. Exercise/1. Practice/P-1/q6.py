# Write a python program to remove a given word from the list strip it at the same time.

l = ["Ashis", "and", "is", "Manish"]


def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n


print(rem(l, "is"))
