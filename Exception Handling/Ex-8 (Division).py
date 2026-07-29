#Program for Demonstrating Exception Occurrence
try:
    a=input("Enter First Number: ")
    b=input("Enter Second Number: ")
    x=int(a)
    y=int(b)
    z=x/y
    s="PYTHON"     #New Statement Added
    print(s[3])
except Exception:    #generic except block where it meant that parent class has it's child classes and
           # all the exceptions are included in the parent class and when exception occurs then it
           # will give you the exception message
    print("\t Oops Something Went Wrong")
else:
    print("\t First Number= {}".format(x))
    print("\t Second Number= {}".format(y))
    print("\t Division= {}".format(z))
finally:
    print("\t Finally Program Executed")