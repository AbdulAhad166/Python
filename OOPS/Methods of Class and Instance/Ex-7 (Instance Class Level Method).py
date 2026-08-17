#Program for Instance Method in Class Level Method
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON"
        cls.getcity()  #One Class Level Method Calling Another Class Level Method
    @classmethod
    def getcity(cls):
        cls.city="HYDERABAD"
        #Create An Object for s1
        s1=Student()
        s1.readstuddata("FIRST") #Calling Instance Method From Class Level Method
    def readstuddata(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("Enter Student Number: "))
        self.name=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))
        print("-----------------------------------------------------")
        self.dispstudata(objinfo) #One Instance Method Calling Another Insatnce Method
    def dispstudata(self,objinfo):
        print("{} Object Information".format(objinfo))
        print("Student Number= {}".format(self.sno))
        print("Student Name= {}".format(self.name))
        print("Student Marks= {}".format(self.marks))
        print("Student Course= {}".format(Student.crs))
        print("Student City= {}".format(Student.city))
#Main Program
Student.getcrs()