#Program for calculating Square of Given Number using Decorator
def square(BB):
    def calculation():
        n=BB()
        result=n**2
        return n,result
    return calculation
def getval():
    return float(input("Enter Any Number: "))
#Main Program
cal=square(getval)
n,result=cal()
print("Square ({}) = {}".format(n,result))