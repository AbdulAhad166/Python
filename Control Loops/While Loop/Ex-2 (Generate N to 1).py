#Program for Generating N to 1 Where N is Positive
n=int(input("Enter Any Digit: "))
if n<=0:
    print("Invalid Input")
else:
    print("Number within {}:".format(n))
    while n>=1:
        print("\t {} ".format(n))
        n=n-1
