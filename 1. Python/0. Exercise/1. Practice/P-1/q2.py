# write a python program to convert celsius to fahrenheit
# F = C * 1.8 + 32


def conversion(c):
    f = c * 1.8 + 32
    return f


c = int(
    input("Enter the temperature in celsius you want to convert in fahrenhiet to: ")
)
farhenheit_temp = conversion(c)
print(f"The converted temperature into fahrenheit is: {farhenheit_temp}°C")
