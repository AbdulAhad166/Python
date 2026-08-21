#Program for Using Inheritance --- Single Inheritance
class c1:
    def disp1(self):
        print("Display C1")
class c2(c1):
    def disp2(self):
        print("Display C2")
#Main Program
o2=c2()  #Creating Object
o2.disp1()  #Displaying Object
o2.disp2()