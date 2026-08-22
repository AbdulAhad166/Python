#Program for Calculating Area of Different Shapes---using super() and Class Name Approach
class Circle:
    def __init__(self,r):  # original Constructor
        self.ac=3.14*r**2
        print("Area of Circle:",self.ac)
        print("-------------------------------------")
class Square:
    def __init__(self,s): # Original Constructor
        self.sa=s*s
        print("Area of Square:",self.sa)
        print("-------------------------------------")
class Rectangle(Square,Circle):
    def __init__(self,L,B): # Overridden Constructor
        self.ra=L*B
        print("Area of Rectangle:",self.ra)
        print("---------------------------------")
        super().__init__(float(input("Enter Side for Square:")))
        Circle.__init__(self,float(input("Enter Radius of Circle:")))

#Main Program
L=float(input("Enter the Length:"))
B=float(input("Enter the Breadth:"))
ro=Rectangle(L,B) # Object Creation