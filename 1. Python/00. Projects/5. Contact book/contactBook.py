from enum import Enum

print("***" + "*" * 30 + "***")
print("Contact Book Management System".center(36))
print("***" + "*" * 30 + "***")

name = []
phone_number = []


def contact_book():
    class status(Enum):
        ADD_NEW_CONTACT = 1
        SEARCH_CONTACT = 2
        DELETE_CONTACT = 3
        DISPLAY_CONTACT = 4

    choice = [1, 2, 3, 4]
    user_choice = input(
        "What do you want to do?\n1 : to add new contact\n2 : to search contact\n3 : to delete contact\n4 : to display all contact\n"
    ).strip()

    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice not in choice:
            print(f"Choose from {choice} in order to perfrom the action.")
    else:
        print("Please enter a valid number")

    if user_choice == 1:
        print("New Contact")
    elif user_choice == 2:
        print("Searching...")
    elif user_choice == 3:
        print("Deleting....")
    elif user_choice == 4:
        print("Displaying the contacts")


contact_book()
