#Program for Demonstrating Exception Occurrence
try:
    a=input("Enter First Number: ")
    b=input("Enter Second Number: ")
    x=int(a)    #Exception Generated Statement---ValueError
    y=int(b)
    z=x/y
    s="PYTHON"   #New Statements
    print(s[8])
except ZeroDivisionError:
    print("\t Do Not Enter Denominator as Zero")
except ValueError:
    print("\t Do Not Enter Alnums,str,symbols")
except:      #Default Except Block
    print("Oops Something Went Wrong")
else:
    print("First Number= {}".format(x))
    print("Second Number= {}".format(y))
    print("Division= {}".format(z))
finally:
    print("\t Finally Program Executed Successfully")

