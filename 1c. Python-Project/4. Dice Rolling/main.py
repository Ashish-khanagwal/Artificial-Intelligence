from random import randint

counter = 0
while True:
    user_input = input("Roll the dice? (y/n): ")
    if user_input.lower() not in ["y", "n"]:
        print("invalid input!")
        continue
    if user_input.lower() == "y":
        num_rolls = int(input("How many dice you want to roll? "))
        rolls = [randint(1, 6) for _ in range(num_rolls)]
        print(f"{tuple(rolls)}")
        counter += 1
    else:
        print("Thank you for playing!")
        print(f"You have rolled the dice {counter} times!")
        break
