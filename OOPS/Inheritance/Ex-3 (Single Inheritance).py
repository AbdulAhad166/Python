#Program for Using Inheritance --- Single Inheritance
class Parent:
    def getparentproperty(self):
        self.pp=float(input("Enter Parent Property: "))
class child(Parent):
    def getchildproperty(self):
        self.cp=float(input("Enter Child Property: "))
    def totprop(self):
        self.tp=self.pp+self.cp
        print("Parent Property: ",self.pp)
        print("Child Property: ",self.cp)
        print("Total Property: ",self.tp)
#Main Program
co=child()
co.getparentproperty()
co.getchildproperty()
co.totprop()