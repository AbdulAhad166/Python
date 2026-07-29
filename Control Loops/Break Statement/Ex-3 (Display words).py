#Program for displaying only MISS in MISSISSIPPI without using Indexing and Slicing
s=input("Enter Any Value: ")
for ch in s:
    print("\t {}".format(ch))
ictr=0
for ch in s:
    if ch=="I":
        ictr=ictr+1
        if ictr==2:
            break
    print(ch,end="")
else:
    print("-----------------------")
