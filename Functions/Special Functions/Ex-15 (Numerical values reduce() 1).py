#Program for accepting List of Numerical Values and find their sum bu using reduce()
import functools
def sumop(x,y):
    return x+y
#Main Program
lst=list(map(float,input("Enter List of Values Separated By Comma: ").split(",")))
res=functools.reduce(sumop,lst)
print("Sum= ",res)