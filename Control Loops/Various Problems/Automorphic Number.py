#Program to check whether a given Number is Automorphic Number or Not
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    sq=n*n
    if str(sq).endswith(str(n)):
        print("\t {} is a Automorphic Number".format(n))
    else:
        print("\t {} is not a Automorphic Number".format(n))


