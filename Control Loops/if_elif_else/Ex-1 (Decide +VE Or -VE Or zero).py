#Program for Accepting any value and Decide weather It is +VE OR -VE OR Zero using elif
n=int(input("Enter Any Number: "))
if n>0:
    print("\t {} is +VE Number".format(n))
elif n<0:
    print("\t {} is -VE Number".format(n))
else:
    print("\t {} is Zero".format(n))
