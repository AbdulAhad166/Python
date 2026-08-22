#Program for Circle,Square,Rectangle Using Polymorphism --- Multi-Level Inheritance
class Circle:
    def area(self):
        self.c=float(input("Enter The Area of Circle: "))
        self.ac=3.14*self.c**2
        print("Area of Circle: ",self.ac)
        print("--------------------------------------------")
class Square(Circle):
    def area(self):
        self.s=float(input("Enter The Side of Square: "))
        self.sa=self.s*self.s
        print("Area of Square: ",self.sa)
        print("--------------------------------------------")
class Rectangle(Square):
    def area(self):
        self.L=float(input("Enter The Length of Rectangle:  "))
        self.B=float(input("Enter The Breadth of Rectangle: "))
        self.ra=self.L*self.B
        print("Area of Rectangle: ",self.ra)
        print("--------------------------------------------")
        Square.area(self)   #Class Name Approach
        Circle.area(self)   #Class Name Approach
#Main Program
r=Rectangle()
r.area()