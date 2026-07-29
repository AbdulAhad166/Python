#program for Cal Factorial of a Number
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    else:
        print("\t Factorial ({})={}".format(n,fact))