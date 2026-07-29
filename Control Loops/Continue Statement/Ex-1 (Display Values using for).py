#Program to Display only PYTON From PYTHON using continue statement
s=input("Enter Any Value: ")
for ch in s:
    print(ch)
else:
    print("-----------------")
for ch in s:
    if ch=="H" or ch=="h":
        continue
    print("\t {}".format(ch),end="")
else:
    print("\n------------------")