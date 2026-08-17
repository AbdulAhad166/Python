#Program for Demonstrating Instance Method and 'self'
class Student:
    def readstudentdata(self):
        print("In readstudentdata(), Address of Current Object: ",id(self))
#Main Program
s1=Student()   #Created the object
print("Main Program: Memory Address of s1 Object= ",id(s1))
s1.readstudentdata()  #Function Call
print("--------------------------------------------------")
s2=Student()
print("Main Program: Memory Address of s2 Object= ",id(s2))
s2.readstudentdata()