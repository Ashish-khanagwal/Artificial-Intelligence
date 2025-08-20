import random

print("***" + "*" * 19 + "***")
print("GUESS THE NUMBER".center(25))
print("***" + "*" * 19 + "***")
print("Guess the number! You have 3 chances to guess.\n")

n = int(
    input(
        "Enter the range you want to set for this game\nstart = 1(fix) \nSpecify the end n: "
    )
)
computer = random.randint(1, n)
count = 3


def show_hint():
    mid = n // 2
    if 1 <= computer <= mid:
        print(f"Hint: The number is between 1 and {mid}.")
    else:
        print(f"Hint: The number is between {mid+1} and {n}.")


def hint():
    print("If you want a hint, type 'h'. To continue guessing, type 'n'.")
    while True:
        user_hint = input("Enter your choice (h/n): ").lower()
        if user_hint == "h":
            show_hint()
            return True  # hint given
        elif user_hint == "n":
            print("No hint will be given. Good luck!")
            return False
        else:
            print("Invalid input. Please type 'h' or 'n'.")


def get_valid_guess():
    while True:
        user_input = input(
            f"Guess the number between 1 and {n} that the computer has generated: "
        )
        if user_input.isdigit():
            return int(user_input)  # valid integer, return it
        else:
            print("Invalid input. Please enter a valid whole number.")


def gtn(count):
    hint_given = False
    while count > 0:
        user = get_valid_guess()
        if user == computer:
            print("Hooray! Your guess is right 🎉")
            break
        else:
            count -= 1
            if count == 0:
                print(
                    f"Sorry, you're out of chances now!\nYou lose!\nThe number was: {computer}"
                )
                break
            else:
                print(f"Your guess is wrong. You have {count} chance(s) left.")
                if not hint_given:
                    if hint():
                        hint_given = True


gtn(count)
