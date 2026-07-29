#Program for Demonstrating Generator Concept
def BBrange(start,stop):
    while start<=stop:
        yield start
        start=start+1
#Main Program
r=BBrange(10,16)# Here r is an object of <class, generator>
#To get the values from generator object, we use next(generator-object)
print(next(r))
print(next(r))
for val in r:
    print("\t {}".format(val))
