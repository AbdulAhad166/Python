#Program For Showing The Execution Time of Multiple Sub Threads Along With Main Thread
import threading,time
class Numbers:
    def Squares(self,lst):
        for val in lst:
            print("\t{}--->Squares=({})--->{}".format(threading.current_thread().name,val,val**2))
            time.sleep(1)
    def Cubes(self,lst):
        for val in lst:
            print("\t{}--->Cubes({})--->{}".format(threading.current_thread().name,val,val**3))
            time.sleep(1)
#Main Program
bt=time.time()
print("Program Execution Started: ",threading.current_thread().name)
lst=[1,3,4,5,8,9,16,55,57]
#Create A Sub Thread
t1=threading.Thread(target=Numbers().Squares,args=(lst,))
t2=threading.Thread(target=Numbers().Cubes,args=(lst,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Program Execution Ended: ",threading.current_thread().name)
et=time.time()
print("Total Execution Time of Sub Threads= ",et-bt)