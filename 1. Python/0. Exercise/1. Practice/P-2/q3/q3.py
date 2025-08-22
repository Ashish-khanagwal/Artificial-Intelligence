# Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# Place these files in a folder for a 13 year old kid.


def table(n):
    result = []
    for i in range(1, 10 + 1):
        value = n * i
        result.append(value)
    return result


def create_file():
    for t in range(2, 21):
        with open(f"{t}.txt", "w") as f:
            f.write(f"Multiplicatin table for {t} is : {table(t)}")


create_file()
