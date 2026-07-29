#Program for Demonstrating Exception Occurrence
try:
    a=input("Enter First Number: ")
    b=input("Enter Second Number: ")
    x=int(a)   #Exception Generated Statement---ValueError
    y=int(b)   #Exception Generated Statement---ValueError
    z=x/y      #Exception Generated Statement---ZeroDivisionError
except ZeroDivisionError as z:   #Here z is Alias Name for ZeroDivisionError
    print("\t Do Not Enter Denominator as Zero",z)
except ValueError as v:          #Here v is Alias Name for ValueError
    print("\t Do Not Enter alnums,str,symbols",v)
else:             #else Block Executes the statements when there is no Exception in try block
    print("First Value= {}".format(x))
    print("Second Value= {}".format(y))
    print("Division= {}".format(z))
finally:       #Finally block will execute for all time
    print("Finally Program Executed Successfully")