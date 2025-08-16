import random
import sys
from enum import Enum


class status(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True
while playagain:

    # MAKING CHOICES

    player_choice = input(
        "Enter your choice...\n1 for rock\n2 for paper\n3 for scissors: \n"
    )
    player_chose = int(player_choice)

    if player_chose < 1 or player_chose > 3:
        sys.exit("You must choose: 1, 2, or 3!")

    print("Your choice is: {}".format(player_choice))

    computer_choice = random.choice("123")
    computer_chose = int(computer_choice)

    print("Computer choice is: {}".format(computer_chose))

    # GAME LOGIC

    if player_chose == 1 and computer_chose == 3:
        print("🎉You win!")
    elif player_chose == 2 and computer_chose == 1:
        print("🎉You win!")
    elif player_chose == 3 and computer_chose == 2:
        print("🎉You win!")
    elif player_chose == computer_chose:
        print("😉Game Tie")
    else:
        print("🥲You lose")

    # PLAY AGAIN?

    playagain = input("Want to play more?\n Y for Yes\n Q for quit!")
    if playagain.lower() == "y":
        continue
    else:
        print("Thank you for playing the game")
        playagain = False

sys.exit("Bye!")
