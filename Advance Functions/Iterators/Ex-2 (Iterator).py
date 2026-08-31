#Program For Demonstrating Functionality of Iterators --- tuple()
n=(10,"BB",80.00,True,3+2j)
print("Content of n={} Type={}".format(n,type(n)))
print("-------------------------------------------------")
#Convert Iterable Object into Iterator Object
itrobj=iter(n)
print("Content of n={} Type={}".format(n,type(n)))
for val in itrobj:
    print("\t {}".format(val))