"""
Static Method :
- A static method is a method that belongs to a class rather than an instance of the class.
- It does not receive the implicit first argument self (instance) or cls (class).
- Static methods behave like regular functions but belong to the class's namespace.
- They cannot modify object state or class state.
- Used as utility functions related to the class but not dependent on instance or class data.

Use the @staticmethod decorator before the method definition.
"""


class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: {self._balance}")
        else:
            print("Deposit amount must be positive")

    @staticmethod  # Static Method
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("Ashish", 500)
account.deposit(500)
print(
    BankAccount.is_valid_interest_rate(5)
)  # Calling static method without creating an object

"""
When to Use Static Methods?
- When the method performs a task that is related to the class but does not modify or require instance/class 
information.

- Examples: helper functions, utility functions, formatting, calculations, validations that don’t rely on 
object data.
"""
