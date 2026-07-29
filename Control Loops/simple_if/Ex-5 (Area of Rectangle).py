#Program for cal Area of Rectangle with all test cases
l=float(input("Enter Length of Rectangle: "))
b=float(input("Enter Breadth of Rectangle: "))
if (l>0) and (b>0):
    n=l*b
    print("\t Area of the Rectangle: ",n)
if (l<=0):
    print("\t {} is Invalid length".format(l))
if (b<=0):
    print("\t {} is Invalid breadth".format(b))