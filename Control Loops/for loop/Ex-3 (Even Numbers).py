#Program for Generating all Even Numbers within N
n=int(input("Enter How Many Even Numbers Do You Want: "))
if n<=0:
    print("Invalid Input")
else:
    print("Even Numbers within {}".format(n))
    for i in range(1,n+1):
        if i%2==0:
            print("\t {}".format(i))
    else:
        print("Program Executed")