#Program FOr Demonstrating Functionality of Iterators --- str()
n="PYTHON"
print("Content of n={} Type={}".format(n,type(n)))
print("-------------------------------------------------")
#Create Iterable Object FOr Iterator Object
itrobj=iter(n)
for val in itrobj:
    print("\t {}".format(val))