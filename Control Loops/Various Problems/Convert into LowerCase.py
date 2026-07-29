#program for accepting a Line of Text and Convert into Lower Case without lower()
n=input("Enter A Line Text: ")
print("Given Line of Text: ",n)
lc=""
for ch in n:
    if ord(ch) in range(65,90):
        lc=lc+chr(ord(ch)+32)
    else:
        lc=lc+ch
else:
    print("\t Lower Case Data",lc)