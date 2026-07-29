#Program for demonstrating Default Arguments
def dispstudinfo(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t{}\t{}".format(sno,sname,marks,crs))
#Main Program
print("-"*50)
print("\tSNO\tSNAME\tMARKS\tCRS")
print("-"*50)
dispstudinfo(10,"RS",50.64)  #Function call with 3 positional Arguments
dispstudinfo(20,"TR",60.56)  #Function call with 3 positional Arguments
dispstudinfo(30,"SR",50.64)  #Function call with 3 positional Arguments
dispstudinfo(40,"RT",60.56)  #Function call with 3 positional Arguments
dispstudinfo(sno=50,sname="YT",marks=45.66,crs="Java") #Function call with 4 keyword Arguments
#Here crs is taken different and will be executed with that different value only it does not
#change or assign to the upper value