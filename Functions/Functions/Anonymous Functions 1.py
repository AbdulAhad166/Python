#Program for Adding Two Values
addon=lambda a, b: a + b
#Main Program
print("Enter Two Values: ")
a,b=float(input()),float(input())
res=addon(a, b)
print("Sum({},{})={}".format(a,b,res))