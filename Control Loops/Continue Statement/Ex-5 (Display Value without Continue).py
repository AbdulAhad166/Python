# Program to Display PYTON From PYTHON using pass
s = input("Enter Any Value: ")
for ch in s:
    print("\t{}".format(ch))
print("----------------")
for ch in s:
    if ch in "hH":
        pass
    else:
        print(ch, end="")
print()
print("----------------")