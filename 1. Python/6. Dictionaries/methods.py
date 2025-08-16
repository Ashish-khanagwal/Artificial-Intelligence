# Copying dictionaries

myeleven = {
    "opener": "Rohit Sharma",
    "opener2": "Shubhman Gill",
    "captain": "MSD",
    "onedown": "Virat Kohli",
}

print(myeleven)

myeleven2 = {
    "2down": "Shreyas Iyer",
    "at 5": "Rishabh Pant",
    "at 6": "Ravindra Jadeja",
    "at 7": "Ravichandran Ashwin",
}

print(myeleven2)
print("")

Team = {}
Team = myeleven2.copy()
print("My eleven2 is copied in new empty team, and now Team is: {} ".format(Team))
Team["at 8"] = "Arshdeep Singh"
print(Team)
print(myeleven2)


# Nested Dictionaries
students = {
    30: {
        "name": "Ashish",
        "age": 24,
    },
    31: {
        "name": "Harsh",
        "age": 22,
    },
}
print(students)
print(students[30]["name"])

print("")
indian = {"toporder": myeleven, "middleorder": myeleven2}

print(indian)
print(indian["toporder"]["opener"])
print(indian["toporder"]["captain"])
print(indian["middleorder"]["at 6"])
print("")

# Converting to and from other data types
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print(d)
