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


c1 = Car(car_type="SUV", drive_type="Manual", wheels=4, seats=7, mileage=25)
print(c1.car_type)

print(c1.company)
print(c1.model)
print(c1.get_details())


"""
The above one is single inheritence

TO make multiple inheritence, you have to define the multiple class in single class: 
class C(A,B)
"""



