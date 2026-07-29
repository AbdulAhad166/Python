#Program for accepting List of +VE and -VE Numbers using filter()
print("Enter List of Values Separated By Comma:\n ")
lst=[float(val) for val in input().split(",")]
print("Given Values= ",lst)
ps=list(filter(lambda x:x>0,lst))
ng=list(filter(lambda x:x<0,lst))
print("List of +ve Values= ",ps)
print("List of -ve Values= ",ng)