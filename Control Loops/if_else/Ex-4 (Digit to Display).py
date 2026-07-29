#program for accepting any Digit and Display Its Name
d=int(input("Enter Any Number: "))
if (d==0):
    print("\t {} is Zero".format(d))
else:
    if (d==1):
        print("\t {} is One".format(d))
    else:
        if (d==2):
            print("\t {} is Two".format(d))
        else:
            if (d==3):
                print("\t {} is Three".format(d))
            else:
                if (d==4):
                    print("\t {} is Four".format(d))
                else:
                    if (d==5):
                        print("\t {} is Five".format(d))
                    else:
                        if (d==6):
                            print("\t {} is Six".format(d))
                        else:
                            if (d==7):
                                print("\t {} is Seven".format(d))
                            else:
                                if (d==8):
                                    print("\t {} is Eight".format(d))
                                else:
                                    if (d==9):
                                        print("\t {} is Nine".format(d))
                                    else:
                                        if (d>9):
                                            print("\t {} is +VE Number".format(d))
                                        else:
                                            if (d<0) and (-9<d<-1):
                                                print("\t {} is -VE Digit")
                                            else:
                                                print("\t {} is -VE Number".format(d))

