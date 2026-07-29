#Program for Demonstrating Generators Concept
#GenEx5.py
def  RSrange(Start,Stop=1,Step=1):
	if Stop<=Start:
		Stop=Start
		Start=1
	while Start<=Stop:
		yield Start
		Start=Start+Step
#Main Program
r1=RSrange(6) # Here r1' is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r1))
print(next(r1))
for val in r1:
	print("\t{}".format(val))
print("---------------------------------------------------------------")
r2=RSrange(10,16) # Here r2' is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r2))
print(next(r2))
for val in r2:
	print("\t{}".format(val))
print("---------------------------------------------------------------")
r3=RSrange(10,21,2) # Here r' is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r3))
print(next(r3))
for val in r3:
	print("\t{}".format(val))
print("---------------------------------------------------------------")