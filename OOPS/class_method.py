"""
Class method are methods defined inside the class that are bound to the class
To create a class method, we use a decorator -> classmethod
"""

# class Welcome:
#
#     @classmethod
#     def greet(cls):
#         print(cls)
#         print("Welcome to My Welcome")
#
#
# w1 = Welcome()
# w1.greet()
# print(Welcome)

"""
Output: 
<class '__main__.Welcome'> <<<<------Here the class is passed rather than class object w1. That is Welcome is passed
Welcome to My Welcome
<class '__main__.Welcome'>
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

    @classmethod
    def welcome(cls):
        print(cls)
        print(f"Welcome to {cls.college_name}")

    @classmethod
    def get_department(cls):
        print(f"Department is {cls.college_name} are")
        for department in cls.department:
            print(department)

student1 = Student("Vikas", 31, "66")
student1.welcome()
student1.study(10)
student1.sports("Cricket")
student1.get_department()