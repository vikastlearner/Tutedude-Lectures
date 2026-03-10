"""
Creating a class and its object
"""

# syntax for class creation: "class MyClass:"

class Student:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    def study(self, n_hours):
        print(f"{self.name} studies for {n_hours} hours.")

    def sports(self, sport):
        print(f"{self.name} plays {sport}.")

student1 = Student("Vikas", 31, "66")
student1.study(10)
student1.sports("Cricket")