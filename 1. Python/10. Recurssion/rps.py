import random
import sys
from enum import Enum


def play_rps():
    class status(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # MAKING CHOICES

    player_choice = input(
        "Enter your choice...\n1 for rock\n2 for paper\n3 for scissors: \n"
    )

    if player_choice not in ["1", "2", "3"]:
        print("You must choose: 1, 2, or 3!")
        play_rps()

    player_chose = int(player_choice)

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
    print("Want to play more?\n")
    while True:
        playagain = input("Y for Yes\nQ for quit!\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Thank you for playing the game")
        sys.exit("Bye!")


play_rps()
