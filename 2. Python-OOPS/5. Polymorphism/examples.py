class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting..")

    def stop(self):
        print("Vehicle is stoping..")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.nuber_of_doors = number_of_doors

    def start(self):
        print("car is starting..")

    def stop(self):
        print("car is stopping..")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):
        print("bike is starting..")

    def stop(self):
        print("bike is stopping..")


vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2018),
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
    # if isinstance(vehicle, Vehicle):
    #     print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    #     vehicle.start()
    #     vehicle.stop()
    # else:
    #     raise Exception("Object is not a valid vehicle")


# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle, Motorcycle):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     else:
#         raise Exception("Object is not a valid vehicle")
