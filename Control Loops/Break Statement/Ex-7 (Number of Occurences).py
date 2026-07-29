#program for accepting any word and find Number of Occurences of every letter
word=input("Enter Any Word: ")
d={}
for ch in word:
    if (ch not in d) and (not ch.isspace()):
        d[ch]=1
    elif (ch in d) and (not ch.isspace()):
        d[ch]=d[ch]+1
else:
    for letter,count in d.items():
        print("\t{} --->{}".format(letter,count))