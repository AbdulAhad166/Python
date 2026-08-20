#SameClassAccount2.py
class Account:
    def __init__(self):
        self.acno=int(input("Enter Account Number: "))
        self.cname=input("Enter Account Holder Name: ")
        self.__bal=float(input("Enter Account Balance: "))
        self.__pin=int(input("Enter Account Pin: "))
        self.bname=input("Enter Account Branch Name: ")
    def __getaccdet(self):    #Here Instance Method is Encapsulated
        print("-"*50)
        print("Account Number: ",self.acno)
        print("Account Holder Name: ",self.cname)
        print("Account Balance: ",self.__bal)
        print("Account Pin: ",self.__pin)
        print("Account Branch Name: ",self.bname)
        print("-"*50)
    def showaccdet(self):   #Here This Function does not Contain Encapsulation so this can be
        self.__getaccdet()       #used for calling the Encapsulated Function

#Main Program
ac=Account()
#ac.getaccdet()  #Here This Will Give Attribute Error Because getaccdet() Made as Encapsulated
ac.showaccdet()