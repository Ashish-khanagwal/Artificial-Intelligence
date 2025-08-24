print("***" + "*" * 24 + "***")
print("*" + "Encapsulation".center(28) + "*")
print("***" + "*" * 24 + "***")

# Example


class Computer:

    def __init__(self):
        self._processor = "Intel i9"  # Protected Attribute
        self.__ram = 16  # Private Attribute
        self.storage = "512GB SSD"  # Public Attribute

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value):
        if value >= 4:
            self.__ram = value
        else:
            raise ValueError("RAM size too small")


computer = Computer()
print(computer.storage)  # Public attribute - accessible
# print(computer._processor)  # Protected attribute - accessible but discouraged

# Accessing private attribute directly gives error
# print(computer.__ram)     # AttributeError (Name Mangling)

# Access private attribute via getter method
print(computer.ram)

# Changing private attribute via setter method
computer.ram = 32
print(computer.ram)

# computer.ram = 2  # ValueError
# print(computer.ram)
