#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#KeywordVariableLengthArgs.py
#In This we have Different Function Calls with Different Names and we have corresponding
# Different Function Def. so that Program will execute  Successfully. But Every Function Name is an Object and It takes Separate Memory Space.
#Here we have 3 Different Function Names and They take 3 Different Memory spaces.
# This is One of the Limitation
def disp1(sno,sname,mm,em,cname): # Function Def-1
	print(sno,sname,mm,em,cname)

def disp2(tno,tname,sub1,sub2):  # Function Def-2
	print(tno,tname,sub1,sub2)

def disp3(cid,cname,hb):  # Function Def-3
	print(cid,cname,hb)

#Main Program
disp1(sno=10,sname="RS",mm=56,em=70,cname="PSF") # Function Call-1 with 5 Keyword Arguments
disp2(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")# Function Call-2 with 4 Keyword Arguments
disp3(cid=1000,cname="JH",hb="Drawing") # Function Call-3 with 3 Keyword Arguments