#Program for Using Inheritance --- Multi-Level Inheritance
class c1:
    def disp1(self):
        print("Display C1")
class c2(c1):
    def disp2(self):
        print("Display C2")
class c3(c2):
    def disp3(self):
        print("Display C3")
#Main Program
o3=c3()        #Creating Object
o3.disp1()     #Displaying Object
o3.disp2()
o3.disp3()
