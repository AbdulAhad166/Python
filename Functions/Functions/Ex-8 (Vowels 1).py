#Program for accepting any word and decide weather it is vowel word or consonent word
n=lambda word:"Vowel Word" if "a" in word.lower() or "e" in word.lower() or \
"i" in word.lower() or "o" in word.lower() or "u" in word.lower() else "Consonant Word"
#Main Program
word=input("Enter Any Word: ")
res=n(word)
print("\t{} is {}".format(word,res))
