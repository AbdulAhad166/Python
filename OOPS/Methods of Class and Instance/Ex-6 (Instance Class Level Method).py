#Program for Class Level Method in Instance Method
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON"
        cls.getcity()  #One Class Level Method Calling Another Class Level Method
    @classmethod
    def getcity(cls):
        cls.city="HYDERABAD"
    def readstuddata(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("Enter Student Number: "))
        self.name=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))
        print("-----------------------------------------------------")
    def dispstuddata(self,objinfo):
        Student.getcrs() #Calling Class Level Method From Instance Method
        print("{} Object Information".format(objinfo))
        print("Student Number: {}".format(self.sno))
        print("Student Name: {}".format(self.name))
        print("Student Marks: {}".format(self.marks))
        print("Student Course: {}".format(Student.crs))
        print("Student City: {}".format(Student.city))
#Main Program
s1=Student()
s1.readstuddata("FIRST")
s1.dispstuddata("FIRST")