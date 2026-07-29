#Want to generate Calendar of a Month for a Year
#Want to generate list of values sum
#Want to generate list of values separated by +VE Values Only
#import builtins----Default Imported Module
import calendar
import functools # Here calendar,functools are Called Pre-Defined Modules
print(calendar.month(2026,6))
print("--------------------------------------")
lst=[10,20,30,40,50,60,70]
s=functools.reduce(lambda x,y:x+y,lst)
print("Sum({})={}".format(lst,s))
print("--------------------------------------")
lst=[10,-20,30,-40,50,-60]
lst1=list(filter(lambda x: x>0,lst))
print("+VE Vals=",lst1)
print("--------------------------------------")