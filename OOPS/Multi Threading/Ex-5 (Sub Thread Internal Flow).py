#Program For Showing The Internal Flow of Sub Threads Along With Main Thread
import threading
def Hello():
    print("Hello() Executed By: ",threading.current_thread().name)
def World():
    print("World() Executed By: ",threading.current_thread().name)
def Display():
    print("Display() Executed By: ",threading.current_thread().name)
#Main Program
print("Program Execution Started: ",threading.current_thread().name)
#Create Three Sub Threads For Executing Three Functions
t1=threading.Thread(target=Hello) #Here t1 is Called Sub Thread object whose default name is thread-1
t2=threading.Thread(target=World) #Here t2 is Called Sub Thread Object Whose default name is thread-2
t3=threading.Thread(target=Display) #Here t3 is Called Sub Thread Object Whose default name is thread-3
#Dispatch the Sub Threads
t1.start()
t2.start()
t3.start()
#Join The Threads
t1.join()
t2.join()
t3.join()
print("Program Execution Ended: ",threading.current_thread().name)

