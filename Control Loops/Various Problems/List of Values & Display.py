#program for Accepting List of Values and Display
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter {} value: ".format(i)))
        lst.append(val)
    else:
        print("\t List of values",lst)