#Program for Checking whether a given number is Spy Number or Not
n=int(input("Enter Any Number: "))
if n<=0:
    print("\t Invalid Input")
else:
    s=0
    p=1
    for d in str(n):
        s=s+int(d)
        p=p*int(d)
    print("\t Sum of Given Value =",s)
    print("\t Product of Given Value =",p)
    if s==p:
        print("\t {} is a spy Number".format(n))
    else:
        print("\t {} is not a spy Number".format(n))
