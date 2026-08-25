#Program For Showing The Execution Time of Multiple Sub Threads Along With Main Thread
import threading,time
class SqNumbers:
    def __init__(self,lst):
        self.lst=lst
    def Squares(self):
        for val in lst:
            print("\t{}--->Squares({})--->{}".format(threading.current_thread().name,val,val**2))
            time.sleep(1)
class CbNumbers:
    def __init__(self,lst):
        self.lst=lst
    def Cubes(self):
        for val in lst:
            print("\t {}--->Cubes({})--->{}".format(threading.current_thread().name,val,val**3))
            time.sleep(1)
#Main Program
bt=time.time()
print("Program Execution Started: ",threading.current_thread().name)
lst=[1,3,4,5,9,16,55,57]
t1=threading.Thread(target=SqNumbers(lst).Squares)
t2=threading.Thread(target=CbNumbers(lst).Cubes)
t1.start()
t2.start()
t1.join()
t2.join()
et=time.time()
print("Total Execution Time of Sub Threads:",et-bt)