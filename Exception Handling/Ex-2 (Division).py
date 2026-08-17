#Program for Demonstrating the Concept of Exception
#This is the Program for Exception so we have converted the Error Message into User Friendly Error Message
"""try:
    a=input("Enter First Value: ")
    b=input("Enter Second Value: ")
    c=a/b
    print("\t First Value= {}".format(a))
    print("\t Second Value= {}".format(b))
    print("\t Division= {}".format(c))
except TypeError:
    print("\t Do Not Enter Direct Values Convert into 'int' Data Type")"""
#Now Using try and except function with correct approach
try:
    a=input("Enter First Value: ")
    b=input("Enter Second Value: ")
    c=a/b
    print("\t First Value= {}".format(a))
    print("\t Second Value= {}".format(b))
    print("\t Division= {}".format(c))
except TypeError:
    print("\t Do Not Enter Direct Values Convert into 'int' Data Type")