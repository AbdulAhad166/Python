#Program to Display PYTON From PYTHON using while loop with continue
s=input("Enter Any Value: ")
i=0
while i<len(s):
    print("\t {}".format(s[i]))
    i=i+1
else:
    print("\n---------------------")
i=0
while i<len(s):
    if s[i]=="H" or s[i]=="h":
        i=i+1
        continue
    print("\t {}".format(s[i]),end="")
    i=i+1
else:
    print()
    print("\n---------------------")