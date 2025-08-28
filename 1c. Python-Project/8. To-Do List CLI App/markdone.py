def strikethrough(text):
    return "".join(char + "\u0336" for char in text)


def markdone_task():
    data = {}
    with open("tasks.txt") as file:
        for line in file:
            line = line.strip()
            if "->" in line:
                key, value = line.split("->", 1)
                data[key.strip()] = value.strip()

    user_key = input("Enter the task key to strikethrough: ").upper()

    if user_key in data:
        value = data.pop(user_key)
        new_key = strikethrough(user_key)
        new_value = strikethrough(value)
        # Write updated tasks back to tasks.txt (without done task)
        with open("tasks.txt", "w") as file:
            for key, value in data.items():
                file.write(f"{key} -> {value}\n")

        # Append the completed task with strikethrough to completedtask.txt
        with open("completedtask.txt", "a") as file:
            file.write(f"{new_key} -> {new_value}\n")

        print(f"Completed task '{user_key}' moved to completedtask.txt file.")
    else:
        print("Task key not found.")
