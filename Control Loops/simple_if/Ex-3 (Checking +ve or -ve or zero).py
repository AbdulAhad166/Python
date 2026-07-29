#Program for Accepting any value and Decide weather it is +ve or -ve or zero using simple if
n=int(input("Enter Any Number: "))
if n>0:
    print("\t {} is +VE Number ".format(n))
if n<0:
    print("\t {} is -VE Number ".format(n))
if n==0:
    print("\t {} is Zero ".format(n))