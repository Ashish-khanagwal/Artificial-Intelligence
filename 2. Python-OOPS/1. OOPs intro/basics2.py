"""
Accessing and Modifying Data:
Trational way - Make the data private and then use getters and setters

"""


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
    
    Name Mangling - it means that, python automatically changes its name when storing it internally by adding
    _ClassName in front of it. Which makes it harder (but not impossible) to access from outside the class.

    Example if we make 'email' as '__email' then it will be stored as ''_User__email'.
    """

    def clean_email(self):
        return self._email.lower().strip()


user1 = User("Ashish", "  AshisH@gmail.com ", "123")
print(user1.clean_email())

"""
_email is accessible outside, see below:-
user1._email = "" --> but we are supposed to not to do that, otherwise there's no point making it 
protected

user1.__email = "" --> Not be able to access the email attribute as it is private and If you try to access 
we will get an error because Python has changed its name behind the scenes.
"""
