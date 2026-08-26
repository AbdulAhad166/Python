#Program for Showing Dead Lock Elimination
import threading,time
class MulTable:
	#Step-1: Create Lock Class Object
	L=threading.Lock()  # Here L is Called Class Level Data Member
	def __init__(self,n):
		self.n=n
	def   table(self):
		#Step-2: Acquire the Lock
		MulTable.L.acquire()
		print("----------------------------------------------------------------")
		if self.n<=0:
			print("\t{}--> {} is Invalid Input".format(threading.current_thread().name,self.n))
		else:
			for i in range(1,11):
				print("\t{}-->{} x {} = {}".format(threading.current_thread().name,self.n,i,self.n*i))
				time.sleep(0.001)
		print("----------------------------------------------------------------")
		#Step-3: Release the Lock
		MulTable.L.release()

#Main Program
#Create Multiple Threads for generating Mul Tables
t1=threading.Thread(target=MulTable(16).table)
t2=threading.Thread(target=MulTable(19).table)
t3=threading.Thread(target=MulTable(-18).table,)
t4=threading.Thread(target=MulTable(9).table)
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()