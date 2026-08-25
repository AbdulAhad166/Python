#Program For Setting The Name And Getting The Name of Sub Thread
import threading
def Welcome(name):
    print("\t {}--->Hello {},Welcome To Multi-Threading".format(threading.current_thread().name,name))
#Main Program
#Create A Sub Thread
t1=threading.Thread(target=Welcome,args=("BB",))
print("Default Sub Thread Name Before: ",t1.name)  #Getter Function 
t1.name="HYD"
print("Default Sub Thread Name After: ",t1.name)
#Dispatch The Sub Thread
t1.start()