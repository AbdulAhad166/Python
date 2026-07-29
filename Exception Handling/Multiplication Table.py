#Program for Generating Multiplication Table For Any Number and using raise keyword
class NegativeNumberError(Exception):pass
class ZeroError(BaseException):pass
def Multi(n):
    if n<0:
        raise NegativeNumberError
    elif n==0:
        raise ZeroError
    else:
        print("-"*50)
        print("Multiplication Table of {}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("\t {} x {} = {}".format(n,i,n*i))
        print("-"*50)
while True:
    try:
        Multi(int(input("Enter Any Number: ")))
    except NegativeNumberError:
        print("\t Do Not Enter Negative Numbers in Multiplication Table---Try Again")
    except ZeroError:
        print("\t Do Not Enter Zero in Multiplication Table---Try Again")
    except ValueError:
        print("\t Do Not Enter Negative Numbers in Multiplication Table---Try Again")
