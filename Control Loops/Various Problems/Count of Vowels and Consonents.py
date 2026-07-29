#Program to Take a Line of Text and count how many vowels and consonents are present
n=input("Enter A Line of Text: ")
vowels=0
consonents=0
for ch in n:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels=vowels+1
        else:
            consonents=consonents+1
print("\t vowels ={}".format(vowels))
print("\t consonents ={}".format(consonents))