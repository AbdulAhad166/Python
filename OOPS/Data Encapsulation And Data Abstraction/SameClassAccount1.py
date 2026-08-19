#SameClassAccount1.py
class Account:
    def __init__(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal=4.5
        self.__pin=6789
        self.bname="SBI"
    def getaccdet(self):
        print("Account Number:",self.__acno)
        print("Account Holder Name:", self.cname)
        print("Account Balance:",self.__bal)
        print("Account PIN:",self.__pin)
        print("Account Branch Name:", ac.bname)
#Main Program
ac=Account()
ac.getaccdet()