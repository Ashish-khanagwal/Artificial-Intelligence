line = "***************"
print(line)
print("Loops".center(15))
print(line)

num = {23, 34, 45, 56, 67}
for i in num:
    print(i)

# count = 1
# while count <= 10:
#     print("Count: ", count)
#     if count == 5:
#         break
#     count += 1
print("")

# while count <= 10:
#     count += 1
#     if count == 5:
#         continue
#     print("count: ", count)
# else:
#     print("Value is not equal to ", count)

# for name in names:
#     print(name)
#
# for name in names:
#     if name == "X":
#         break
#     print(name)

# for x in names:
#     if x == "X":
#         continue
#     print(x)

# for i in range(4):
#     print(i)

for i in range(2, 21, 2):
    print(i)
else:
    print("Glad that's over!")

names = ["Ashish", "Manish", "X", "Lalit", "Harsh"]
actions = ["Devops", "App Developer", "Y", "Mechanical", "Tester"]

# for name in names:
#     for profession in actions:
#         print(name, profession)

# Above code's output down below:
#
# Ashish Devops
# Ashish App Developer
# Ashish Y
# Ashish Mechanical
# Ashish Tester
# Manish Devops
# Manish App Developer
# Manish Y
# Manish Mechanical
# Manish Tester
# X Devops
# X App Developer
# X Y
# X Mechanical
# X Tester
# Lalit Devops
# Lalit App Developer
# Lalit Y
# Lalit Mechanical
# Lalit Tester
# Harsh Devops
# Harsh App Developer
# Harsh Y
# Harsh Mechanical
# Harsh Tester

# Instead of two nested loops, use zip() which ties together two lists element by element:
for name, profession in zip(names, actions):
    print(name, profession)
print("")
# Similar results can be achieved by using nested loop too, but with some extra logic see below:
for i in range(len(names)):
    for j in range(len(actions)):
        if i == j:
            print(names[i], actions[j])
print("")
# But still the better way to do is using zip() method.
# names and actions list can also be converted into dictionary by using zip()
mapping = dict(zip(names, actions))
print(mapping)
