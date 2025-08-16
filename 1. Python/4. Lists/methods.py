users = ["Ashish", "Manish", "Saurav", "Harsh", "Lalit", "Aniket"]
print(users)
print(len(users))

users[4:4] = [
    "Robert",
    "Alex",
]  # this will add these values at index 4 without replacing
print(users)

users[4:6] = ["Eddie", "RDJ"]  # This will replace the values from index 4 to 5
print(users)
print("")

# Removing the item from the lists
users.remove("Ashish")  # --> Remove the mentioned item from the list
print(users)
print("")

print(users.pop())  # --> Will return the last element and removes it too
print(users)  # --> Removes the last element from the list
print("")

del users[0]  # --> Deletes the item from the list at index 0
print(users)
print("")

# users.clear()  # --> Clears this list and return the empty list
# print(users)

num = [3, 1, 4, 7, 5, 2, 8, 6, 9, 3, 1, 3]
print(len(num))
print(min(num))
print(max(num))
print(sum(num))
print(num.count(3))
print(num.index(3))

# num.sort()
# print(num)

# num.sort(reverse=True)
# print(num)
#
# num.reverse()
# print(num)

print(sorted(num, reverse=True))
print(num)

users[0:0] = ["ashish"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

# Copying the list
numscopy = num.copy()
nums2 = num[:]
nums3 = list(num)

print("")
print(num)
print(numscopy)
print(nums2)
print(nums3)

# Iterating in a list
for i in num:
    print(i)
