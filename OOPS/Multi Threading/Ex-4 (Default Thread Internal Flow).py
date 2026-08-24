#Program For Showing The Internal Flow of Default Thread --- Main Thread
import threading
def Hello():
    print("Hello() Executed By: ",threading.current_thread().name)
def World():
    print("World() Executed By: ",threading.current_thread().name)
def Display():
    print("Display() Executed By: ",threading.current_thread().name)
#Main Program
print("Program Execution Started",threading.current_thread().name)
print("-----------------------------------------------")
Hello()
print("-----------------------------------------------")
World()
print("-----------------------------------------------")
Display()
print("-----------------------------------------------")
print("Program Execution Ended",threading.current_thread().name)