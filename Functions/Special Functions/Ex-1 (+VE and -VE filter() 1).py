#Program for accepting list of values and get +ve and -ve using filter()
def pos(n):
    if n>0:
        return True
    else:
        return False
def neg(n):
    if n<0:
        return True
    else:
        return False
#Main Program
print("Enter List of Values Separated by space:\n ")
lst=[float(val) for val in input().split(" ")]
print("Given Values= ",lst)
x=filter(pos,lst) # Here x is an object of type <class, filter>
y=filter(neg,lst) # Here y is an object of type <class, filter>
#Convert Filter Object into List / tuple /set
ps=list(x)
ng=list(y)
print("List of +VE Values= ",ps)
print("List of -VE Values= ",ng)