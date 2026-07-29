#Program for Accepting a Numerical Value and get its square,square root,cube
#Program for Demonstrating with Non-Decorators (Normal Functions)
def getval():
    return 5
def square():
    n=getval()
    res=n**2
    print("Square of ({})={}".format(n,res))
def squareroot():
    n=getval()
    res=n**0.5
    print("Square Root of ({})={}".format(n,res))
def cube():
    n=getval()
    res=n**3
    print("Cube of({})={}".format(n,res))
#Main Program
square()
squareroot()
cube()