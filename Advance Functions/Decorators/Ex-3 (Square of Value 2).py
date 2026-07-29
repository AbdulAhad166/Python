#Program for Calculating Square of Given Number using Decorator
# the symbol of Decorator is @ to be used
def square(BB):
    def calculation():
        n=BB()
        res=n**2
        return n,res
    return calculation
@square                    #Internally PVM Takes as square(getval)
def getval():
    return float(input("Enter Any Number: "))

#Main Program
n,res=getval()             #Normal Function Call
print("Square ({}) = {}".format(n,res))
