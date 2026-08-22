#Univ.py<----File Name Acts As Module Name
class Univ:
    def getdata(self):
        self.uname=input("Enter University Name: ")
        self.uloc=input("Enter University Location: ")
    def dispdata(self):
        print("-"*50)
        print("University Details")
        print("-"*50)
        print("University Name:",self.uname)
        print("University Location:",self.uloc)
        print("-"*50)