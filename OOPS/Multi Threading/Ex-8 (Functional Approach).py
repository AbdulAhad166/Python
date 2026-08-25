#Program For Running The Sub Thread with start()
import threading
def welcome(name):
    print("\t {}--->Welcome To Multi-Threading".format(threading.current_thread().name,name))
#Main Program
#Create A Sub Thread
t1=threading.Thread(target=welcome,args=("BB",))
#Dispatch the Thread using start()
t1.start()  