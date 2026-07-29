#Program for Demonstrating Exception and using raise keyword
class NumberDivisionError(Exception):pass
def division(a,b):
    if b==0:
        raise NumberDivisionError
    else:
        return a/b
while True:
    try:
        a=int(input("Enter First Number: "))
        b=int(input("Enter Second Number: "))
        res=division(a,b)  #Function Call
    except NumberDivisionError:
        print("\t Do NOt Enter Zero in Denominator---Try Again")
    except ValueError:
        print("\t Do Not Enter Alnums,str,Symbols---Try Again")
    else:
        print("\t Division ({},{}) = {}".format(a,b,res))
        break
    finally:
        print("\t Program Executed")