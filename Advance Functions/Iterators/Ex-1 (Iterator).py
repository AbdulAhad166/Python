#Program For Demonstrating Functionality of Iterators --- list()
n=[10,"RS",34.54,True,2+3j]
print("Content of n={} Type={}".format(n,type(n)))
print("---------------------------------------------------")
#Convert Iterable Object into Iterator Object
itrobj=iter(n)
print("Content of n={} Type={}".format(itrobj,type(itrobj)))
print(next(itrobj))
print(next(itrobj))
