#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#PureKeywordVariableLengthArgsEx1.py
def  disp(**BB):#Here **BB is Called Keyword Variable Length Param and whose type <class, dict>
	print(BB,type(BB))
#Main Program
disp(sno=10,sname="RS",mm=56,em=70,cname="PSF") # Function Call-1 with 5 Keyword Arguments
disp(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")# Function Call-2 with 4 Keyword Arguments
disp(cid=1000,cname="JH",hb="Drawing") # Function Call-3 with 3 Keyword Arguments