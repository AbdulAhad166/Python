#Program for Calculating Area of Different Shapes---using super() Approach
class Circle:
    def __init__(self):      #Original Constructor
        self.c=float(input("Enter The Radius of Circle: "))
        self.ac=3.14*self.c**2
        print("Area of Circle: ",self.ac)
        print("-------------------------------------------")
class Square:
    def __init__(self):      #Original Constructor
        self.s=float(input("Enter The Side of Square: "))
        self.sc=self.s*self.s
        print("Area of Square: ",self.sc)
        print("-------------------------------------------")
        super().__init__()
class Rectangle(Square,Circle):
    def __init__(self):     #Overridden Constructor
        self.L=float(input("Enter The Length of Rectangle: "))
        self.B=float(input("Enter The Breadth of Rectangle: "))
        self.ra=self.L*self.B
        print("Area of Rectangle: ",self.ra)
        print("--------------------------------------------")
        super().__init__()   #super() Name Approach
#Main Program
r=Rectangle()  #Object Creation
