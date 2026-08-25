#Program For Running The Sub Threads Using OOPS
import threading
class Got:
    def Welcome(self,name):
        print("{}--->{}--->Welcome to Multi-Threading".format(threading.current_thread().name,name))
#Main Program
#Create a Sub Thread
t1=threading.Thread(target=Got().Welcome,args=("BB",))
t1.start()