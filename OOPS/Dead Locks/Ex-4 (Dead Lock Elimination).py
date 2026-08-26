#Program For Eliminating Dead Lock Occurrence
import threading,time
class Multitable:
    def table(self,n):
        #Acquire the Lock
        L.acquire()
        if n<=0:
            print("\t {}--->{} Invalid Input".format(threading.current_thread().name,n))
        else:
            for i in range(1,11):
                print("\t {}--->{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
                time.sleep(0.0000001)
        #Release the Lock
        L.release()
#Main Program
#Create Lock Class Object
L=threading.Lock()
#Create Multiple Sub Threads for Multiple Tables
t1=threading.Thread(target=Multitable().table,args=(19,))
t2=threading.Thread(target=Multitable().table,args=(20,))
t3=threading.Thread(target=Multitable().table,args=(-21,))
t4=threading.Thread(target=Multitable().table,args=(22,))
#Dispatch the Sub Threads
t1.start()
t2.start()
t3.start()
t4.start()
