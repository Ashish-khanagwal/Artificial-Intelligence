print("***" + "*" * 24 + "***")
print("*" + "Encapsulation".center(28) + "*")
print("***" + "*" * 24 + "***")


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insuficient Funds.")
        self._balance -= amount


account = BankAccount()
print(account.balance)
account.deposit(200)
print(account.balance)
account.withdraw(100)
print(account.balance)
