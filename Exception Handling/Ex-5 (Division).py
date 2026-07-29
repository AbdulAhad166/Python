#Program for Demonstrating Exception occurrence 
#Exception Handling Concept
try:
    a=input("Enter First Number: ")
    b=input("Enter Second Number: ")
    x=int(a)   #Exception Generated Statements ---ValueError
    y=int(b)   #Exception Generated Statements ---ValueError
    z=x/y      #Exception Generated Statements ---ValueError
except (ZeroDivisionError,ValueError):   #Multi Exception Handling Block
    print("\t Do Not Enter Denominator as Zero")
    print("\t Do Not Enter Alnums,str,Symbols")
else:      #Here else Block is optional for better clarity of getting the result we use else block
    print("\t First Number= {}".format(x))
    print("\t Second Number= {}".format(y))
    print("\t Division= {}".format(z))
finally:   #Here finally block is also optional for getting the program is executed or not we use finally block
    print("\t Finally Program is Executed")
