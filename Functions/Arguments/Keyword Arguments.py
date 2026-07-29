#Program for Demonstrating Key word args
#KeywordArgsEx1.py
def disp(a,b,c,d):
	print("\t{}\t{}\t{}\t{}".format(a,b,c,d))
#Main Program
print("-"*50)
print("\tA\tB\tC\tD")
print("-"*50)
disp(10,20,30,40) # Function call with 4 Positional Args
disp(10,20,d=40,c=30) # Function call with 2 Pos Args +2 kwd args
disp(d=40,c=30,a=10,b=20) # Function call with 4 kwd args
#disp(c=30,d=40,10,20)----SyntaxError: positional argument follows keyword argument
disp(c=30,d=40,a=10,b=20)
disp(10,c=30,d=40,b=20)
print("-"*50)