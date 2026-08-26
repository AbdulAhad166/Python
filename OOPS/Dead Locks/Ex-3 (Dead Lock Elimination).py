#Program for Eliminating the Dead Lock Occurrence
import threading,time
def table(n):
    #Acquire the Lock
    L.acquire()
    if n<=0:
        print("\t {}--->{} Invalid Input".format(threading.current_thread().name,n))
    else:
        for i in range(1,11):
            print("\t {}--->{} x {} = {}".format(threading.current_thread().name,n,i,n*i))
            time.sleep(1)
    #Release the Lock
    L.release()
#Main Program
#Create Lock Class Object
L=threading.Lock()
#Create Multiple Sub Threads For Generating Multiple Tables
t1=threading.Thread(target=table,args=(18,))
t2=threading.Thread(target=table,args=(19,))
t3=threading.Thread(target=table,args=(20,))
t4=threading.Thread(target=table,args=(-21,))
#Dispatch the Sub Threads
t1.start()
t2.start()
t3.start()
t4.start()