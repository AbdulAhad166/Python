#Program for Demonstrating Inner loops while loop in while loop
i=1
while i<=5:
    print("\tOuter Loop: Val of i={}".format(i))
    print("------------------------------------------")
    j=1
    while j<=3:
        print("\tInner Loop: Val of j={}".format(j))
        j=j+1
    else:
        i=i+1
        print("\t Coming Out of Inner Loop Going To Outer Loop")
        print("------------------------------------------")
else:
    print("\t Coming Out of Outer Loop")
