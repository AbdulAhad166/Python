#Program For Demonstrating Functionality of Iterators --- Set() and FrozenSet()
n={10,"BB",34.64,True,3+2j}  #OR frozenset ({10,"RS",34.65,True,3+2j})
print("Content of n={} Type={}".format(n,type(n)))
print("-----------------------------------------------")
#Convert Iterable Object to Iterator Object
itrobj=iter(n)
print("Content of n={} Type={}".format(n,type(n)))
for val in itrobj:
    print("\t {}".format(val))