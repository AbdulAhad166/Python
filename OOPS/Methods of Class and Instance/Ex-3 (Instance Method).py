#Program For Reading the Values of Student Using Classes and Object
class Student:
    def readstudentdata(self,objinfo):
        print("\t Enter {} Object Information".format(objinfo))
        self.sno=int(input("Enter Student Number: "))
        self.name=input("Enter Student Name: ")
        self.marks=float(input("Enter Student Marks: "))
        print("-----------------------------------------------")
        self.dispstuddata(objinfo) #Calling Instance Method From Another Instance Method of Same Class
    def dispstuddata(self,objinfo):
        print("{} Object Information".format(objinfo))
        print("\t Student Number: {}".format(self.sno))
        print("\t Student Name: {}".format(self.name))
        print("\t Student Marks: {}".format(self.marks))

#Main Program
s1=Student()
s2=Student()
#Read The Data For s1 Object and Display its Content
s1.readstudentdata("FIRST")
print("----------------------------------------------")
#Read The Data For s2 Object and Display its Content
s2.readstudentdata("SECOND")