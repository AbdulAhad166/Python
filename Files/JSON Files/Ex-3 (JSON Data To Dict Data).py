#Program for Converting JSON String Data into Dict Data---json.loads()
import json
jsonformat='{"ENO":"100","NAME":"Rossum","SAL":"12.55"}'
print("JSON Content={} Type={}".format(jsonformat,type(jsonformat)))
#Convert JSON Data into Dict Data
dictobj=json.loads(jsonformat)
print("Dict Object Content={} Type={}".format(dictobj,type(dictobj)))
for a,b in dictobj.items():
    print("\t {}--->{}".format(a,b))
