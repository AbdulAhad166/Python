#Program for Finding the Sum of Square and Cubes N Natural Nums
n=int(input("Enter How Many Natural Numbers Do You Want: "))
if n<=0:
    print("Invalid Input")
else:
    s=0
    ss=0
    cs=0
    print("\tNatNum\tSquares\tCubes")
    for i in range(1,n+1):
        print("\t {} \t {} \t {}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i
        cs=cs+i
    else:
        print("\t{}\t\t{}\t{}".format(s,ss,cs))

