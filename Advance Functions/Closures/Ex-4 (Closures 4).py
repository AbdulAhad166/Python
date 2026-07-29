#Program for Demonstrating the Concept of Closure
gpassets1=10
def grandparent():#Outer Function
	gpassets2=100  # Local Variable for Outer Function and Global for Inner function--Non-Local Variables
	print("Grand Parent Property={}".format(gpassets2))
	def grandchild(gcp):  # inner function---Closure
		nonlocal gpassets2
		global gpassets1
		totprop=gpassets1+gpassets2+gcp
		print("grandchild()--Grand Grand Prop:{} :Grand PP:{}  Child Prop:{}   totprop:{}".format(gpassets1,gpassets2,gcp,totprop))
		gpassets1=gpassets1+1
		gpassets2=gpassets2+1
	for gcp in range(1000,1011):
		grandchild(gcp)
#Main Program
grandparent()
