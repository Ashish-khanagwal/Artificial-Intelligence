# Create a Class "Programmer" for storing information of few programmers working at microsoft.


class Programmer:
    company = "Microsoft"

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def display_info(self):
        print(
            f"{self.name} is working at {Programmer.company} on role of {self.role} with salary (Lpa): {self.salary}"
        )


employee1 = Programmer("Ashish", "DevOps Engineer", 2500000)
employee1.display_info()

employee2 = Programmer("Manish", "App Developer", 2500000)
employee2.display_info()
