#Program for Demonstrating Exception Occurrence
try:
    a=input("Enter First Number: ")
    b=input("Enter Second Number: ")
    x=int(a)   #Exception Generated Statements---ValueError
    y=int(b)   #Exception Generated Statements---ValueError
    z=x/y      #Exception Generated Statements---ZeroDivisionError
    s="PYTHON"   #New Statements
    print(s[1])
except Exception as RS:    #Here RS is Alias Name for Exception and this is generic Except Block
    print("\t Oops Something Went Wrong")
else:
    print("First Number= {}".format(x))
    print("Second Number= {}".format(y))
    print("Division= {}".format(z))
finally:
    print("\t Finally Program Executed")