#Program For Running The Sub Thread With start()---Using OOPS Concept
import threading
class Got:
    def __init__(self,name):
        self.name=name
    def Welcome(self):
        print("\t {}--->Hello: {}, Welcome To Multi-Threading".format(threading.current_thread().name,self.name))
#Main Program
#Create Sub Thread
t1=threading.Thread(target=Got("RS").Welcome)
#Dispatch the Sub Thread
t1.start()