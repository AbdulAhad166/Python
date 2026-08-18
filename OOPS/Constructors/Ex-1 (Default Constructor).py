#Program for Creating Default Constructors
class Employee:
    def __init__(self):
        print("I am from Default/Parameter-less Constructor")
        self.sno=100
        self.name="BB"
        print("Employee Number: ",self.sno)
        print("Employee Name: ",self.name)
#Main Program
s1=Employee() #Object Creation-Makes the PVM to call the Default Constructor Implicitly
s2=Employee() #Object Creation-Makes the PVM to call the default Constructor Implicitly