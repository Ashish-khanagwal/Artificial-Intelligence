import random
import sys

from ques_hint import quiz_hints_100
from question import quiz_dict

final_score = 0

# ANSI escape codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"


def main():
    global final_score
    global ques
    hint_count = 0
    count = 1
    print(f"{CYAN}{BOLD}Welcome to the Quiz Game!{RESET}\n")
    while count <= 5:
        data = [k.strip() for k in quiz_dict.keys()]
        ques = random.choice(data)
        print(f"{YELLOW}Question {count}: {BOLD}{ques}{RESET}")
        correct_ans = quiz_dict.get(ques)
        ans = correct_ans.lower() if correct_ans else None

        while True:
            user_ans = input(f"{CYAN}(A)nswer or (H)int: {RESET} ").strip().lower()
            if user_ans == "h":
                if hint_count < 2:
                    get_hint(ques)
                    hint_count += 1
                    print(f"{YELLOW}Hints used: {hint_count}/2{RESET}")
                else:
                    print(f"{RED}No hints left!{RESET}")
            elif user_ans == "a":
                answer = input(f"{CYAN}Your answer: {RESET}").strip().lower()
                if answer == ans:
                    print(f"{GREEN}Hurrayy 🎉, {ans} is right answer mate!{RESET}\n")
                    final_score += 1
                else:
                    print(
                        f"{RED}OOps! wrong answer!!{RESET}\nCorrect answer is 👉 {BOLD}{ans}{RESET}\n"
                    )
                break
            else:
                print(f"{RED}Invalid input! Please type 'A' or 'H'.{RESET}")
        count += 1
    print(f"{BOLD}The final score 👉 {final_score} out of 5{RESET}\n")
    playagain()


def get_hint(ques):
    if ques in quiz_hints_100.keys():
        hint_ans = quiz_hints_100.get(ques)
        print(f"{CYAN}Hint: {BOLD}{hint_ans}{RESET}")


def playagain():
    global final_score
    print(f"{CYAN}{BOLD}Want to answer some more?{RESET}")
    while True:
        user_again = input(f"(Y)es or (Q)uit\n{CYAN}> {RESET}").strip()
        if user_again.lower() not in ["y", "q"]:
            print(f"{RED}Please enter 'Y' to play again or 'Q' to quit.{RESET}")
            continue
        else:
            break
    if user_again.lower() == "y":
        final_score = 0
        print("\n" + "-" * 40 + "\n")
        return main()
    else:
        print(f"{GREEN}Thank you for playing!!{RESET}")
        sys.exit("Bye!!")


if __name__ == "__main__":
    main()
