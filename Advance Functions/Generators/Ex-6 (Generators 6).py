#Program for Demonstrating Generators Concept
def getcourse():
	yield "C"
	yield "Java"
	yield "PYTHON"
	yield "DSA"

#Main Program
cr=getcourse() # Here cr is an object of <class, generator>
print(next(cr))
print(next(cr))
print(next(cr))
print(next(cr))
#print(next(cr))-----Gives StopIteration