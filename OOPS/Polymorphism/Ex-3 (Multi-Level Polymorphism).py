#Program for Using Polymorphism --- Multi-Level Inheritance
class Rectangle:
    def draw(self):
        print("Drawing Rectangle")
class Circle(Rectangle):
    def draw(self):
        print("Drawing Circle")
class Square(Circle):
    def draw(self):
        print("Drawing Square")
        Rectangle.draw(self)
        Circle.draw(self)
#Main Program
s=Square()
s.draw()