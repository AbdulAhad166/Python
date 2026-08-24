#Program For Showing The Execution Time of Default Thread Flow ---Main Thread
import threading,time
def Squares(lst):
    for val in lst:
        print("\t {}---->Squares({})={}".format(threading.current_thread().name,val,val**2))
def Cubes(lst):
    for val in lst:
        print("\t {}---->Cubes({})={}".format(threading.current_thread().name,val,val**3))
#Main Program
bt=time.time()   #For Calculating Beginning Time
print("Program Execution Started: ",threading.current_thread().name)
lst=[2,3,6,5,8,9,10,11,16,18,19,90,555]
Squares(lst)    #Function Call
print("------------------------------------------------")
Cubes(lst)      #Function Call
print("------------------------------------------------")
print("Program Execution Ended: ",threading.current_thread().name)
et=time.time()  #For Calculating Ending Time
print("Total Execution Time of Default Thread= ",et-bt)
