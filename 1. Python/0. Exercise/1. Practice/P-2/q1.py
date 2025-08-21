# Write a program to read the text from a given file 'poem.txt' and findout whether it contains the word "Twinkle"

with open("poem.txt", "r") as file:
    twinkle = False
    line = file.readline()
    while line != "":
        words = line.split()
        if "Twinkle" in words:
            print("File contains the word 'Twinkle'")
            twinkle = True
            break
        line = file.readline()
    if not twinkle:
        print("File doesn't contain the word: 'Twinkle'")


# found = False
#
# with open("poem.txt", "r") as file:
#     for line in file:
#         poem_words = line.split()
#         if "Twinkle" in poem_words:
#             found = True
#             break
#
# if found:
#     print("File contains the word 'Twinkle'")
# else:
#     print("File doesn't contain 'Twinkle'")
