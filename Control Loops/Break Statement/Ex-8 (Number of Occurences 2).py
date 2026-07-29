#program for accepting any word and find Number of Occurences of every letter
word=input("Enter Any Word: ")
d={}
for ch in word:
    if (not ch.isspace()):
        if(ch not in d):
            d[ch]=1
        else:
            d=d[ch]+1
else:
    for letter,count in d.items():
        print(letter,count)