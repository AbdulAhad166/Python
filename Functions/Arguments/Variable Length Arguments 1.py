#Program for Demonstrating Variable Length Arguments
#In This Program, we have Different Function Calls with Different Names and we have corresponding Different Function Def. so that Program will execute  Successfully. But Every Function Name is an Object and It takes Separate Memory Space.
#Here we have 5 Different Function Names and They take 5 Different Memory spaces. This is One of the Limitation
def  disp1(a,b,c,d,e):  # Function Def-1
	print(a,b,c,d,e)
def  disp2(a,b,c,d):  # Function Def-2
	print(a,b,c,d)
def  disp3(a,b,c):  # Function Def-3
	print(a,b,c)
def  disp4(a,b):  # Function Def-4
	print(a,b)
def  disp5(a):  # Function Def-5
	print(a)
#Main Program
disp1(10,20,30,40,50)  # Function Call-1 with 5 Pos Args
disp2(10,20,30,40)  # Function Call-2 with 4 Pos Args
disp3(10,20,30)  # Function Call-3 with 3 Pos Args
disp4(10,20)  # Function Call-4 with 2 Pos Args
disp5(10)  # Function Call-5 with 1 Pos Arg