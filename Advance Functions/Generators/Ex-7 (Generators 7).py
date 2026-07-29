#Program for Demonstrating Generators Concept
import random as r   #here why we took import because randint() is used inside the function
def getotp():
	for i in range(20):
		yield "Ur OTP:"+str(r.randint(1000,10000))
#Main Program
cr=getotp() # Here cr is an object of <class, generator>
print(next(cr))