#Program For Finding University,College,Student Using Polymorphism--super() and Class Name Approaches
class Univ:
    def getdata(self):   #Original Method
        self.uname=input("Enter University Name: ")
        self.uloc=input("Enter University Location: ")
    def dispdata(self):       #Original Method
        print("-"*50)
        print("University Details")
        print("-"*50)
        print("University Name: ",self.uname)
        print("University Location: ",self.uloc)
        print("-"*50)
class College(Univ):
    def getdata(self):         #Overridden Method
        self.cname=input("Enter College Name: ")
        self.cloc=input("Enter College Location: ")
        super().getdata()
    def dispdata(self):         #Overridden Method
        print("-"*50)
        print("College Details")
        print("-"*50)
        print("College Name: ",self.cname)
        print("College Location: ",self.cloc)
        print("-"*50)
class Student(College):
    def getdata(self):      #Overridden Method
        self.sno=int(input("Enter Student Number: "))
        self.sname=input("Enter Student Name: ")
        self.crs=input("Enter Student Course: ")
        super().getdata()
    def dispdata(self):       #Overridden Method
        Univ.dispdata(self)
        College.dispdata(self)
        print("-"*50)
        print("Student Details")
        print("-"*50)
        print("Student Number: ",self.sno)
        print("Student Name: ",self.sname)
        print("Student Course: ",self.crs)
        print("-"*50)
#Main Program
s=Student()  #Object Creation
s.getdata()
s.dispdata()
