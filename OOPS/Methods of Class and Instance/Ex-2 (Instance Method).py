#Program for Reading the Values of Student Using Classes and Objects
class Student:
    def readstudentdata(self,objinfo):
        print("\t Enter {} Object Information".format(objinfo))
        self.sno=int(input("Enter Student Number: "))
        self.name=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))
    def dispstuddata(self,objinfo):
        print("\t {} Object Information".format(objinfo))
        print("\t Student Number: {}".format(self.sno))
        print("\t Student Name: {}".format(self.name))
        print("\t Student Marks: {}".format(self.marks))
#Main Program
s1=Student()
s2=Student()
print("Content of s1 Object= ",s1.__dict__)
print("Content of s2 Object= ",s2.__dict__)
print("---------------------------------------")
s1.readstudentdata("FIRST")
print("---------------------------------------")
s2.readstudentdata("SECOND")
print("------------------------------------------")
#Display the Object s1 Data
s1.dispstuddata("FIRST")
print("------------------------------------------")
#Display the Object s2 Data
s2.dispstuddata("SECOND")
print("------------------------------------------")