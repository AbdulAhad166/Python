#Program for accepting a Line of Text and Find Number chars without spaces (Don't use spaces)
s=input("Enter a Line of Text: ")
L=0
for ch in s:
    L=L+1
else:
    print("Given String Length: ",s)
    print("Length of Given String Without Spaces: ",L)
#code for length of given string without spaces
L=0
nsp=0
for ch in s:
    if not ch.isspace():
        L=L+1
    else:
        nsp=nsp+1
else:
    print("Given String Length: ",s)
    print("Length of Given String Without Spaces: ",L)
    print("Number of Spaces Contains: ",nsp)

