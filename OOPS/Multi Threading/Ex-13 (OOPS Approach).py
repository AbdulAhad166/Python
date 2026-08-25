#Program For Running The Sub Threads Using OOPS
import threading
class Got:
    def Welcome(self,name):
        print("{}--->{}--->Welcome to Multi-Threading".format(threading.current_thread().name,name))
#Main Program
#Create An Object of Class of Got to Call Instance Class
g=Got()
#Create a Sub Thread
t1=threading.Thread(target=g.Welcome,args=("BB",))
t1.start()