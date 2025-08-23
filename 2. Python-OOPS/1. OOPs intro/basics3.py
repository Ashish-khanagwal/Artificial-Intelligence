"""
Accessing and Modigying Data

2. Properties - Python provides a more "Pythonic" and concise way to manage private data while still
supporting encapsulation and validation: the @property decorator. Properties allow you to access getters
and setters as if they are ordinary attributes, making your code cleaner and more readable.
"""

from datetime import datetime


class User:
    def __init__(self, name, email):
        self.name = name
        self._email = email

    """
    You use the @property decorator to define a getter, 
    and then use @<propertyname>.setter for the setter.
    """

    @property
    def email(self):  # Getter method
        print(f"Email was accessed at {datetime.now()}")
        return self._email

    @email.setter
    def email(self, new_email):  # Setter method with validation
        if "@" in new_email:
            self._email = new_email


user1 = User("Ashish", "ashish@gmail.com")
print(user1.email)  # Access like an attribute, but calls the getter

print("")
# Set like an attribute, but calls the setter
user1.email = "Ashish@gmail.com"
print(user1.email)


# Another Example
class Product:
    def __init__(self, model, price):
        self.model = model
        self._price = price

    @property
    def price(self):
        print("Price of the car: ")
        return self._price

    @price.setter
    def price(self, sell_price):
        if sell_price > 2000:
            self._price = sell_price


car = Product("Tesla", 1500)
print(car.price)
car.price = 2500
print(car.price)
