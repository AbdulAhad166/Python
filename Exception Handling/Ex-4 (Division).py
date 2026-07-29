#Program for Demonstrating Exception Occurrence
try:
    a=input("Enter First Number: ")
    b=input("Enter Second Number: ")
    x=int(a)
    y=int(b)
    z=x/y
except ZeroDivisionError:
    print("\t Do Not Enter Denominator as Zero")
except ValueError:
    print("\t Do Not Enter Alnums,str,symbols")
else:
    print("\t First Value= {}".format(x))
    print("\t Second Value= {}".format(y))
    print("\t Division= {}".format(z))
finally:   #Here finally Block is kept because it gives the result whether there is exception in
           # try block or not it gives the result that is present in the finally block
    print("\t Finally Program is Executed")