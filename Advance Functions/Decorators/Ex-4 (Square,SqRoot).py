#Program for Calculating Square and Square Root of Given Values using Decorator
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
@squareroot
@square
def getval():
    return float(input("Enter Any Number: "))
#Main Program
n,sqv,sqvrt=getval()
print("Square ({}) = {}".format(n,sqv))
print("Square Root ({}) = {}".format(n,sqvrt))
