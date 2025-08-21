from enum import Enum

print("***" + "*" * 30 + "***")
print("Contact Book Management System".center(36))
print("***" + "*" * 30 + "***")

contacts = {}


def add_contact(contacts):
    name = input("Enter name: ").strip().lower()
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"Contact for {name} added/updated.")


def del_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted.")
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


def search_contact(contacts):
    search_name = input("Enter the name to search: ").strip()
    if search_name in contacts:
        print(f"Phone number of {search_name}: {contacts[search_name]}")
    else:
        print(f"{search_name} not found in contact list.")


def contact_input():
    while True:
        choice = input(
            "What do you want to do?\n"
            "1 : to add new contact\n"
            "2 : to search contact\n"
            "3 : to delete contact\n"
            "4 : to display all contacts\n"
            "5 : to exit\n"
        ).strip()

        if choice.isdigit():
            choice_int = int(choice)
            if 1 <= choice_int <= 5:
                return choice_int
            else:
                print("Choose a number from 1 to 5.")
        else:
            print("Please enter a valid number.")


def contact_book():
    global contacts
    while True:
        user_choice = contact_input()
        if user_choice == 1:
            print("New Contact")
            add_contact(contacts)
        elif user_choice == 2:
            print("Searching...")
            search_contact(contacts)
        elif user_choice == 3:
            print("Deleting....")
            del_contact(contacts)
        elif user_choice == 4:
            print("Displaying the contacts")
            display_contacts(contacts)
        elif user_choice == 5:
            print("Exiting program. Goodbye!")
            break


# Start the program
contact_book()
