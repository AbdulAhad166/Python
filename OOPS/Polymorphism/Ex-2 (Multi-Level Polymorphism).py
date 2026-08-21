#Program For Using Polymorphism --- Multi-Level Inheritance
class Rectangle:
    def draw(self):
        print("Drawing Rectangle")
class Circle(Rectangle):
    def draw(self):
        print("Drawing Circle")
        super().draw()
class Sqaure(Circle):
    def draw(self):
        print("Drawing Square")
        super().draw()
#Main Program
co=Sqaure()
co.draw()