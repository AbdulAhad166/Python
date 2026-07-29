#program for accepting any Digit and Display Its Name
n=int(input("Enter Any Number: "))
if (n==0):
    print("\t {} is Zero".format(n))
if (n==1):
    print("\t {} is One".format(n))
if (n==2):
    print("\t {} is Two".format(n))
if (n==3):
    print("\t {} is Three".format(n))
if (n==4):
    print("\t {} is Four".format(n))
if (n==5):
    print("\t {} is Five".format(n))
if (n==6):
    print("\t {} is Six".format(n))
if (n==7):
    print("\t {} is Seven".format(n))
if (n==8):
    print("\t {} is Eight".format(n))
if (n==9):
    print("\t {} is Nine".format(n))
if (n>9):
    print("\t {} is Positive Number".format(n))
if (n<0) and n in range(-1,-10,-1):
    print("\t {} is Negative Digit".format(n))
if (n<0) and n not in range(-1,-10,-1):
    print("\t {} is Negative Number".format(n))
