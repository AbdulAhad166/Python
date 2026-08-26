#Program For Showing The Dead Lock Occurrence With OOPS Concept
import threading,time
class Multitable:
    def table(self,n):
        if n<=0:
            print("\t {}--->{} Invalid Input".format(threading.current_thread().name,n))
        else:
            for i in range(1,11):
                print("\t {}--->{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
                time.sleep(1)
#Main Program
#Create Multiple Sub Threads To Multiple Tables
t1=threading.Thread(target=Multitable().table,args=(16,))
t2=threading.Thread(target=Multitable().table,args=(18,))
t3=threading.Thread(target=Multitable().table,args=(9,))
t4=threading.Thread(target=Multitable().table,args=(2,))
#Dispatch The Sub Threads
t1.start()
t2.start()
t3.start()
t4.start()
