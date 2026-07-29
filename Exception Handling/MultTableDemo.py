#MultTableDemo.py<----Main Program
from MultExcept import NegativeNumberError,ZeroError
from MultTable import Table
while True:
    try:
        Table(int(input("Enter Any Number: ")))
    except ZeroError:
        print("\t Do Not Enter Zero for Multiplication Table---Try Again")
    except NegativeNumberError:
        print("\t Do Not Enter Negative Number for Multiplication Table---Try Again")
    except ValueError:
        print("\t Do Not Enter Alnums,Str,Symbols---Try Again")
    else:
        print("Program Executed")