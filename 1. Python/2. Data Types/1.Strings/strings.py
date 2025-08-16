line1 = "********************"
line3 = "*    String D.T    *"

print(line1)
print(line3)
print(line1)

# String Data Type
firstname = "Ashish"
lastname = "Khanagwal"
print(firstname)
print(type(firstname))
print(type(firstname) == str)
print(isinstance(firstname, str))

print('')

# Constructor Function
pizza = str("Pepperoni")
print(pizza)
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Accessing Characters
language = "Japanese"
print(language[0])  # First character
print(language[1])  # Second character
print(language[2])  # Third character

print(language[-1])  # Last character
print(language[-2])  # Second last character

# String Slicing
word = "Artificial Intelligence"
# string[start:end:step]
print(len(word))  # Length of the string
print(word[5:14:])
print(word[:23:2])

# Concatenation
fullname = firstname + " " + lastname
print(fullname)
age = 24
sentence = "My name is: " + fullname + " and I am " + str(age) + " Years old"
print(sentence)
# this str(age) is known as typecasting (integer to string)

# Multiline string
multiline = '''
Hey Mate!
How are you doing?
                        all good!
                        What about you?
'''
print(multiline)

# Escaping special characters
sentence_2 = 'I\'m back at work!\n\t\t\tHey!\n\nWhere\'s this at\\located'
print(sentence_2)
# \ (backslash to escape characters)
# \t (tab)
# \n (newline)
# \\ (to add a backslash)

# String methods
print("\nString methods")
print(firstname)
print(firstname.upper())  # Convert to uppercase
print(firstname.lower())  # Convert to lowercase
print(firstname.title())  # Convert to title case

print(len(multiline))  # Length of the multiline string
print(multiline.title())  # Convert to title case
print(multiline.replace("good", "okay"))
print(multiline)
print(len(multiline.strip()))  # Remove leading and trailing whitespace
print(len(multiline))

multiline += "          " # Adding whitespace at the end
print(len(multiline))
multiline = "             " + multiline # Adding whitespace at the beginning
print(len(multiline))
print(len(multiline.strip()))  # After stripping whitespace
print(len(multiline.rstrip()))  # Remove trailing whitespace
print(len(multiline.lstrip()))  # Remove leading whitespace
