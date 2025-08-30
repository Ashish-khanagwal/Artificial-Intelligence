import os
import sys

from colorama import Fore, Style, init

init(autoreset=True)


def add_diary():
    date_str = input(Fore.CYAN + "Enter date  (DD-MM-YYYY): ")
    print(f"{Fore.GREEN}Date: {date_str}")
    print("Write about your day (CTRL+D to finish): ")
    user_day = sys.stdin.read()
    print(f"\n\n{Fore.YELLOW}Your Day: ")
    print(user_day)
    with open(f"{date_str}.txt", "w") as file:
        file.write(f"{date_str}\n{user_day}")
    with open("date_title.txt", "a") as file:
        file.write(date_str + "\n")


def display_all_dates():
    try:
        with open("date_title.txt", "r") as file:
            dates = [line.strip() for line in file if line.strip()]
            print(Fore.MAGENTA + "Available diary dates:")
            for date in dates:
                print(Fore.CYAN + date)
            return dates
    except FileNotFoundError:
        print(Fore.RED + "No diary dates found.")
        return main()


def choose_date(dates):
    selected_date = input(
        Fore.CYAN + "Enter the date you want to see (format DD-MM-YYYY): "
    ).strip()
    if selected_date in dates:
        return selected_date
    else:
        print(Fore.RED + "Date not found in diary.")
        return None


def display_diary(date_str):
    try:
        with open(f"{date_str}.txt", "r") as file:
            content = file.read()
            print(f"\n{Fore.MAGENTA}Diary for {Fore.CYAN}{date_str}")
            print(Fore.MAGENTA + "=" * 20)
            print(Fore.YELLOW + content)
    except FileNotFoundError:
        print(Fore.RED + f"No diary entry found for {date_str}.")


def edit_diary(date_str):
    try:
        with open(f"{date_str}.txt", "r") as file:
            lines = file.readlines()
        count = 1
        print(Fore.MAGENTA + "Current file content:")
        for line in lines:
            if line.strip():
                print(Fore.CYAN + f"{count} --> {Fore.YELLOW}{line.strip()}\n")
                count += 1
        n = int(input(Fore.CYAN + "How many changes do you want to make? "))
        for _ in range(n):
            to_find = input(Fore.CYAN + "Enter the text you want to replace: ")
            replace_with = input(Fore.CYAN + "Enter the new text: ")
            for i, line in enumerate(lines):
                if to_find in line:
                    lines[i] = line.replace(to_find, replace_with)
        with open(f"{date_str}.txt", "w") as file:
            file.writelines(lines)
        print(Fore.GREEN + "File updated successfully.")
    except FileNotFoundError:
        print(Fore.RED + f"No diary entry found for {date_str}.")


def del_diary(date_str):
    filename = f"{date_str}.txt"
    confirm = (
        input(
            Fore.RED + f"Do you want to delete the diary entry for {date_str}? (Y/N): "
        )
        .strip()
        .upper()
    )
    if confirm == "Y":
        try:
            os.remove(filename)
            print(Fore.GREEN + f"Diary entry for {date_str} has been deleted.")
            with open("date_title.txt", "r") as file:
                dates = [line.strip() for line in file if line.strip()]
            if date_str in dates:
                dates.remove(date_str)
            else:
                print(Fore.RED + f"{date_str} not found in date_title.txt")
            with open("date_title.txt", "w") as file:
                for date in dates:
                    file.write(date + "\n")
            print(Fore.GREEN + f"Updated date_title.txt, removed entry for {date_str}")
        except FileNotFoundError:
            print(Fore.RED + "date_title.txt not found, nothing to update.")
    else:
        print(Fore.YELLOW + "Deletion cancelled.")
        return main()


def main():
    print(Fore.MAGENTA + 50 * "-" + "\n")
    print(Fore.CYAN + "Welcome to Dear Diary\n")
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "Write about your day and make your own life story."
    )
    print(Fore.MAGENTA + "\n" + 50 * "-" + "\n")

    while True:
        print(Fore.GREEN + "What you wanna do today?")
        print(
            Fore.BLUE + "(D)" + Style.RESET_ALL + "isplay Dates to view the diary entry"
        )
        print(Fore.BLUE + "(A)" + Style.RESET_ALL + "dd to your diary")
        print(Fore.BLUE + "(E)" + Style.RESET_ALL + "dit your diary")
        print(Fore.BLUE + "(DL)" + Style.RESET_ALL + "ete the diary")
        print(Fore.BLUE + "(X)" + Style.RESET_ALL + "it the diary")
        user_action = input("\n").strip().upper()

        if user_action == "D":
            dates = display_all_dates()
            if not dates:
                continue
            selected_date = choose_date(dates)
            if selected_date:
                display_diary(selected_date)
        elif user_action == "A":
            add_diary()
        elif user_action == "E":
            dates = display_all_dates()
            if not dates:
                continue
            selected_date = choose_date(dates)
            if selected_date:
                edit_diary(selected_date)
        elif user_action == "DL":
            dates = display_all_dates()
            if not dates:
                continue
            selected_date = choose_date(dates)
            if selected_date:
                del_diary(selected_date)
        elif user_action == "X":
            print(Fore.YELLOW + "Thank you for writing today! See you tomorrow")
            sys.exit("Bye!!")
        else:
            print(Fore.RED + "Invalid choice, choose from D, A, E, DL, X!")


if __name__ == "__main__":
    main()
