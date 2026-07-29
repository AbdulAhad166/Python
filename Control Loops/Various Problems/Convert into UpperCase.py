#program for accepting a Line of Text and Convert into Upper Case without using upper()
n=input("Enter A Line of Text: ")
print("Given Line of Text: ",n)
uc=""
for ch in n:
    if ord(ch) in range(97,123):
        uc=uc+chr(ord(ch)-32)
    else:
        uc=uc+ch
else:
    print("Upper Case Data: ",uc)
