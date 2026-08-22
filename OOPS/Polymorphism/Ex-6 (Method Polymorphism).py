#Program for Calculating Area of Different Shapes---using super() and Class Name Approaches
class Circle:
    def area(self):      #Original Method
        self.c=float(input("Enter The Radius of Circle: "))
        self.ac=3.14*self.c**2
        print("Area of Circle: ",self.ac)
        print("-------------------------------------------")
class Square:
    def area(self):      #Original Method
        self.s=float(input("Enter The Side of Square: "))
        self.sc=self.s*self.s
        print("Area of Square: ",self.sc)
        print("-------------------------------------------")
class Rectangle(Square,Circle):
    def area(self):     #Overridden Method
        self.L=float(input("Enter The Length of Rectangle: "))
        self.B=float(input("Enter The Breadth of Rectangle: "))
        self.ra=self.L*self.B
        print("Area of Rectangle: ",self.ra)
        print("--------------------------------------------")
        super().area()   #super() Name Approach
        Circle.area(self)   #Class Name Approach
#Main Program
r=Rectangle()
r.area()