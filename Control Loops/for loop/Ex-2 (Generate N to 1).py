#program for Generating N to 1 where N is +VE
n=int(input("Enter How Many Numbers Do You Want: "))
if n<=0:
    print("Invalid Input")
else:
    print("Numbers from {} to 1".format(n))
    for i in range(n,0,-1):
        print("\t {}".format(i))
    else:
        print("Program Executed")