#Program for accepting a line of text/word and get it swap case
#lower to upper or upper to lower
def readline():
    return input("Enter Any Line of Text/Word: ")
def swapcase():
    line=readline()
    sc=""
    for ch in line:
        if ch.isupper():
            sc=sc+ch.lower()
        elif ch.islower():
            sc=sc+ch.upper()
        else:
            sc=sc+ch
    print("Swap Case: ",sc)
#Main Program Function Call
swapcase()