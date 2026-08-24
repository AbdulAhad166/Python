#Program For Showing Default Thread Name
import threading
tname=threading.current_thread().name    #Gives the Actual Thread Name That is Present
print("Default Thread Name= ",tname)
print("Number Threads= ",threading.active_count()) #Counts How Many Threads Are Present