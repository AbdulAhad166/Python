#Program for Generating all Even Numbers In reverse Order within N
n=int(input("Enter How Many Even Numbers Do You Want: "))
if n<=0:
    print("Invalid Input")
else:
    print("Reversed Even Numbers within {}".format(n))
    if n%2!=0:
        n=n-1
    for i in range(n,0,-2):
        print("\t {}".format(i))
    else:
        print("Program Executed")