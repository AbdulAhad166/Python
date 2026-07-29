#Program for Demonstrating Variable Length Arguments
#PureVariableLengthArgsEx4.py
def    disp(sno,sname,marks,*BB, city="HYD"): # here *BB is Called Variable Length Parameter and whose type is <class,tuple>
		print("---------------------------------------")
		print("\tStudent Number={}".format(sno))
		print("\tStudent Name={}".format(sname))
		print("\tStudent Marks={}".format(marks))
		print("\tStudent City={}".format(city))
		print("Variable Length Args")
		s=0
		for val in BB:
			print("\t{}".format(val))
			s=s+val
		print()
		print("\tSum=",s)
		print("---------------------------------------")
#Main Program--Family of Multiple Similar Function Calls with Variable Length args
disp(100,"RS",34.56,10,20,30,40,50)  # Function Call-1
disp(200,"DR",33.33,10,20,30,40)  # Function Call-2
disp(300,"TR",55.55,10,20,30)  # Function Call-3
disp(400,"SR",22.22,10,20)  # Function Call-4
disp(500,"KV",44.23,10)  # Function Call-5
disp(600,"JH",44.78)  # Function Call-6
disp(700,"DT",11.11,city="USA") # Function Call-7
#disp(800,"PT",21.11,city="RSA",1.2,2.3,3.4) # SyntaxError: positional argument follows
# keyword argument
disp(800,"PT",21.11,1.2,2.3,3.4,city="RSA")