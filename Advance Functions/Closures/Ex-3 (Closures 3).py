#Program for Demonstrating the concept of Closure
def grandparent(gpassets=100):
    print("Grand Parent Property= {}".format(gpassets))
    def grandchild(gcp):
        totprop=gpassets+gcp
        print("grandchild()---Grand Parent Property: {} Grand Child Property: {}  totprop:{}".format(gpassets,gcp,totprop))
    for gcp in range(1000,1011):
        grandchild(gcp)
#Main Program
grandparent()