#Program for Sending The Amount to Persons and Checking the Bank Balance
import threading,time
class Bank:
    acbal=2000
    L=threading.Lock()
    def withdraw(self,wamt):
        Bank.L.acquire()
        if wamt>Bank.acbal:
            print("\t Hello: {}, INR: {} Cheque is Bounced".format(threading.current_thread().name,wamt))
            time.sleep(1)
        else:
            Bank.acbal=Bank.acbal-wamt
            print("\t Hello: {}, INR: {} Cheque is Cleared".format(threading.current_thread().name,wamt))
            print("\t Remaining Balance: ",Bank.acbal)
            time.sleep(1)
        Bank.L.release()
#Main Program
#Create Sub Threads
t1=threading.Thread(target=Bank().withdraw,args=(500,))
t1.name="BB"
t2=threading.Thread(target=Bank().withdraw,args=(500,))
t2.name="RS"
t3=threading.Thread(target=Bank().withdraw,args=(1000,))
t3.name="NB"
t4=threading.Thread(target=Bank().withdraw,args=(2000,))
t4.name="HD"
#Dispatch the Sub Threads
t1.start()
t2.start()
t3.start()
t4.start()