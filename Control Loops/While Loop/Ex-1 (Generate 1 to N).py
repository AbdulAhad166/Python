#program for generating 1 to N where N is Positive
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    print("Number Within {}: ",n)
    i=1
    while i<=n:
        print("\t {}".format(i))
        i=i+1
    else:
        print("Program Executed")