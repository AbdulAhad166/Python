#Program for Using Polymorphism --- Multi-Level Inheritance
class Rectangle:
    def draw(self):            #Original Method
        print("Drawing Rectangle")
class Circle(Rectangle):
    def draw(self):           #Method Overridden
        print("Drawing Circle")
class Square(Circle):
    def draw(self):              #Method Overridden
        print("Drawing Square")
        Rectangle.draw(self)  #Class Name Approach
        Circle.draw(self)     #Class Name Approach
#Main Program
s=Square()
s.draw()