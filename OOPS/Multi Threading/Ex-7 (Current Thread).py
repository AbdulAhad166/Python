#Program For Getting Currently Executing Thread
import threading
t=threading.current_thread()
print("Default Thread Name: ",t.name)
print("--------------OR-------------------")
print("Default Thread Name: ",threading.current_thread().name)