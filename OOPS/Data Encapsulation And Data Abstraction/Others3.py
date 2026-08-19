#Others3.py<---Main Program<----Data Abstraction\
from Account3 import Account
ac=Account()   #Object Creation
ac.getaccdet()  #Cannot Call Instance Method Because It is Encapsulated
print("-"*50)
print("Account Number: ",ac.acno)
print("Account Name: ",ac.cname)
print("Account Balance: ",ac.bal)
print("Account Pin Number: ",ac.pin)
print("Account Branch Name: ",ac.bname)
print("-"*50)