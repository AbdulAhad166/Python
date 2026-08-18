#Program For Creating Both Default and Parameterized Constructor by Calling Both Constructors
class Test:
    def __init__(self,a=1,b=2):  #Default Cum Parameterized Constructor
        print("I am from Default/Parameterized Constructor")
        self.a=a
        self.b=b
        print("\t Value of a: ",self.a)
        print("\t Value of b: ",self.b)
#Main Program
t1=Test() #Object Creation-Makes The PVM to Call Default Constructor
t2=Test(10,20) #Object Creation-Makes the PVM to Call Parameterized Constructor Implicitly
t3=Test(100,200) #Object Creation-Makes the PVM to Call Parameterized Constructor Implicitly
t4=Test(b=20) #Object Creation-Makes the PVM to Call Parameterized Constructor Implicitly
t5=Test(b=1000,a=2000) #Object Creation-Makes the PVM to Call Parameterized Constructor Implicitly