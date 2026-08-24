#Program For Showing The Execution Time of Sub Threads Along With  Main Thread
import threading,time
def Squares(lst):
    for val in lst:
        print("\t {}--->Squares({})={}".format(threading.current_thread().name,val,val**2))
def Cubes(lst):
    for val in lst:
        print("\t {}--->Cubes({})={}".format(threading.current_thread().name,val,val**3))
#Main Program
bt=time.time()
print("Program Execution Started: ",threading.current_thread().name)
lst=[10,6,55,16,18,2,9,1]
#Create a Sub Thread For Executing Squares()
t1=threading.Thread(target=Squares,args=(lst,)) #Here t1 is Sub Thread Object Whose Default Name is thread-1
#Create a Sub Thread For Executing Cubes()
t2=threading.Thread(target=Cubes,args=(lst,)) #Here t2 is Sub Thread Object Whose Default Name is thread-2
#Dispatch the Sub Threads
t1.start()
t2.start()
#Join the Sub Threads
t1.join()
t2.join()
print("Program Execution Ended: ",threading.current_thread().name)
et=time.time()
print("Total Execution Time of Sub Threads= ",et-bt)