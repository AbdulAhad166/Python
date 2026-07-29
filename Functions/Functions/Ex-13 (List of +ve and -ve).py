#Program for getting all +ve and -ve form a list
#List Comprehension
lst=[10,20,50,-43,-54,-45,32]
pslist=[val for val in lst if val>0]
nglist=[val for val in lst if val<0]
print("List of +VE Values= ",pslist)
print("List of -VE Values= ",nglist)