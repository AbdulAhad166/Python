#Program for Generating all Odd Numbers In reverse Order within N
n=int(input("Enter How Many Odd Numbers Do You Want: "))
if n<=0:
    print("Invalid Input")
else:
    print("Odd Numbers Reversed within {}".format(n))
    if n%2==0:
        n=n-1
    for i in range(n,0,-2):
        print("\t {}".format(i))
    else:
        print("Program Executed")