#Program for Demonstrating Generators Concept
def  RSrange(Val):
	i=1
	while i<=Val:
		yield i
		i=i+1

#Main Program
r=RSrange(6) # Here r' is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
#print(next(r))-----Gives  StopIteration