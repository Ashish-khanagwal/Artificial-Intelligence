import random
import sys
from enum import Enum


def playgame():
    class status(Enum):
        SNAKE = 1
        WATER = 2
        GUN = 3

    print("********************")
    print("Welcome".center(20))
    print("********************")
    print("It's a game of Snake, Water, and Gun: Choose your best to survive\n")
    user = input("Enter your choice\n1 for Snake\n2 for Water\n3 for Gun:\n")

    if user not in ["1", "2", "3"]:
        print("Choose from 1, 2, or 3 only")
        playgame()
    you_chose = int(user)

    print("You chose: {}".format(you_chose))
    computer = random.choice("123")
    opponent_chose = int(computer)
    print("Computer chose: {}".format(opponent_chose))

    if you_chose == opponent_chose:
        print("😉 It's a tie")
    elif you_chose == 1 and opponent_chose == 2:
        print("🎉You win")
    elif you_chose == 2 and opponent_chose == 3:
        print("🎉You win")
    elif you_chose == 3 and opponent_chose == 1:
        print("🎉You win")
    else:
        print("😭You lose")

    print("Want to play more?")
    while True:
        playagain = input("Enter: Y for yes\nQ for quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break
    if playagain.lower() == "y":
        return playgame()
    else:
        print("Thank you for playing")
        sys.exit("Bye!👋")


playgame()
