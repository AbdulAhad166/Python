#Program for getting all +ve values and -ve values separately
#NOT TUPLE COMPREHENSION
lst=[10,-20,30,-40,50,-60,70,-80,90]
pslist=(val for val in lst if val>0) #It is not Tuple comprehension
nglist=(val for val in lst if val<0)
#Here pslist is an object of <class, generator>
#Convert generator object into list /set/tuple
t=list(pslist)
r=set(nglist)
print("List of +VE Values= ",t)
print("List of -VE Values= ",r)