#Program for accepting line of text/word to title case first letter will be upper and other are lower
def readline():
    return input("Enter Any Line of Text/Word: ")
def abdtitle():
    line=readline()    #One Function Calls Another Function
    words=line.split()
    tc=""
    for word in words:
        tc=tc+word[0].upper()+word[1:].lower()
    else:
        print(tc)
#Main Program
abdtitle()