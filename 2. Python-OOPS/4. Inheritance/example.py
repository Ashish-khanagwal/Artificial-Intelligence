class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} vehicle is driving")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def drive(self):
        # Extending parent method behavior
        super().drive()
        print(f"{self.brand} {self.model} car is driving smoothly")


car = Car("Toyota", "Corolla")
car.drive()

# Output:
# Toyota vehicle is driving
# Toyota Corolla car is driving smoothly
