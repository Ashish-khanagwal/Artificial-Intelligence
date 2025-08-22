"""
enumerate() is a built-in built-in Python function that adds a counter (index) to an iterable and
returns it as an enumerate object, which yields pairs of (index, element) during iteration.
"""

fruits = ["apple", "banana", "pineapple", "grapes"]

for i, fruit in enumerate(fruits):
    print(i, fruit)

print("")

"""
here, fruit is the content in fruits list, and i represents the count (index) it starting from,
by default it's zero, we can specify the index too 'start=1'
"""

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

print("")

words = ["a", "b", "c", "d", "e"]
indexed_words = [(i, w) for i, w in enumerate(words, start=1)]
print(indexed_words)

print("")

char = ["a", "x", "b", "c", "x", "d", "x"]
find_word = [i for i, w in enumerate(char) if w == "x"]
print(find_word)

word = "hello"
char_word = [(i, ch) for i, ch in enumerate(word, start=1)]
print(char_word)
