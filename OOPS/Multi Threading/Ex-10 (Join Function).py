#Program For Showing The Execution Status of Sub Thread Before and After start() and After Completion With join()
import threading,time
def Welcome(name):
    print("\t {}--->Welcome To Multi-Threading".format(threading.current_thread().name,name))
    print("\t {}--->Going To Sleep For 6 Seconds".format(threading.current_thread().name))
    time.sleep(6)
    print("\t Coming Out of Sleep After 6 Seconds".format(threading.current_thread().name))
#Main Program
print("Program Execution Started: ",threading.current_thread().name)
print("Total Number of Threads= ",threading.active_count())
t1=threading.Thread(target=Welcome,args=("BB",))
print("Execution Status of t1 Before start()= ",t1.is_alive())
t1.start()
print("Total Number of Threads= ",threading.active_count())
print("Execution Status of t1 After start()= ",t1.is_alive())
#Make The Sub Threads To Join Main Thread
t1.join()
print("Total Number of Threads= ",threading.active_count())
print("Execution Status of t1 After Complete Execution= ",t1.is_alive())
print("Program Execution Ended: ",threading.current_thread().name)