#Program for Generating 1 to n Numbers By Using Threads After Each and Every Second
import threading,time
def numbergen(n):
    if n<0:
        print("\t {}--->{} is Invalid Input".format(threading.current_thread().name,n))
    else:
        print("Numbers Till:{}".format(n))
        for i in range(1,n+1):
            print("\t{}--->Number:{}".format(threading.current_thread().name,i))
            time.sleep(1)
t1=threading.Thread(target=numbergen,args=(int(input("Enter How Many Number Do You Want: ")),))
t1.start()
