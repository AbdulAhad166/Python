#DivOperationDemo.py<------Main Program
from DivExcept import NumberDivisionError
from DivOperation import division
while(True):
    try:
        a=int(input("Enter First Number: "))
        b=int(input("Enter Second Number: "))
        res=division(a,b)  #Function Call
    except NumberDivisionError:
        print("\t Do Not Enter Zero For Denominator----Try Again")
    except ValueError:
        print("\t Do Not Enter Alnums,str,Symbols----Try Again")
    else:
        print("Division ({},{}) = {}".format(a,b,res))
        break
    finally:
        print("Program Executed")
