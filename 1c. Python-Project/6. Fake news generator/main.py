import random

from words import actions, places, subjects

while True:
    user_input = input("Want some funny news headline? (y/n): ")
    if user_input.lower() not in ["y", "n"]:
        print("invalid input")
        continue
    if user_input.lower() == "y":
        s = random.choice(subjects)
        a = random.choice(actions)
        p = random.choice(places)
        print(f"BREAKING NEWS 👉 {s} {a} {p}\n")
    else:
        print("I hope you enjoyed the headlines!")
        break
