#Program for Saving Dict Object data to JSON File---json.dump()
import json
dictobj={'ENO':'100','NAME':'Rossum','SAL':'12.55'}
with open("emp.json","w") as fp:
    json.dump(dictobj,fp)
    print("Dict Data Saved in JSON File---Verify")