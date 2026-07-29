#Program for Demonstrating Inner loops for loop in for loop
for i in range(1,6):
    print("\t Outer Loop: value of i={}".format(i))
    print("------------------------------------------")
    for j in range(1,4):
        print("\t Inner Loop: value of j={}".format(j))
    else:
        print("\t Coming Out of Inner Loop and Going To Outer Loop")
        print("------------------------------------------")
else:
    print("\t Coming Out of Outer Loop")