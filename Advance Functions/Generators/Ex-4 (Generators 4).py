#Program for Demonstrating Generators Concept
def  RSrange(Start,Stop,Step):
	while(Start<=Stop):
		yield Start
		Start=Start+Step

#Main Program
r=RSrange(10,21,2) # Here r' is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r))
print(next(r))
for val in r:
	print("\t{}".format(val))