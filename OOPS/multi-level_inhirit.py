class Vehicle:
    company = "Vikas Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels, with {self.n_seats} seater and provide a mileage of {self.mileage}"


class Car(Vehicle):
    model = "Vartiga_vxi"
    def __init__(self, car_type, drive_type, wheels, seats, mileage):
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(wheels, seats, mileage)

class ElectricCar(Car):
    def __init__(self, car_type, drive_type, wheels, seats, mileage, battery_capacity, distance_range):
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
        super().__init__(car_type, drive_type, wheels, seats, mileage)

    def charge(self):
        print(f"Car is charging until {self.battery_capacity}")


ec1 = ElectricCar("Eletric", "Auto", 4, 7, 25, 82, 200)
print(ec1.__dict__)
