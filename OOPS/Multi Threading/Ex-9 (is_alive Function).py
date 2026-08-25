#Program For Showing The Execution Status of sub Threads
import threading
def Welcome(name):
    print("\t {}--->Welcome To Multi-Threading",threading.current_thread().name,name)
#Main Program
#Create A Sub Thread
print("Program Execution Started: ",threading.current_thread().name)
t1=threading.Thread(target=Welcome,args=("BB",))
print("Execution Status Before Start(): ",t1.is_alive())
t1.start()
print("Execution Status After Start(): ",t1.is_alive())
print("Program Execution Ended: ",threading.current_thread().name)