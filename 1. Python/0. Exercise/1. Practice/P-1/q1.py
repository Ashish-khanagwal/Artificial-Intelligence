# Write a program using functions to find greatest of three numbers.


def biggest(a, b, c):
    max = a
    if b > a:
        if b > c:
            max = b
        else:
            max = c
        return max
    elif c > a:
        if c > b:
            max = c
        else:
            max = b
        return max
    else:
        return max


print("ashish khanagwal")

a, b, c = map(int, input("Enter 3 numbers seprated by space: ").split())
print(biggest(a, b, c))
