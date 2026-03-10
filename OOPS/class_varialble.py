"""
Class variable are defined at class level and is shared among objects
"""


class Student:

    college_name = "Abc college"  #class variables
    department = ["Science", "Arts", "Commerce"]

    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    def study(self, n_hours):
        print(f"{self.name} studies for {n_hours} hours.")

    def sports(self, sport):
        print(f"{self.name} plays {sport}.")


student = Student("Vikas", 21, "10")
