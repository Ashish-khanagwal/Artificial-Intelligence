"""
Protected and Private Methods

1. Protected Methods
- Conventionally indicated by a single underscore prefix: _method_name.
- Meaning: "This method is for internal use only" and should be treated as non-public.
- Not enforced: Protected methods can still be accessed from outside the class, but by convention,
they shouldn’t be.
"""


class Employee:
    def __init__(self, name):
        self.name = name
        self._display_name()  # Called Internally

    def _display_name(self):  # Protected Method
        print(f"Employee name is: {self.name}")


E1 = Employee("Ashish")

"""
2. Private Method
- Indicated by a double underscore prefix: __method_name.
- Name mangling is applied by Python: the method name is internally changed to _ClassName__method_name.
- This makes it harder (but not impossible) to access the method from outside the class.
- Useful for hiding implementation details strictly within the class.
"""


class Employee:
    def __init__(self, name):
        self.name = name

    def __display_name(self):  # Private Method
        print(f"Employee name is {self.name}")

    def show(self):
        # Can call private method inside class
        self.__display_name()


emp = Employee("Alice")
emp.show()  # Works, calls the private method internally

# emp.__display_name()  # AttributeError: 'Employee' object has no attribute '__display_name'

# But can access by name mangling:
# emp._Employee__display_name()  # Works but not recommended


# Example


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount:
            self._balance += amount
            self.__log_transaction("Deposit", amount)
        else:
            print("Deposit amount must be positive")

    def _is_valid_amount(self, amount):  # Protected Method
        return amount > 0

    def __log_transaction(self, transaction_type, amount):  # Private Method
        print(
            f"Logging {transaction_type} of ${amount}. New balance is ${self._balance}"
        )

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 10


account = BankAccount("Ashish", 2000)
account.deposit(4000)
print(BankAccount.is_valid_interest_rate(8))

"""
3. Why Use Protected and Private Methods?

- Protected: Signal to other developers that the method is internal and should not be accessed directly.

- Private: Hide critical implementation details to avoid accidental use or modification.
"""
