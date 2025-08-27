# Without Walrus Operator
my_list = [1, 2, 3, 4, 5, 6, 7]
n = len(my_list)

if n > 5:
    print(f"List is too long ({n} elements)")

# With Walrus operator
if (n := len(my_list)) > 5:
    print(f"The list is too long ({n} elements, expected <= 5)")


# More examples
# without walrus
line = input()
while line != "quit":
    print(f"You said {line}")
    line = input()

# with Walrus
while (line := input()) != "quit":
    print(f"You said {line}")

# another example

total = 0
while (num := int(input("Enter a number from (0 to stop)"))) != 0:
    total += num
print(f"Total is {total}")


# Without Walrus


def f(x):
    return x + 1


result = []
for x in range(5):
    y = f(x)
    result.append([y, y**2, y**3])

print(result)

# With walrus

results = [[y := f(x), y**2, y**3] for x in range(5)]
print(results)
