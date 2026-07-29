#Program for Accepting any value and Decide weather It is +VE OR -VE OR Zero
n=float(input("Enter Any Value: "))
if (n>0):
    print("\t {} is +VE Number".format(n))
else:
    if (n<0):
        print("\t {} is -VE Number".format(n))
    else:
        print("\t {} is Zero".format(n))