#Program for Demonstrating Positional Arguments
#This Program is to determine that this will execute multiple times same like crs that is
# equal to all the inputs and takes more time to execute
def  dispstudinfo(sno,sname,marks,crs):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))
#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstudinfo(10,"RS",45.67,"PYTHON") # Function Call with 4 Pos Args
dispstudinfo(20,"TR",35.17,"PYTHON") # Function Call with 4 Pos Args
dispstudinfo(30,"DR",25.33,"PYTHON") # Function Call with 4 Pos Args
dispstudinfo(40,"JH",15.33,"PYTHON") # Function Call with 4 Pos Args
dispstudinfo(sname="KV",sno=50,crs="PYTHON",marks=45.89) # Function Call with 4 Keyword Args
print("-"*50)