#Program for Reading JSON File Object into Dict Object
import json
with open("emp.json","r") as fp:
    dictobj=json.load(fp)
    for a,b in dictobj.items():
        print("{}--->{}".format(a,b))
