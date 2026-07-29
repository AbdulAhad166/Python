#Program for Calculating Square,Square Root,Cube using Decorator
def cube(calv):
    def calcube():
        n,sqv,sqvrt=calv()
        cbv=n**3
        return n,sqv,sqvrt,cbv
    return calcube
def squareroot(calc):
    def process():
        n,sqv=calc()
        sqvrt=n**0.5
        return n,sqv,sqvrt
    return process
def square(BB):
    def calculation():
        n=BB()
        res=n**2
        return n,res
    return calculation

@cube
@squareroot
@square
def getval():
    return float(input("Enter Any Numerical Value: "))
#Main Program
n,sqv,sqvrt,cbv=getval()
print("Square ({}) = {}".format(n,sqv))
print("Square Root ({}) = {}".format(n,sqvrt))
print("Cube ({}) ={}".format(n,cbv))