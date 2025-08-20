print("***" + "*" * 24 + "***")
print("Students Score Card".center(30))
print("***" + "*" * 24 + "***")

students = []
marks = []

num_of_students = int(input("How many number of students you want to add: "))


# ENTRIES
def new_entries(num_of_students):
    names_input = input("Enter the student name seperated by comma : ").strip()
    scores_input = input(
        "Enter the respective marks of students seperated by comma: "
    ).strip()

    name_list = [name.strip() for name in names_input.split(",")]
    score_list = [score.strip() for score in scores_input.split(",")]

    # Check if inputs have correct length and scores are digits
    if len(name_list) != num_of_students:
        print("Number of names does not match the specified number of students.")
        return False
    if len(score_list) != num_of_students:
        print("Number of scores does not match the specified number of students.")
        return False
    if not all(score.isdigit() for score in score_list):
        print("All scores must be numeric.")
        return False

    for i in range(num_of_students):
        students.append(name_list[i])
        marks.append(int(score_list[i]))
    return True


new_entries(num_of_students)

record = dict(zip(students, marks))
print(record)

new_list = []


# LOGIC
def scorecard():
    if not marks:  # Check if marks is empty
        print("No student marks available to display.")
        return
    highest_mark = marks[0]
    for h in marks:
        if h > highest_mark:
            highest_mark = h
    for name, score in record.items():
        if score == highest_mark:
            print(f"The highest mark is {highest_mark} scored by {name}")

    lowest_mark = marks[0]
    for l in marks:
        if l < lowest_mark:
            lowest_mark = l
    for name, score in record.items():
        if score == lowest_mark:
            print(f"The lowest mark is {lowest_mark} scored by {name}")

    total = 0
    for i in marks:
        total += i
    average = total / len(marks)
    print(f"Average marks of the class are: {average}")


scorecard()

# REPEAT
while True:
    more = input("Do you want to add more students? (yes/no): ").strip().lower()
    if more == "yes":
        num_input = input("How many more students do you want to add? ").strip()
        if not num_input.isdigit():
            print("Please enter a valid number.")
            continue

        num_of_students = int(num_input)

        success = new_entries(num_of_students)
        if not success:
            continue  # retry if validation fails

        # Update the record dictionary with new data
        record = dict(zip(students, marks))
        print(record)

        # Call scorecard to display updated stats
        scorecard()
    else:
        break

print("Final student records:")
print(record)
