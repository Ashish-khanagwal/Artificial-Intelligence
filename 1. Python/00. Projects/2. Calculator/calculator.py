import sys


def calc():

    # WELCOME MESSAGE
    print("********************")
    print("Welcome".center(20))
    print("********************")
    print("It's a Calculator, Let's do some calculator\n\n")

    # TAKING INPUTS
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter first number: "))

    print(f"you have entered {num1} and {num2} for the calculation\n")
    print(
        "Now choose the Arithmetic operation you want to perfrom:\n+ for addition\n- for subtraction\n* for multiplication\n/ for division"
    )
    op = input("Enter the operator: ")

    # LOGIC

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error - division by zero")
            return
    else:
        result = "Invalid operator"

    print(f"The result is: {result}\n")

    # START AGAIN
    print("Want to calculate more?\n")

    while True:
        startagain = input("If yes then type Y or\nwant to quite then press Q\n")
        if startagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if startagain.lower() == "y":
        return calc()
    else:
        print("Thank you for using the calculator.")
        sys.exit("bye")


calc()
