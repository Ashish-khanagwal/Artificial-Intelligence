# The game() function in a program lets user play a game and returns the score as an integer.
# you need to read a file 'Hi-score.txt' which is blank or either contains the previous high score.
# you need to write a program to update the hi-score.txt file everytime game() breaks the high-score.
import random


def game():
    print("You're playing a game....")
    score = random.randint(1, 101)

    with open("hi-score.txt") as file:
        high_score = file.read()
        if high_score != "":
            high_score = int(high_score)
        else:
            high_score = 0

    print(f"your score is {score}")

    if score > high_score:
        print("Congrats 🎉, New high score!!")
        print(f"your score is {score}")
        with open("hi-score.txt", "w") as file:
            file.write(str(score))
    return score


game()
