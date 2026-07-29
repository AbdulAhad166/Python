#Program for Demonstrating Inner loops--while loop in for loop
for i in range(1,6):
    print("\t Outer Loop:val of i={}".format(i))
    print("--------------------------------------")
    j=1
    while j<=3:
        print("\t Inner Loop: val of j={}".format(j))
        j=j+1
    else:
        print("\t Coming Out of Inner Loop Going To Outer Loop")
        print("--------------------------------------")
else:
    print("\t Coming Out of Outer Loop")