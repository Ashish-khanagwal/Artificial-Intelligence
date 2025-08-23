"""
Accessing and Modifying Data:

1. Trational way - Make the data private and then use getters and setters
"""

from datetime import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    """
    '_' this single underscore in '_email' means that, attribute is protected. A convention signalling that
    it's for internal use only but still accessible to outside.

    '__' double undescore, Name Mangling makes the attribute private, and harder to access from outside the class,
    but can be accessed within in the same class.

    def clean_email(self):
        return self._email.lower().strip()

    
    Name Mangling - it means that, python automatically changes its name when storing it internally by adding
    _ClassName in front of it. Which makes it harder (but not impossible) to access from outside the class.

    Example if we make 'email' as '__email' then it will be stored as ''_User__email'.
    """

    # Getter Method
    def get_email(self):
        print(f"Email was accessed at {datetime.now()}")
        return self._email

    # Setter Method
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("Ashish", "ashish@gmail.com ", "123")
print(user1.get_email())  # Access with getter method.

user1.set_email("Ashishkhanagwal@gmail.com")  # Modify the object with setter
print(user1.get_email())
"""
_email is accessible outside, see below:-
user1._email = "" --> but we are supposed to not to do that, otherwise there's no point making it 
protected

user1.__email = "" --> Not be able to access the email attribute as it is private and If you try to access 
we will get an error because Python has changed its name behind the scenes.
"""


# Another Example
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # double underscore == private attribute

    def get_balance(self):
        print("Here's your balance")
        return self.__balance

    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Balance can't be negative")


account = BankAccount("Ashish", 10000)
print(account.get_balance())

account.set_balance(100000000000)
print(account.get_balance())
