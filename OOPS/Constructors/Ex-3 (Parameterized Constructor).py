#Program for Creating Parameterized Constructor
class Employee:
    def __init__(self,empno,empname):
        print("I am From Parameterized Constructor")
        self.eno=empno
        self.ename=empname
        print("\t Employee Number: ",self.eno)
        print("\t Employee Name: ",self.ename)
#Main Program
s1=Employee(10,"RS") #Object Creation-Makes the PVM to Call Parameterized Constructor
s2=Employee(20,"TR") #Object Creation-Makes the PVM to Call Parameterized Constructor
s3=Employee(30,"BB") #Object Creation-Makes the PVM to Call Parameterized Constructor 