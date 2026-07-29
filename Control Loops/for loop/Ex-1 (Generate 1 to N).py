#program for Generating 1 to N where N is +VE
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Number")
else:
    print("\t Numbers within:{}".format(n))
    for i in range(1,n+1):
        print("\t {}".format(i))
    else:
        print("\t Program Executed")