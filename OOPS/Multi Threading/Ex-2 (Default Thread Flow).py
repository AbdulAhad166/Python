#Program For Showing The Default Thread Flow --- Main Thread
import threading
def Squares(lst):
    for val in lst:
        print("\t {}--->Squares({})={}".format(threading.current_thread().name,val,val**2))
def Cubes(lst):
    for val in lst:
        print("\t {}--->Cubes({})={}".format(threading.current_thread().name,val,val**3))
#Main Program
print("Program Execution Started: ",threading.current_thread().name)
lst=[10,3,9,6,4,2,11,16,20]
Squares(lst)     #Function Call
print("-----------------------------------------")
Cubes(lst)       #Function Call
print("-----------------------------------------")
print("Program Execution Ended: ",threading.current_thread().name)