"""
Create a class 'Employee' and add Salary and increment properties to it.
"""


class Employee:
    def __init__(self, employee_name, salary):
        self.employee_name = employee_name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, increment):
        if self._salary < 40000:
            self._salary += increment
            print(f"Salary updated to {self._salary}")
        else:
            print("Your salary is good, no increment this year!")


employee1 = Employee("Ashish", 30000)
employee1.salary = 5000
