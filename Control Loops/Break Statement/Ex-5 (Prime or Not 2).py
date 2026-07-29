#program for accepting a Numerical Integer Value and
#Decide whether It is Prime or Not
n=int(input("Enter Any Integer Value to Decide Prime or Not:"))
if n<=1:
    print("\t{} is Invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if n%i==0:
            res=False
            break
    if res:
        print("\t{} is Prime".format(n))
    else:
        print("\t{} is Not Prime".format(n))