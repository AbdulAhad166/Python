#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#KeywordVariableLengthArgsEx3.py
#In This we have Family Similar Function Calls and we have corresponding Multiple  Functions
# Def with same Function Name. This Program will execute because we are Defining the Function,
# and Immediately we are Calling Definition Only But not all.
def disp(sno,sname,mm,em,cname): # Function Def-1
		print(sno,sname,mm,em,cname)
disp(sno=10,sname="RS",mm=56,em=70,cname="PSF") # Function Call-1 with 5 Keyword Arguments
#---------------------------------------------------------------------------------------
def disp(tno,tname,sub1,sub2):  # Function Def-2
	print(tno,tname,sub1,sub2)
disp(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")# Function Call-2 with 4 Keyword Arguments
#---------------------------------------------------------------------------------------
def disp(cid,cname,hb):  # Function Def-3
	print(cid,cname,hb)
disp(cid=1000,cname="JH",hb="Drawing") # Function Call-3 with 3 Keyword Arguments
#---------------------------------------------------------------------------------------
#Limitation:
#If we have 1000 Similar Function Calls with Keyword Variable Length args then we must define
# 1000 Function Definitions
#Which is one of the Time Consuming Process.
#To Over this Process, we define ONE Function Definition, Irrespective of  N-Similar Function
# Calls with Keyword Variable Length args by using the concept of  KEY WORD VARIABLE
# LENGTH ARGUMENTS.