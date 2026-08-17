#Program for Demonstrating The Functionality of Class Level Method
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON"
        cls.getcity()
    @classmethod
    def getcity(cls):
        cls.city="HYDERABAD"
#Main Program
Student.getcrs()  #Calling Class Level Method
print("Student Course= ",Student.crs)
print("Student Course= ",Student.city)