line1 = "***********************"

print(line1)
print("Complex Value".center(23))
print(line1)

z1 = 7 + 3J
z2 = 8 - 5j

print(z1)
print(z2)
print(type(z1))
print(z1.real)
print(z1.imag)

print( z1 + z2 )  # Addition
print( z1 - z2 )  # Subtraction
print( z1 * z2 )  # Multiplication
print( z1 / z2 )  # Division

z = complex(9, 7)
print(z)
print(abs(z))  # Absolute value
print(z.conjugate())  # Conjugate of the complex number

# Mathematical functions from cmath module
import cmath
print("")
print(cmath.phase(z))  # Phase anlge in the radians
print(cmath.polar(z))  # Polar coordinates (magnitude, angle)