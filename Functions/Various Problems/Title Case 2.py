#program for accepting a Line fo Text and convert it into Title Case
# (Don't use title())
def readline():
    return input("Enter Line of Text:")
def abdtitle():
    line=readline() # One Function Calls another Function--Function Cahin
    words=line.split()
    for index in range(len(words)):
        words[index]=words[index][0].upper()+words[index][1:].lower()
    else:
        print("Title Case="," ".join(words))
#Main Program
abdtitle()