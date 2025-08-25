"""
Create a class with a class attribute a; create an object from it and set "a" directly using object.a = 0.
Does this change the class attribute.
"""


class method:
    a = 4

    def __init__(self):
        pass


met = method()
print(met.a)
met.a = 0  # instance attribute is set to 0

"""
When met.a = 0 is set, it creates a new attribute a only for the met object. 
The original class attribute a inside method stays the same and is not changed. 
Other objects created from the class will still see the class attribute's value unless 
they also set their own a.
"""

print(met.a)  # instance attribute is printed
print(method.a)  # calls the class attribute
