#Student.py<---File Acts As Module Name
from Univ import Univ
from College import College
class Student(College):
    def getdata(self):
        self.sno=int(input("Enter Student Number: "))
        self.sname=input("Enter Student Name: ")
        self.crs=input("Enter Student Course: ")
        super().getdata()
    def dispdata(self):
        Univ.dispdata(self)
        College.dispdata(self)
        print("-"*50)
        print("Student Details")
        print("-"*50)
        print("Student Number: ",self.sno)
        print("Student Name:",self.sname)
        print("Student Course:",self.crs)
        print("-"*50)