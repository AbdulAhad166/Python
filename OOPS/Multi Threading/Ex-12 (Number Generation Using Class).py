#Program For Generating 1 to N Numbers Using Threads After Each and Every Second
import threading,time
class Numbers:
    def generate(self,n):
        if n<0:
            print("\t {}--->{} is Invalid Input".format(threading.current_thread().name,n))
        else:
            print("Numbers Till: {}".format(n))
            for i in range(1,n+1):
                print("\t{}--->Number={}".format(threading.current_thread().name,i))
                time.sleep(1)
#Main Program
t1=threading.Thread(target=Numbers().generate,args=(int(input("Enter How Many Numbers Do You Want:")),))
t1.start()