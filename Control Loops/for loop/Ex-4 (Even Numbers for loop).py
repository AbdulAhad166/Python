#program for Generating  All Even Numbers within N use only for loop
n=int(input("Enter How Many Numbers Do Yu Want: "))
if n<=0:
    print("Invalid Input")
else:
    print("Even Numbers within {}".format(n))
    for i in range(2,n+1,2):
        print("\t {}".format(i))
    else:
        print("Program Executed")