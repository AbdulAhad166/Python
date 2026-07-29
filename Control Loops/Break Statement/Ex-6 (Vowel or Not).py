#program for accepting a word and
#Decide whether It is Vowel or Not
w=input("Enter Any Word: ")
res="Not Vowel Word"
for ch in w:
    if ch in "aeiouAEIOU":
        res="Vowel Word"
        break
print("\t {} is {}".format(w,res))