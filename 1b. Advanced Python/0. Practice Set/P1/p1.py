"""
Write a program to open 3 files 1.txt, 2.txt, and 3.txt if any these files are not present, a message
without exiting the program must be printed prompting the same.
"""


def files():
    with open("1.txt") as f1, open("2.txt") as f2, open("3.txt") as f3:
        # Do something with the files, for example:
        content1 = f1.read()
        content2 = f2.read()
        content3 = f3.read()
        # Print or process the contents as needed
        print("Content of 1.txt:")
        print(content1)
        print("\nContent of 2.txt:")
        print(content2)
        print("\nContent of 3.txt:")
        print(content3)


try:
    files()
except FileNotFoundError:
    print("Files not found")
else:
    print("Files found")
