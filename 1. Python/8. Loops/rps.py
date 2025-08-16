import random
import sys

line = "*************************"
print(line)
print("Welcome".title().center(26))
print(line)
print("Rock🪨 Paper📄 Scissor✂️")
print(line)

playagain = True
while playagain:
    player_name = input("Enter your name: ").upper()
    print("Player name is {}".format(player_name))

    print("")
    choice = ["rock", "paper", "scissors"]
    print("Let's play a game of Rock, Paper, Scissors!")
    print("You can choose between Rock, Paper, or Scissors.\n")
    player_choice = input("Enter your choice: \n")

    if player_choice.lower() not in choice:
        print("Not a valid entry!")
        break
    else:
        print("You chose: {}".format(player_choice))

        computer_choice = random.choice(choice)
        print("Computer chose: {}".format(computer_choice))

        # Game Logic

        if player_choice.lower() == computer_choice:
            print("It's a tie!😉")
        elif (
            (player_choice.lower() == "rock" and computer_choice == "scissors")
            or (player_choice.lower() == "paper" and computer_choice == "rock")
            or (player_choice.lower() == "scissors" and computer_choice == "paper")
        ):
            print("{} win!🎉".format(player_name))
        else:
            print("{} lose!😢".format(player_name))
        print("Thank you for playing!")

        playagain = input("Want to play again?\nY for Yes!\n Q to quit the game!")
        if playagain.lower() == "y":
            continue
        else:
            print("🤗Thank you for playing!🤗")
            playagain = False
sys.exit("bye!👋👋")
