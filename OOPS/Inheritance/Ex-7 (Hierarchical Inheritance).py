#Program For Using Inheritance ---- Hierarchical Inheritance
class c1:
    def disp1(self):
        print("Display C1")
class c2(c1):
    def disp2(self):
        print("Display C2")
class c3(c1):
    def disp3(self):
        print("Display C3")
#Main Program
print("With Respect To Class C2")
o2=c2()
o2.disp1()
o2.disp2()
#o2.disp3()  #There is No Reference of c3 class so It Gives Attribute Error
print("With Respect To Class C3")
o3=c3()
o3.disp1()
o3.disp3()
#o3.disp2()  #There is No Reference of c2 Class so It Gives Attribute Error