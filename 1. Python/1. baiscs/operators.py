print((5 > 3) and (3 < 1))
print(3 == 3)
print(not(3 == 3))

x = 3
x += 3
print(x)

x *= 2
print(x)

x **= 2  # (Exponentiation/power)
print(x)

# x /= 12 => 12.0 (True Division)

# x //= 12 => 12 (Floor Division)

# x %= 12 => 0 (Remainder)
print(x)

print('')
line1 = "*    Memborship Operators (in/not in)    *"
print(line1)
print("a" in "apple")
print("b" not in "apple")

print('')
line2 = "*    Identity Operators (is/is not)    *"
print(line2)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is c)

print('')
line3 = "*    Example    *"
age = 24
if (age >= 18) :
  print("You can vote") 
else :
  print("You cannot vote")

print("*   Ternary Operator   *")
print("You can vote") if (age >= 18) else print("You cannot vote")