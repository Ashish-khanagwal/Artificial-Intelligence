"""
Static Attributes -
1. Static attributes (also called class variables) are variables defined inside a class but outside any instance methods.
2. These attributes are shared by all instances of the class.
3. They belong to the class itself, not to any individual object.

Usecase -
1. When you want to share data or state common to all instances.
2. Save memory — instead of each instance storing its own copy, all share one variable.
3. Useful for constants or counters that track data globally across instances.
"""


class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")


user1 = User("Ashish", "ashish@gmail.com")
user1.display_user()
user2 = User("Khanagwal", "khanagwal@gmail.com")
user2.display_user()
print(User.user_count)
print(user1.user_count)  # 2
print(user2.user_count)  # 2

# Changing static attribute via the Class
User.user_count = 1
print(user1.user_count)  # 1
print(user2.user_count)  # 1
