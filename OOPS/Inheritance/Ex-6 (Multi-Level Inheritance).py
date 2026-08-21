#Program For Using Inheritance --- Multi-Level Inheritance
class GrandParent:
    def grandparentproperty(self):
        self.gpp=float(input("Enter GrandParent Property: "))
class Parent(GrandParent):
    def parentproperty(self):
        self.pp=float(input("Enter Parent Property: "))
class Child(Parent):
    def childproperty(self):
        self.cp=float(input("Enter Child Property: "))
    def totprop(self):
        print("GrandParent Property: ",self.gpp)
        print("Parent Property: ",self.pp)
        print("Child Property: ",self.cp)
        self.tp=self.gpp+self.pp+self.cp
        print("Total Property: ",self.tp)
#Main Program
co=Child()
co.grandparentproperty()
co.parentproperty()
co.childproperty()
co.totprop()
