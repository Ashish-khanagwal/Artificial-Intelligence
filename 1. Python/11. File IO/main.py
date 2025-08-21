print("***" + "*" * 14 + "***")
print("*" + "File I/O".center(18) + "*")
print("***" + "*" * 14 + "***\n")
print("Hello world")
# Reading a file
f = open("main.txt")
data = f.read()
print(data)

# Writing in a file
st = "First we got to know, how to write a file.\nSecond we got to know, how to write in a file.\nThird, we got to know how to read a file line by line."
f = open("main.txt", "w")
f.write(st)
print("")

# Reading lines in a file
f = open("main.txt")
# lines = f.readlines()
# print(lines, type(lines))

# Read lines one by one.
# line1 = f.readline()
# print(line1)
#
# line2 = f.readline()
# print(line2)
#
# line3 = f.readline()
# print(line3)
#
# line4 = f.readline()
# print(line4 == "")

line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()
