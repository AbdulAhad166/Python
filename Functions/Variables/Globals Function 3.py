#Program for Demonstrating globals()
#In This Program we have Sames Names for Local and Global Variables
a=10
b=20  # Here a,b are Called global variables
def  operations():
	x=globals() # Here x is Called Dict Object contains Global Var Names as Key,  Global Var Values as Value
	print("-------------------------------------------------------------")
	print("List of Visible and Invisible Global Variables")
	print("-------------------------------------------------------------")
	for gvn,gvv in x.items():
		print("{}-->{}".format(gvn,gvv))
	print("-------------------------------------------------------------")
	print("List of Programmer-Defined Global Variables-Way-1")
	print("-------------------------------------------------------------")
	print("Global Var a=",x['a'])
	print("Global Var b=",x['b'])
	print("-------------------------------------------------------------")
	print("List of Programmer-Defined Global Variables-Way-2")
	print("-------------------------------------------------------------")
	print("Global Var a=",x.get('a'))
	print("Global Var b=",x.get('b'))
	print("-------------------------------------------------------------")
	print("List of Programmer-Defined Global Variables-Way-3")
	print("-------------------------------------------------------------")
	print("Global Var a=",globals().get('a'))
	print("Global Var b=",globals().get('b'))
	print("-------------------------------------------------------------")
	print("List of Programmer-Defined Global Variables-Way-4")
	print("-------------------------------------------------------------")
	print("Global Var a=",globals()['a'])
	print("Global Var b=",globals()['b'])
	print("-------------------------------------------------------------")
#Main Program
operations()