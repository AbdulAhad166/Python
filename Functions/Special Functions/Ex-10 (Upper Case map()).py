#Program for accepting a line of text and convert into upper case using map()
n=input("Enter A Line of Text: ")
uppercase="".join(list(map(str.upper,n)))
print(uppercase)