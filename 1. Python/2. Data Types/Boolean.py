line1 = "***********************"

print(line1)
print("Boolean Value".center(23))
print(line1)

isoldEnough = True
if isoldEnough:
    print("You are old enough to vote!")

print(bool(0)) # 0 is considered False (consider as falsy values)
print(bool([])) # Empty list is False
print(bool("Hello")) # Non-empty string is True

age = 18
if age > 18 or age == 18:
    print("You are eligible to vote!")

print(bool(not(0)))
