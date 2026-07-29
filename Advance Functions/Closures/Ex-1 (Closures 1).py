#Program for Demonstrating the concept of closures
def grandparent(gpassets=100):         #Outer Function
    print("Grand Parents Property= {}".format(gpassets))
    def grandchild():          #Inner Function ------Closure
        print("\t grandchild()--Grand Parent Property: ",gpassets)
    return grandchild
#Main Program
grcd=grandparent()
grcd()   #This is a Function Call and this is a closure that will show only one on demand
grcd()