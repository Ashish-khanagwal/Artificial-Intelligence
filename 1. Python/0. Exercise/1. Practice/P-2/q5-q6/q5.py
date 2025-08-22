# Program for a list of such words to be censored

words = ["dumb", "dirty", "drunk", "dopey", "damn", "dodgy"]

with open("censored.txt") as file:
    content = file.read()

for word in words:
    content = content.replace(word, "*" * len(word))

with open("censored.txt", "w") as file:
    file.write(content)
