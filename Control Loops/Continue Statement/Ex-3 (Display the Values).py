#Program for Displaying PTON From PYTHON using continue statement
s=input("Enter Any Value: ")
for ch in s:
    print("\t {}".format(ch))
else:
    print("\n-------------------")
for ch in s:
        if not set(ch).isdisjoint(set("YHyh")):
            continue
        print("\t {}".format(ch),end="")
else:
    print()
    print("\n-------------------")

