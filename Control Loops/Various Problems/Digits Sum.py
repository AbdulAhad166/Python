#program for accepting a Number and Find Its Digits Sum
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    s=0
    for d in str(n):
        s=s+int(d)
    else:
        print("Sum of Digits({})={}".format(n,s))