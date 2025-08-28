import sys

from editask import edit_task
from markdone import markdone_task


def view_task():
    with open("tasks.txt") as file:
        content = file.read()
        print(content)


def add_task():
    with open("tasks.txt", "a") as file:
        add_tasks = input("Heading of the task:\n").upper()
        add_description = input("Enter the description of the task\n")
        file.write(f"{add_tasks} -> {add_description}\n")


def del_task():
    data = {}
    with open("tasks.txt") as file:
        for line in file:
            line = line.strip()
            if "->" in line:
                key, value = line.split("->", 1)
                data[key.strip()] = value.strip()
    try:
        task_delete = input(
            "Enter the heading of the task you want to delete. "
        ).upper()
        del data[task_delete]
    except KeyError:
        print("Not in the tasks!")
    else:
        print("Task deleted")
        with open("tasks.txt", "w") as file:
            for key, value in data.items():
                file.write(f"{key} -> {value}\n")


def main():
    user_input = input(
        "Type\n(V): View\n(A): Add\n(D): Delete\n(MD): Done\n(E): Edit\n"
    ).strip()

    if user_input.lower() == "v":
        view_task()
    elif user_input.lower() == "a":
        add_task()
    elif user_input.lower() == "d":
        del_task()
    elif user_input.lower() == "md":
        markdone_task()
    elif user_input.lower() == "e":
        edit_task()
    else:
        print("Invalid choice. Please enter one of V, A, D, MD, E.")

    print("Want to keep exploring?")
    while True:
        user_explore = input("(y/n): ")
        if user_explore.lower() not in ["y", "n"]:
            continue
        else:
            break
    if user_explore.lower() == "y":
        return main()
    else:
        print("Thank you for using TO-DO CLI APP!!")
        sys.exit("Bye!!")


if __name__ == "__main__":
    main()
