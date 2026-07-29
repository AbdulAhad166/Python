#Program for Demonstrating Inner loops--for loop in while loop
i=1
while i<=5:
    print("\tOuter Loop: val of i={}".format(i))
    print("---------------------------------------")
    for j in range(1,4):
        print("\tOuter Loop: val of j={}".format(j))
    else:
        i=i+1
        print("\t Coming Out of Inner Loop Going to Outer Loop")
        print("---------------------------------------")
else:
    print("\t Coming Out of Outer Loop")
