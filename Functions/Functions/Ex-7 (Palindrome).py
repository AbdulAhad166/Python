#Program for accepting any Value and Decide whether It is Palindrome or not
#Anonymous Functions
palindrome=lambda val:"Palindrome" if val==val[::-1] else "Not Palindrome"
#Main Program
value=input("Enter Any Value: ")
res=palindrome(value)
print("\t{} is {}".format(value,res))