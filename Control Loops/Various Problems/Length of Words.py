# Program for accepting a Line of Text and Find Length of Each Word
line=input("Enter A Line of Text: ")
words=line.split()
d={}
for word in words:
    d[word]=len(word)
else:
    for w,wl in d.items():
        print("\t {} ---> {}".format(w,wl))