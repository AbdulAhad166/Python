#Others2.pt<---Main Program<----Data Abstraction
from Account2 import Account
ac=Account()  #Object Creation
ac.getaccdet()  #Calling Instance Method
print("-"*50)
print("Account Number: ",ac.acno)   #acno is Encapsulated
print("Account Holder Name: ",ac.cname)   #cname is Not Encapsulated
print("Account Balance: ",ac.bal)     #bal is Encapsulated
print("Account Pin Number: ",ac.pin)   #pin is Encapsulated
print("Account Branch Name: ",ac.bname)   #bname is Not Encapsulated
print("-"*50)
