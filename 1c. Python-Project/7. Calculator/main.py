import sys

HISTORY_FILE = "history.txt"


def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.strip().lstrip("-").isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a valid integer.")


def get_valid_operator():
    valid_ops = ["+", "-", "*", "/"]
    while True:
        op = input("Enter the operator (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")


def show_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            history = f.read()
        if history.strip():
            print("\nCalculation History:\n" + history)
        else:
            print("\nHistory is empty.")
    except FileNotFoundError:
        print("\nNo history found.")


def clear_history():
    with open(HISTORY_FILE, "w") as f:
        pass
    print("History cleared.")


def check_history():
    while True:
        choice = input(
            "Want to check history? (y/n)\nType 'c' to clear the history\n: "
        ).lower()
        if choice == "y":
            show_history()
            break
        elif choice == "c":
            clear_history()
            break
        elif choice == "n":
            print("Okay, no history shown.")
            break
        else:
            print("Please enter 'y', 'n', or 'c'.")


def perform_calculation():
    num1 = get_valid_number("Enter first number: ")
    num2 = get_valid_number("Enter second number: ")
    op = get_valid_operator()

    if op == "/" and num2 == 0:
        print("Error - division by zero is not allowed.")
        return None

    result = None
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2

    print(f"The result of {num1} {op} {num2} is: {result}\n")
    return f"{num1} {op} {num2} = {result}"


def main():
    print("Welcome to the Calculator App!\n")

    while True:
        calculation = perform_calculation()
        if calculation:
            with open(HISTORY_FILE, "a") as file:
                file.write(calculation + "\n")
        check_history()

        while True:
            cont = input(
                "Do you want to calculate more? (Y to continue / Q to quit): "
            ).lower()
            if cont == "y":
                break
            elif cont == "q":
                print("Thank you for using the calculator. Goodbye!")
                sys.exit()
            else:
                print("Please enter 'Y' to continue or 'Q' to quit.")


if __name__ == "__main__":
    main()
