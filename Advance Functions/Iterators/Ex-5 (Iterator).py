#Program FOr Demonstrating Functionality of Iterators --- range()
n=range(10,21,1)
print("Content of n={} Type={}".format(n,type(n)))
print("-----------------------------------------------")
#Create Iterable Object for Iterator Object
itrobj=iter(n)
print("Content of n={} Type={}".format(itrobj,type(itrobj)))
for val in itrobj:
    print("\t {}".format(val))