import random
import string
import sys

from data import capital_alphabets, lower_alphabets, number, special_characters

# ANSI escape codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"


def is_valid_password():
    # Catching ValueError if any
    try:
        # Taking input to decide length of passwrod
        uc = int(input(f"{YELLOW}How many capital alphabets do you want? {RESET}"))
        ul = int(input(f"{YELLOW}How many lowercase alphabets do you want? {RESET}"))
        un = int(input(f"{YELLOW}How many numbers do you want? {RESET}"))
        usc = int(input(f"{YELLOW}How many special characters do you want? {RESET}"))
        length = uc + ul + un + usc

        # Checking validity of password
        if 8 <= length <= 18:
            return uc, ul, un, usc
        else:
            print(
                f"{RED}Length of password is impermissible!{RESET}\n{RED}Let's go again!!{RESET}"
            )
            return main()
    # Caught ValueError
    except ValueError:
        print(f"{RED}Ivalid Value{RESET}\n{CYAN}Let's go again!{RESET}")
        return main()


def password_generator(uc, ul, un, usc):

    # Random selection
    c_alpha = random.sample(capital_alphabets, uc)
    l_alpha = random.sample(lower_alphabets, ul)
    num = random.sample(number, un)
    s_char = random.sample(special_characters, usc)

    # Password generation
    password_list = c_alpha + l_alpha + num + s_char
    random.shuffle(password_list)
    password = "".join(password_list)
    secret_password = "*" * len(password)
    strength = password_strength(password)

    print(f"{RED}Your password's strength: {YELLOW}{strength}{RESET}")

    # Password secrecy
    def show_password(masked, original):
        print(f"{CYAN}Your secret password is: {BOLD}{masked}{RESET}")
        print(f"{CYAN}Want to reveal the password?{RESET}")
        while True:
            reveal = input(f"{YELLOW}(R)eveal or (N)o-Reveal: {RESET}").strip()
            if reveal.lower() not in ["r", "n"]:
                continue
            else:
                break
        if reveal.lower() == "r":
            print(f"{GREEN}Your password is: {BOLD}{original}{RESET}")
        else:
            pass

    show_password(secret_password, password)


def password_strength(password):
    length = len(password)
    strength_points = 0

    # Points for length
    if length >= 8:
        strength_points += 1
    if length >= 12:
        strength_points += 1
    if length >= 16:
        strength_points += 1

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    character_types = sum([has_upper, has_lower, has_digit, has_special])
    strength_points += character_types

    if length > 0 and len(set(password)) < length / 2:
        strength_points -= 1

    # Strength classification
    if strength_points >= 6:
        return "Strong"
    elif strength_points >= 4:
        return "Medium"
    else:
        return "Weak"


def main():
    # WELCOME
    print("\n" + "-" * 40)
    print(f"{CYAN}{BOLD}Welcome To Random Password Generator\n{RESET}")
    print(
        f"{CYAN}Generate password of your own preferences (length should be 8 to 16){RESET}"
    )
    print("-" * 40 + "\n")

    # If valid password
    result = is_valid_password()
    if result:
        uc, ul, un, usc = result
        password_generator(uc, ul, un, usc)

    # Generate Again
    print(f"{CYAN}Want to generate more?{RESET}")
    while True:
        user_input = input(f"{YELLOW}(Y)es or (Q)uit\n{RESET}").strip()
        if user_input.lower() not in ["y", "q"]:
            print(f"{RED}Choose Y or Q{RESET}")
            continue
        else:
            break
    if user_input.lower() == "y":
        return main()
    else:
        print(f"{GREEN}Thank you for using Password Generator!!{RESET}")
        sys.exit("Bye!")


# Calling main function
if __name__ == "__main__":
    main()
