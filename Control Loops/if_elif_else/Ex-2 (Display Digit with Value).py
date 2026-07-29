#program for accepting any Digit and Display Its Name
n=int(input("Enter Any Digit: "))
if (n==0):
    print("\t {} is Zero".format(n))
elif (n==1):
    print("\t {} is One".format(n))
elif (n==2):
    print("\t {} is Two".format(n))
elif (n==3):
    print("\t {} is Three".format(n))
elif (n==4):
    print("\t {} is Four".format(n))
elif (n==5):
    print("\t {} is Five".format(n))
elif (n==6):
    print("\t {} is Six".format(n))
elif (n==7):
    print("\t {} is Seven".format(n))
elif (n==8):
    print("\t {} is Eight".format(n))
elif (n==9):
    print("\t {} is Nine".format(n))
elif (n>9):
    print("\t {} is +VE Number".format(n))
elif (n<0) and n in range(-9,-1):
    print("\t {} is -VE Digit".format(n))
elif (n<0) and n not in range(-9,-1):
    print("\t {} is -VE Number".format(n))