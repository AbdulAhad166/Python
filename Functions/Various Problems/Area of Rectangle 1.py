#By using Functions Calculate the Area of Rectangle
def readvals():
    l=float(input("Enter Length of Rectangle: "))
    b=float(input("Enter Breadth of Rectangle: "))
    return l,b
def calarea(l,b):
    return l*b
def dispresult(l,b,ar):
    print("---------------------------------")
    print("\tLength = ",l)
    print("\tBreadth = ",b)
    print("\tArea = ",ar)
    print("---------------------------------")
#Main Program
l,b=readvals()
ar=calarea(l,b)
dispresult(l,b,ar)
