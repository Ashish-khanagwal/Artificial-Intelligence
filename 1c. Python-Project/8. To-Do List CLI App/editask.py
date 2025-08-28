def edit_task():
    with open("tasks.txt", "r") as file:
        lines = file.readlines()

    print("Current tasks:")
    for line in lines:
        print(line.strip())

    user_key = input("Enter the task key you want to edit: ").upper()
    found = False

    for i, line in enumerate(lines):
        if "->" in line:
            key, value = line.split("->", 1)
            if key.strip().upper() == user_key:
                found = True
                choice = input("Edit (K)ey or (V)alue? ").strip().upper()

                if choice == "K":
                    new_key = input("Enter the new key: ").strip().upper()
                    # Replace key only, keep value same
                    lines[i] = f"{new_key} ->{value}"
                elif choice == "V":
                    new_value = input("Enter the new value/description: ").strip()
                    # Replace value only, keep key same
                    lines[i] = f"{key.strip()} -> {new_value}\n"
                else:
                    print("Invalid choice.")
                break

    if not found:
        print("Task key not found.")
        return

    # Write all lines back to the file
    with open("tasks.txt", "w") as file:
        file.writelines(lines)

    print("Task updated successfully.")
