import sys

from editask import edit_task
from markdone import markdone_task


def view_task():
    try:
        with open("tasks.txt") as file:
            content = file.read()
            if content.strip():
                print("Current tasks:\n" + content)
            else:
                print("No task found!! Start adding!")

    except FileNotFoundError:
        print("No tasks.txt file found, start by adding a tasks.")


def add_task():
    with open("tasks.txt", "a") as file:
        add_task_key = input("Heading of the task:\n").strip().upper()
        add_description = input("Enter the description of the task\n").strip()
        if not add_task_key or not add_description:
            print("Both heading and description are required.")
            return
        existing_keys = set()
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    if "->" in line:
                        key, _ = line.split("->", 1)
                        existing_keys.add(key.strip().upper())
        except FileNotFoundError:
            pass  # File may not exist yet

        if add_task_key in existing_keys:
            print(
                f"Task heading '{add_task_key}' already exists. Use edit to modify it."
            )
            return edit_task()

        with open("tasks.txt", "a") as file:
            file.write(f"{add_task_key} -> {add_description}\n")
        print(f"Task '{add_task_key}' added successfully.")


def del_task():
    data = {}
    try:
        with open("tasks.txt") as file:
            for line in file:
                line = line.strip()
                if "->" in line:
                    key, value = line.split("->", 1)
                    data[key.strip()] = value.strip()
    except FileNotFoundError:
        print("Tasks.txt not found!")
    task_delete = (
        input("Enter the heading of the task you want to delete. ").strip().upper()
    )
    if task_delete in data:
        del data[task_delete]
        with open("tasks.txt", "w") as file:
            for key, value in data.items():
                file.write(f"{key} -> {value}\n")
        print(f"Task {task_delete} deleted")
    else:
        print("Not task found!")


def main():
    while True:
        print("\nType a command:")
        print("(V)iew tasks")
        print("(A)dd a task")
        print("(D)elete a task")
        print("(MD) Mark task as done")
        print("(E)dit a task")
        print("(Q)uit")

        user_input = input("Your choice: ").strip().lower()

        if user_input == "v":
            view_task()
        elif user_input == "a":
            add_task()
        elif user_input == "d":
            del_task()
        elif user_input == "md":
            markdone_task()
        elif user_input == "e":
            edit_task()
        elif user_input == "q":
            print("Thank you for using TO-DO CLI APP!! Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter one of V, A, D, MD, E, Q.")


if __name__ == "__main__":
    main()
