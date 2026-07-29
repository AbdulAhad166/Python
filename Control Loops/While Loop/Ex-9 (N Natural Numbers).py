#Program for Finding the Sum of N Natural Nums
n=int(input("Enter How Many Natural Numbers Do You Want: "))
if n<=0:
    print("Invalid Input")
else:
    print("Natural Numbers of {}".format(n))
    s=0 #Additive Identity
    i=1
    while i<=n:
        print("\t {}".format(i))
        s=s+i
        i=i+1
    else:
        print("Sum {}".format(s))