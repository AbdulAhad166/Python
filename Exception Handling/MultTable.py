#MultTable.py<----Module Name
from MultExcept import NegativeNumberError,ZeroError
def Table(n):
    if n<0:
        raise NegativeNumberError
    elif n==0:
        raise ZeroError
    else:
        print("-"*50)
        print("\t Multiplication Table for {}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("\t {} x {} = {}".format(n,i,i*n))
        print("-"*50)
