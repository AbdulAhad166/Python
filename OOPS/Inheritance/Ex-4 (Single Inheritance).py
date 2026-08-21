#Program For Using Inheritance --- Single Inheritance
class parent:
    def getparentproperty(self):
        self.pp=float(input("Enter Parent Property: "))
class child(parent):
    def getchildproperty(self):
        self.cp=float(input("Enter Child Property: "))
    def totprop(self):
        self.getparentproperty()   #Calling Instance Methods
        self.getchildproperty()
        self.tp=self.pp+self.cp
        print("Total Property: ",self.tp)
#Main Program
co=child()     #Creating Object
co.totprop()