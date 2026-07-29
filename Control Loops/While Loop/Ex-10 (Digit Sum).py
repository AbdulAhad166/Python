#program for Accepting a Number and Find Its Digits Sum
n=int(input("Enter Any Digit: "))
if n<=0:
    print("Invalid Input")
else:
    tn=n
    s=0
    while(n>0):
        d=n%10
        s=s+d
        n=n//10
    else:
        print("\t Sum of Digits({})={}".format(tn,s))