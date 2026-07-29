#Program for Demonstrating globals()
#In This Program we have Different Names for Local and Global Variables
a=10
b=20
c=30
d=40  #Here a,b,c,d are Global Variables
def operation():
    x=100
    y=200
    z=300
    r=400
    res=x+y+z+r+a+b+c+d  #Here x,y,z,r are Local Variables
    print("\tResult= ",res)
#Main Program
operation()