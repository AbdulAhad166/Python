#Program For Finding Number of Threads Which Are Running
import threading
print("Thread Name= ",threading.current_thread().name)
print("Number of Active Threads= ",threading.active_count())    