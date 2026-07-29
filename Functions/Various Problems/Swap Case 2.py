#Program for accepting line of text/word and get its swap case without using upper()and lower()
def readline():
    return input("Enter Any Line of Text/Word: ")
def swapcase():
    line=readline()
    sc=""
    for ch in line:
        if ord(ch) in range(65,91):
            sc=sc+chr(ord(ch)+32)
        elif ord(ch) in range(97,123):
            sc=sc+chr(ord(ch)-32)
        else:
            sc=sc+ch
    else:
        print("Swap Case: ",sc)
#Main Program Calling Function
swapcase()