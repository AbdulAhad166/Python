#Program for Demonstrating Generators Concept
def  BBrange(Val):
	i=1
	while(i<=Val):
		yield i
		i=i+1

#Main Program
r=BBrange(6) # Here r' is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r))
print(next(r))
for val in r:
	print("\t{}".format(val))