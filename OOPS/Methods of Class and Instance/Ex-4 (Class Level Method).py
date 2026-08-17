#Program for Demonstrating The Functionality of Class Level Method
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON"  #OR Student.crs="PYTHON"
    @classmethod
    def getcity(cls):
        cls.city="HYDERABAD"   #OR Student.city="HYDERABAD"
#Main Program
Student.getcrs()  #Calling Class Level Method
Student.getcity()  #Calling Class Level Method
print("Student Course= ",Student.crs)
print("Student City= ",Student.city)