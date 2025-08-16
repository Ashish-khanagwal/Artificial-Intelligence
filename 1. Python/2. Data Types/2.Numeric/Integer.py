line1 = "*********************"
line3 = "*    Integer D.T    *"

print(line1)
print(line3)
print(line1)

a = 45
b = -63
c = 32
print(a)
print(b)
print(type(b))
print(a + b)
print(a - b)
print(a * c)
print(a + b / c)

pi = 3.145926
print(pi)
print(abs(pi))
print(round(pi))
print(round(pi, 2))
print(max(45, -45, 30))
print(min(45, -45, 30))

# Type conversion
str = "54"
print(type(str))
num = int(str)
print(type(num))
# print(int("New York")) ----> Error if we attempt to cast incorrect data

# Mathematic functions from math Module 
print("")
import math

print(math.pi)
print(math.ceil(pi)) # Nearest integer greater than or equal to pi
print(math.floor(pi)) # Floor value --> Nearest integer less than or equal to pi
print(math.factorial(5))
print(math.sqrt(144))
print(math.isqrt(144)) # Integer square root
print(math.trunc(pi)) # Truncate to integer