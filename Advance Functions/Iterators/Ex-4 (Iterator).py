#Program For Demonstrating Functionality of Iterators --- dict()
n={1:"PYTHON",2:"JAVA",3:"C",4:"C++"}
print("Content of n={} Type={}".format(n,type(n)))
print("------------------------------------------------")
#Create Iterable Object to Iterator Object
itrobj=iter(n)
print("Content of n={} Type={}".format(n,type(n)))
for key in itrobj:
    print("\t{}--->{}".format(key,n[key]))