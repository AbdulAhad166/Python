#Program For Using Polymorphism --- Single Inheritance
class Rectangle:
    def draw(self):         #Original Method
        print("Drawing Rectangle")
class Circle(Rectangle):
    def draw(self):          #Method Overridden
        print("Drawing Circle")
#Main Program
co=Circle()
co.draw()