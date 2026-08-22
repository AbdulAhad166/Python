#Program For Circle,Square,Rectangle using Polymorphism --- Multi-Level Inheritance
class Circle:
    def area(self):         #Original Method
        self.r=float(input("Enter The Radius of Circle: "))
        self.ac=3.14*self.r**2
        print("Area of Circle: ",self.ac)
        print("-------------------------------------------")
class Square(Circle):
    def area(self):         #Overridden Method
        self.s=float(input("Enter The Side of The Square: "))
        self.sc=self.s*self.s
        print("Area of Square: ",self.sc)
        print("-----------------------------------------------")
        super().area()      #super() Name Approach
class Rectangle(Square):
    def area(self):          #Overridden Method
        self.L=float(input("Enter The Length of Rectangle: "))
        self.B=float(input("Enter The Breadth of Rectangle: "))
        print("Area of Rectangle: ",self.L*self.B)
        print("------------------------------------------------")
        super().area()   #Calling the Immediate Method using super() Name Approach
#Main Program
r=Rectangle()   #Creating Object
r.area()