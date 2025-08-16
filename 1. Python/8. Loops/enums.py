from enum import Enum

line = "********************"
print(line)
print("Enum".center(20))
print(line)


class Status(Enum):
    Pending = 1
    In_progress = 2
    Completed = 3
    Failed = 4


print(Status.Pending)
print(Status.Pending.name)
print(Status.Pending.value)


task_progress = int(input("Enter the progress of the task (1-4): "))
for status in Status:
    if status.value == task_progress:
        print(f"Task status is: {status.name}")
        break
else:
    print("Invalid status entered")
