"""
Static method - method defined inside a class which is not bound to any thing - class/object
To create a statics method, we use static method decorator.
It don't take any argument, that is fine.
"""

class Student:
    college_name = "Abc college"  # class variables
    department = ["Science", "Arts", "Commerce"]
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    def study(self, n_hours):
        print(f"{self.name} studies for {n_hours} hours.")

    def sports(self, sport):
        print(f"{self.name} plays {sport}.")

    @staticmethod  ####<<<<<Static METHOD >>>>>>
    def welcome():
        print(f"Welcome to college")

    @classmethod
    def get_department(cls):
        print(f"Department is {cls.college_name} are")
        for department in cls.department:
            print(department)



student1 = Student("Vikas", 31, "66")
student1.welcome()