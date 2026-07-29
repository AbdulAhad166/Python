#Program for Demonstrating Exception Occurrence
try:
    a=input("Enter First Number: ")
    b=input("Enter Second Number: ")
    x=int(a)
    y=int(b)
    z=x/y
    s="PYTHON"
    print(s[5])
except BaseException as B:   #Here BaseException is also generic except block and it is defined as Alias Name
    print("\t Oops Something Went Wrong")
else:
    print("\t First Number= {}".format(x))
    print("\t Second Number: {}".format(y))
    print("Division= {}".format(z))
finally:
    print("\t Finally Program Executed")