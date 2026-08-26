#Program For Eliminating Dead Lock using Different Process
import threading,time
class Multitable:
    L=threading.Lock()  #Here L is Called Class Level Data Member
    def table(self,n):
        #Acquire the Lock
        Multitable.L.acquire()
        if n<=0:
            print("\t {}--->{} Invalid Input".format(threading.current_thread().name,n))
        else:
            for i in range(1,11):
                print("\t {}--->{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
                time.sleep(1)
        #Release the Lock
        Multitable.L.release()
#Main Program
#Create Multiple Sub Threads For Multiple Tables
t1=threading.Thread(target=Multitable().table,args=(3,))
t2=threading.Thread(target=Multitable().table,args=(6,))
t3=threading.Thread(target=Multitable().table,args=(9,))
t4=threading.Thread(target=Multitable().table,args=(11,))
#Dispatch the Sub Threads
t1.start()
t2.start()
t3.start()
t4.start()
