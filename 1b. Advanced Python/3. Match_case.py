# Basic Example

command: str = input("Enter start/stop ")

match command:
    case "start":
        print("Starting..")

    case "stop":
        print("Stopping..")

    case _:
        print("Unknown command")

# Another Example
value = int(input("Enter 1,2,3,10,20: "))
match value:
    case 1 | 2 | 3:
        print("Small numbers")

    case 10 | 20:
        print("Multiple of 10..")

    case _:
        print("Other number")
