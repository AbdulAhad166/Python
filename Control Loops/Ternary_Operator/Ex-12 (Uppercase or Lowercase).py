#program to check whether a character is uppercase or lowercase using the if..else operator.
ch=input("Enter a character: ")
res="Upper Case" if ch.isupper() else "Lower Case"
print(res)