#Program for accepting any word and decide whether It is Vowel or consonant
#Anonymous Functions
n=lambda word:"Vowel Word" if not set(word).isdisjoint(set("aeiouAEIOU")) else "Consonant Word"
#Main Program
value=input("Enter Any word: ")
res=n(value)
print("\t{} is {}".format(value,res))