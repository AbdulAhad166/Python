#Program for accepting List of +ve and -ve values using filter()
pos=lambda x:x>0
ng=lambda x:x<0
#Main Program
print("Enter List of values separated by space:\n ")
lst=[float(val) for val in input().split(" ")]
print("Given Values= ",lst)
ps=list(filter(pos,lst))
ng=list(filter(ng,lst))
print("List of +VE Values= ",ps)
print("List of -VE Values= ",ng)
