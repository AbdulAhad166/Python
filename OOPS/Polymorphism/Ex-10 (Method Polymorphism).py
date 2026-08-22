#Program for Calculating Area of Different Shapes---using super() and Class Name Approach
class Circle:
    def area(self,r):     #Original Method
        self.ac=3.14*r**2
        print("Area of Circle:",self.ac)
        print("---------------------------------------")
class Square:
    def area(self,s):      #Original Method
        self.sa=s*s
        print("Area of Square:",self.sa)
        print("---------------------------------------")
class Rectangle(Square,Circle):
    def area(self,L,B):     #Overridden Method
        self.ra=L*B
        print("Area of Rectangle:",self.ra)
        print("---------------------------------------")
        super().area(float(input("Enter Side of Square: ")))
        Circle.area(self,float(input("Enter Area of Circle: ")))
#Main Program
L=float(input("Enter Length of Rectangle: "))
B=float(input("Enter Breadth of Rectangle: "))
r=Rectangle()   #Object Creation
r.area(L,B)