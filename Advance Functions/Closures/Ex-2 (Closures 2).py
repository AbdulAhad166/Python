#Program for Demonstrating the concept of closure
def grandparent(gpassets=100):
    print("Grand Parent Property= {}".format(gpassets))
    def grandchild(gcp):
        totprop=gpassets+gcp  #In Default PVM Takes 1
        print("grandchild()---Grand Parent Property:{} Child Property:{} totproperty:{}".format(gpassets,gcp,totprop))
    return grandchild
#Main Program
grcd=grandparent()  #Function Call
for gcp in range(1000,1011):         
    grcd(gcp)