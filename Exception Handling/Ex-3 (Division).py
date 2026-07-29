#Program for Demonstrating Exception Occurrence
try:
    a=input("Enter First Number: ")
    b=input("Enter Second Number: ")
    x=int(a)  #Exception Generated Statements ----- ValueError
    y=int(b)  #Exception Generated Statements ----- ValueError
    z=x/y     #Exception Generated Statements ----- ValueError
except ZeroDivisionError:
    print("Do Not Enter Denominator as Zero")
except ValueError:
    print("Do Not Enter Alnums,str,symbols")
else:      #Here else Block is used for printing the results of the program for better
           # clarity of the program we use else block for printing the values
    print("\t First Value= {}".format(x))
    print("\t Second Value= {}".format(y))
    print("\t Division = {}".format(z))

